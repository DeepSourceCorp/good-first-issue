#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""GitHub repository data fetcher for Good First Issue.

This module fetches repository data from GitHub API, analyzes issues
with beginner-friendly labels, and generates structured data for the website.
"""

import json
import random
import re
import threading
import time
from collections import Counter
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from operator import itemgetter
from os import getenv, path
from pathlib import Path
from typing import TypedDict, Dict, List, Optional, Union, Any, Set

import toml

from github3 import exceptions, login
from numerize import numerize
from emoji import emojize
from slugify import slugify
from loguru import logger

# Configuration constants
MAX_CONCURRENCY = 5  # max number of requests to make to GitHub in parallel
DEFAULT_REQUESTS_PER_SECOND = 1.0

# File paths
REPO_DATA_FILE = "data/repositories.toml"
REPO_GENERATED_DATA_FILE = "data/generated.json"
TAGS_GENERATED_DATA_FILE = "data/tags.json"
LABELS_DATA_FILE = "data/labels.json"

# GitHub API configuration
ISSUE_STATE = "open"
ISSUE_SORT = "created"
ISSUE_SORT_DIRECTION = "desc"
ISSUE_LIMIT = 10

# Repository filtering
MAX_INACTIVITY_DAYS = 90  # Skip repos inactive for more than 3 months
MIN_TAG_OCCURRENCES = 3  # Minimum occurrences for a tag to be included

# Data processing
SLUGIFY_REPLACEMENTS = [["#", "sharp"], ["+", "plus"]]
GH_URL_PATTERN = re.compile(r"[http://|https://]?github.com/(?P<owner>[\w\.-]+)/(?P<name>[\w\.-]+)/?")

# Load labels data at module level
def _load_labels_data() -> List[str]:
    """Load labels data from file.
    
    Returns:
        List of issue labels
        
    Raises:
        RuntimeError: If labels file doesn't exist
    """
    labels_file = Path(LABELS_DATA_FILE)
    if not labels_file.exists():
        raise RuntimeError(f"No labels data file found at {LABELS_DATA_FILE}. Exiting.")
    
    try:
        with open(labels_file, encoding="utf-8") as f:
            data = json.load(f)
            return data.get("labels", [])
    except (json.JSONDecodeError, KeyError) as e:
        raise RuntimeError(f"Invalid labels data format: {e}") from e


ISSUE_LABELS = _load_labels_data()


class RepoNotFoundException(Exception):
    """Exception raised when a repository is not found on GitHub."""
    pass


class ConfigurationError(Exception):
    """Exception raised for configuration-related errors."""
    pass


class GitHubRateLimiter:
    """Thread-safe rate limiter for GitHub API requests.
    
    This class manages GitHub API rate limits by coordinating requests
    across multiple threads and implementing proactive pausing when
    the remaining quota is low.
    """

    def __init__(self, client, requests_per_second: float = DEFAULT_REQUESTS_PER_SECOND) -> None:
        """Initialize the rate limiter.
        
        Args:
            client: GitHub API client instance
            requests_per_second: Maximum requests per second to allow
        """
        self._client = client
        self._lock = threading.Lock()
        self._min_interval = 1.0 / requests_per_second
        self._last_request_time = 0.0
        self._remaining: Optional[int] = None
        self._reset_time: Optional[float] = None
        self._paused_until = 0.0

    def acquire(self) -> None:
        """Block until it's safe to make an API request."""
        with self._lock:
            # Check for coordinated pause
            current_time = time.time()
            if current_time < self._paused_until:
                wait_time = self._paused_until - current_time
                logger.info("Waiting {:.0f}s for rate limit reset", wait_time)
                time.sleep(wait_time)

            # Refresh rate limit info periodically
            if self._remaining is None or self._remaining % 100 == 0:
                self._update_rate_limit()

            # Proactive pause if quota low
            if self._remaining is not None and self._remaining < 100:
                if self._reset_time:
                    wait_time = max(0, self._reset_time - time.time() + 5)
                    if wait_time > 0:
                        logger.warning("Low quota ({}). Pausing {:.0f}s", self._remaining, wait_time)
                        self._paused_until = time.time() + wait_time
                        time.sleep(wait_time)
                        self._remaining = None

            # Enforce minimum interval
            elapsed = time.time() - self._last_request_time
            if elapsed < self._min_interval:
                time.sleep(self._min_interval - elapsed)

            self._last_request_time = time.time()
            if self._remaining:
                self._remaining -= 1

    def _update_rate_limit(self) -> None:
        """Update rate limit information from GitHub API."""
        try:
            info = self._client.rate_limit()['resources']['core']
            self._remaining = info['remaining']
            self._reset_time = info['reset']
            logger.debug("Rate limit: {}/{}", self._remaining, info['limit'])
        except Exception as e:
            logger.warning("Failed to check rate limit: {}", e)

    def report_rate_limit_hit(self) -> None:
        """Call when ForbiddenError received - triggers coordinated pause."""
        with self._lock:
            self._update_rate_limit()
            if self._reset_time:
                wait_time = max(60, self._reset_time - time.time() + 5)
            else:
                wait_time = 60
            self._paused_until = time.time() + wait_time
            self._remaining = 0
            logger.warning("Rate limit hit. All workers pause for {:.0f}s", wait_time)


def parse_github_url(url: str) -> Dict[str, str]:
    """Parse GitHub repository URL and extract owner and name.
    
    Args:
        url: GitHub repository URL
        
    Returns:
        Dictionary with 'owner' and 'name' keys, or empty dict if invalid
    """
    match = GH_URL_PATTERN.search(url)
    return match.groupdict() if match else {}


class RepositoryIdentifier(TypedDict):
    """Type definition for repository identifier."""
    owner: str
    name: str


class IssueInfo(TypedDict):
    """Type definition for issue information."""
    title: str
    url: str
    number: int
    comments_count: int
    created_at: str


class RepositoryInfo(TypedDict):
    """Type definition for repository information."""
    name: str
    owner: str
    description: str
    language: str
    slug: str
    url: str
    stars: int
    stars_display: str
    last_modified: str
    id: str
    issues: List[IssueInfo]


class TagInfo(TypedDict):
    """Type definition for tag information."""
    language: str
    count: int
    slug: str


def get_repository_info(
    identifier: RepositoryIdentifier,
    client,
    rate_limiter: GitHubRateLimiter
) -> Optional[RepositoryInfo]:
    """Fetch and process repository information from GitHub API.
    
    Args:
        identifier: Repository owner and name
        client: GitHub API client
        rate_limiter: Rate limiter instance
        
    Returns:
        Repository information dict or None if repository doesn't meet criteria
    """
    owner, name = identifier["owner"], identifier["name"]

    logger.info("Getting info for {}/{}", owner, name)

    max_retries = 3

    for attempt in range(max_retries):
        try:
            rate_limiter.acquire()
            repository = client.repository(owner, name)
            
            # Skip archived repositories
            if repository.archived:
                logger.info("\t skipping archived repository")
                return None

            # Skip repositories with no recent activity
            days_since_push = (datetime.now(timezone.utc) - repository.pushed_at).days
            if days_since_push > MAX_INACTIVITY_DAYS:
                logger.info("\t skipping due to inactivity ({} days since last push)", days_since_push)
                return None

            # Fetch issues with beginner-friendly labels
            good_first_issues: Set = set()
            for label in ISSUE_LABELS:
                rate_limiter.acquire()
                try:
                    issues_for_label = repository.issues(
                        labels=label,
                        state=ISSUE_STATE,
                        number=ISSUE_LIMIT,
                        sort=ISSUE_SORT,
                        direction=ISSUE_SORT_DIRECTION,
                    )
                    good_first_issues.update(issues_for_label)
                except Exception as e:
                    logger.warning("Failed to fetch issues for label '{}': {}", label, e)
                    continue
                    
            logger.info("\t found {} good first issues", len(good_first_issues))
            
            # Check if repository meets criteria
            if not good_first_issues or not repository.language:
                logger.info("\t skipping due to insufficient issues or info")
                return None

            # Build repository information
            info: RepositoryInfo = {
                "name": name,
                "owner": owner,
                "description": emojize(repository.description or ""),
                "language": repository.language,
                "slug": slugify(repository.language, replacements=SLUGIFY_REPLACEMENTS),
                "url": repository.html_url,
                "stars": repository.stargazers_count,
                "stars_display": numerize.numerize(repository.stargazers_count),
                "last_modified": repository.pushed_at.isoformat(),
                "id": str(repository.id),
                "issues": []
            }

            # Process issues
            issues: List[IssueInfo] = []
            for issue in good_first_issues:
                issue_info: IssueInfo = {
                    "title": issue.title,
                    "url": issue.html_url,
                    "number": issue.number,
                    "comments_count": issue.comments_count,
                    "created_at": issue.created_at.isoformat(),
                }
                issues.append(issue_info)

            info["issues"] = issues
            return info

        except exceptions.ForbiddenError:
            rate_limiter.report_rate_limit_hit()
            if attempt < max_retries - 1:
                logger.warning("Rate limited on {}/{}. Retrying after coordinated pause...", owner, name)
                continue
            else:
                logger.error("Rate limit exceeded after {} retries: {}/{}", max_retries, owner, name)
                return None

        except exceptions.NotFoundError:
            logger.warning("Not Found: {}/{}", owner, name)
            return None

        except exceptions.ConnectionError as e:
            logger.warning("Connection error: {}/{} - {}", owner, name, e)
            return None
        except Exception as e:
            logger.error("Unexpected error processing {}/{}: {}", owner, name, e)
            if attempt < max_retries - 1:
                continue
            return None

    return None


def _validate_configuration() -> None:
    """Validate required configuration and environment variables.
    
    Raises:
        ConfigurationError: If required files or environment variables are missing
    """
    if not path.exists(REPO_DATA_FILE):
        raise ConfigurationError(f"Repository data file not found: {REPO_DATA_FILE}")
    
    if not getenv("GH_ACCESS_TOKEN"):
        raise ConfigurationError(
            "GitHub access token not found in environment variable 'GH_ACCESS_TOKEN'. "
            "Please set this variable and try again."
        )


def _load_repositories_data() -> List[RepositoryIdentifier]:
    """Load and validate repositories data from TOML file.
    
    Returns:
        List of repository identifiers
        
    Raises:
        ConfigurationError: If data file is invalid
    """
    try:
        with open(REPO_DATA_FILE, "r", encoding="utf-8") as data_file:
            data = toml.load(data_file)
            
        if "repositories" not in data:
            raise ConfigurationError("Missing 'repositories' key in data file")
            
        repository_urls = data["repositories"]
        if not isinstance(repository_urls, list):
            raise ConfigurationError("'repositories' should be a list")
            
        logger.info("Found {} repository entries in {}", len(repository_urls), REPO_DATA_FILE)
        
        # Parse and validate URLs
        repositories = []
        invalid_urls = []
        
        for url in repository_urls:
            parsed = parse_github_url(url)
            if parsed:
                repositories.append(parsed)
            else:
                invalid_urls.append(url)
        
        if invalid_urls:
            logger.warning("Found {} invalid repository URLs, skipping them", len(invalid_urls))
            
        if not repositories:
            raise ConfigurationError("No valid repository URLs found")
            
        # Shuffle for random processing order
        random.shuffle(repositories)
        return repositories
        
    except toml.TomlDecodeError as e:
        raise ConfigurationError(f"Invalid TOML format in {REPO_DATA_FILE}: {e}") from e
    except Exception as e:
        raise ConfigurationError(f"Error loading repositories data: {e}") from e


def _process_repositories(
    repositories: List[RepositoryIdentifier],
    client,
    rate_limiter: GitHubRateLimiter
) -> List[RepositoryInfo]:
    """Process repositories using thread pool.
    
    Args:
        repositories: List of repository identifiers
        client: GitHub API client
        rate_limiter: Rate limiter instance
        
    Returns:
        List of successfully processed repository information
    """
    processed_repos: List[RepositoryInfo] = []
    
    def process_repo(identifier: RepositoryIdentifier) -> Optional[RepositoryInfo]:
        """Wrapper function for thread pool processing."""
        return get_repository_info(identifier, client, rate_limiter)
    
    with ThreadPoolExecutor(max_workers=MAX_CONCURRENCY) as executor:
        # Use as_completed for better error handling and progress tracking
        future_to_repo = {
            executor.submit(process_repo, repo): repo for repo in repositories
        }
        
        for future in as_completed(future_to_repo):
            repo_identifier = future_to_repo[future]
            try:
                result = future.result()
                if result:
                    processed_repos.append(result)
                    logger.info("Successfully processed {}/{}", 
                               result["owner"], result["name"])
            except Exception as e:
                logger.error("Error processing repository {}/{}: {}",
                           repo_identifier["owner"], repo_identifier["name"], e)
    
    return processed_repos


def _generate_tags_data(repositories: List[RepositoryInfo]) -> List[TagInfo]:
    """Generate tags data from processed repositories.
    
    Args:
        repositories: List of processed repository information
        
    Returns:
        List of tag information sorted by count
    """
    tags_counter = Counter(repo["language"] for repo in repositories)
    
    tags = [
        {
            "language": language,
            "count": count,
            "slug": slugify(language, replacements=SLUGIFY_REPLACEMENTS),
        }
        for language, count in tags_counter.items()
        if count >= MIN_TAG_OCCURRENCES
    ]
    
    return sorted(tags, key=itemgetter("count"), reverse=True)


def _write_output_files(repositories: List[RepositoryInfo], tags: List[TagInfo]) -> None:
    """Write processed data to JSON output files.
    
    Args:
        repositories: List of repository information
        tags: List of tag information
    """
    try:
        # Write repositories data
        with open(REPO_GENERATED_DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(repositories, f, indent=2, ensure_ascii=False)
        logger.info("Wrote data for {} repos to {}", len(repositories), REPO_GENERATED_DATA_FILE)
        
        # Write tags data
        with open(TAGS_GENERATED_DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(tags, f, indent=2, ensure_ascii=False)
        logger.info("Wrote {} tags to {}", len(tags), TAGS_GENERATED_DATA_FILE)
        
    except Exception as e:
        logger.error("Failed to write output files: {}", e)
        raise


def main() -> None:
    """Main entry point for the repository data fetcher."""
    try:
        logger.info("Starting Good First Issue data fetcher")
        
        # Validate configuration
        _validate_configuration()
        
        # Load repositories data
        repositories = _load_repositories_data()
        
        # Initialize GitHub client and rate limiter
        client = login(token=getenv("GH_ACCESS_TOKEN"))
        rate_limiter = GitHubRateLimiter(client, requests_per_second=DEFAULT_REQUESTS_PER_SECOND)
        
        # Process repositories
        logger.info("Processing {} repositories with {} workers", 
                   len(repositories), MAX_CONCURRENCY)
        processed_repos = _process_repositories(repositories, client, rate_limiter)
        
        # Generate tags
        tags = _generate_tags_data(processed_repos)
        
        # Write output files
        _write_output_files(processed_repos, tags)
        
        logger.success("Successfully processed {} repositories and {} tags", 
                      len(processed_repos), len(tags))
        
    except (ConfigurationError, KeyboardInterrupt) as e:
        logger.error("Application error: {}", e)
        raise
    except Exception as e:
        logger.error("Unexpected error: {}", e)
        raise


if __name__ == "__main__":
    main()
