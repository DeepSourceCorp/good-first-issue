#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import random
import re
import threading
import time
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from operator import itemgetter
from os import getenv, path
from typing import TypedDict, Dict, Union, Sequence, Optional

import toml

from github3 import exceptions, login
from numerize import numerize
from emoji import emojize
from slugify import slugify
from loguru import logger

MAX_CONCURRENCY = 5  # max number of requests to make to GitHub in parallel
REPO_DATA_FILE = "data/repositories.toml"
REPO_GENERATED_DATA_FILE = "data/generated.json"
TAGS_GENERATED_DATA_FILE = "data/tags.json"
GH_URL_PATTERN = re.compile(r"[http://|https://]?github.com/(?P<owner>[\w\.-]+)/(?P<name>[\w\.-]+)/?")
LABELS_DATA_FILE = "data/labels.json"
ISSUE_STATE = "open"
ISSUE_SORT = "created"
ISSUE_SORT_DIRECTION = "desc"
ISSUE_LIMIT = 10
SLUGIFY_REPLACEMENTS = [["#", "sharp"], ["+", "plus"]]
MAX_INACTIVITY_DAYS = 90  # Skip repos inactive for more than 3 months

if not path.exists(LABELS_DATA_FILE):
    raise RuntimeError("No labels data file found. Exiting.")

with open(LABELS_DATA_FILE) as labels_file:
    LABELS_DATA = json.load(labels_file)

    ISSUE_LABELS = LABELS_DATA["labels"]


class RepoNotFoundException(Exception):
    """Exception class for repo not found."""


class GitHubRateLimiter:
    """Thread-safe rate limiter for GitHub API requests."""

    def __init__(self, client, requests_per_second=1.0):
        self._client = client
        self._lock = threading.Lock()
        self._min_interval = 1.0 / requests_per_second
        self._last_request_time = 0.0
        self._remaining: Optional[int] = None
        self._reset_time: Optional[float] = None
        self._paused_until = 0.0

    def acquire(self):
        """Block until it's safe to make an API request."""
        with self._lock:
            # Check for coordinated pause
            if time.time() < self._paused_until:
                wait_time = self._paused_until - time.time()
                logger.info("Waiting {:.0f}s for rate limit reset", wait_time)
                time.sleep(wait_time)

            # Refresh rate limit info periodically
            if self._remaining is None or self._remaining % 100 == 0:
                self._update_rate_limit()

            # Proactive pause if quota low
            if self._remaining is not None and self._remaining < 100:
                if self._reset_time:
                    wait_time = max(0.0, self._reset_time - time.time() + 5)
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

    def _update_rate_limit(self):
        try:
            info = self._client.rate_limit()["resources"]["core"]
            self._remaining = info["remaining"]
            self._reset_time = info["reset"]
            logger.debug("Rate limit: {}/{}", self._remaining, info["limit"])
        except Exception as e:
            logger.warning("Failed to check rate limit: {}", e)

    def report_rate_limit_hit(self, retry_after: Optional[int] = None):
        """Call when rate limit or 429 received - triggers coordinated pause."""
        with self._lock:
            self._update_rate_limit()
            if retry_after is not None and retry_after > 0:
                wait_time = float(retry_after) + 5
            elif self._reset_time and self._reset_time > time.time():
                wait_time = max(60.0, self._reset_time - time.time() + 5)
            else:
                wait_time = 60.0
            self._paused_until = max(self._paused_until, time.time() + wait_time)
            self._remaining = 0
            logger.warning("Rate limit hit. All workers pause for {:.0f}s", wait_time)


def parse_github_url(url: str) -> dict:
    """Take the GitHub repo URL and return a tuple with owner login and repo name."""
    match = GH_URL_PATTERN.search(url)
    if match:
        return match.groupdict()
    return {}


class RepositoryIdentifier(TypedDict):
    owner: str
    name: str


RepositoryInfo = Dict["str", Union[str, int, Sequence]]


def get_repository_info(
    identifier: RepositoryIdentifier, client, rate_limiter: GitHubRateLimiter
) -> Optional[RepositoryInfo]:
    """Get the relevant information needed for the repository from its owner login and name."""
    owner, name = identifier["owner"], identifier["name"]

    logger.info("Getting info for {}/{}", owner, name)

    max_retries = 3

    for attempt in range(max_retries):
        try:
            rate_limiter.acquire()
            repository = client.repository(owner, name)
            # Don't find issues inside archived repos.
            if repository.archived:
                return None

            # Skip repos with no recent activity
            days_since_push = (datetime.now(timezone.utc) - repository.pushed_at).days
            if days_since_push > MAX_INACTIVITY_DAYS:
                logger.info("\t skipping due to inactivity ({} days since last push)", days_since_push)
                return None

            good_first_issues: set = set()
            for label in ISSUE_LABELS:
                rate_limiter.acquire()
                issues_for_label = repository.issues(
                    labels=label,
                    state=ISSUE_STATE,
                    number=ISSUE_LIMIT,
                    sort=ISSUE_SORT,
                    direction=ISSUE_SORT_DIRECTION,
                )
                for issue in issues_for_label:
                    # Filter out pull requests, which GitHub's issue endpoint returns
                    if getattr(issue, "pull_request_urls", None):
                        continue
                    good_first_issues.add(issue)

            logger.info("\t found {} good first issues", len(good_first_issues))
            # check if repo has at least one good first issue
            if good_first_issues and repository.language:
                # store the repo info
                info: RepositoryInfo = {}
                info["name"] = name
                info["owner"] = owner
                info["description"] = emojize(repository.description or "")
                info["language"] = repository.language
                info["slug"] = slugify(repository.language, replacements=SLUGIFY_REPLACEMENTS)
                info["url"] = repository.html_url
                info["stars"] = repository.stargazers_count
                info["stars_display"] = numerize.numerize(repository.stargazers_count)
                info["last_modified"] = repository.pushed_at.isoformat()
                info["id"] = str(repository.id)

                # Sort by created_at descending and get the latest issues up to ISSUE_LIMIT
                sorted_issues = sorted(good_first_issues, key=lambda x: x.created_at, reverse=True)[:ISSUE_LIMIT]

                # get the latest issues with the tag
                issues = []
                for issue in sorted_issues:
                    issues.append(
                        {
                            "title": issue.title,
                            "url": issue.html_url,
                            "number": issue.number,
                            "comments_count": issue.comments_count,
                            "created_at": issue.created_at.isoformat(),
                        }
                    )

                info["issues"] = issues
                return info
            else:
                logger.info("\t skipping due to insufficient issues or info")
                return None

        except (exceptions.ForbiddenError, exceptions.ClientError) as exc:
            # Check if this is a rate limit (403 Forbidden or 429 Too Many Requests)
            status_code = getattr(exc, "code", None)
            is_rate_limit = isinstance(exc, exceptions.ForbiddenError) or status_code == 429
            if not is_rate_limit:
                logger.warning("Client error ({}) on {}/{}: {}", status_code, owner, name, exc)
                return None

            response = getattr(exc, "response", None)
            retry_after_str = getattr(response, "headers", {}).get("Retry-After") if response else None
            retry_after = int(retry_after_str) if retry_after_str and retry_after_str.isdigit() else None

            rate_limiter.report_rate_limit_hit(retry_after=retry_after)
            if attempt < max_retries - 1:
                backoff = (2**attempt) + random.uniform(0.5, 1.5)
                logger.warning(
                    "Rate limited on {}/{} (attempt {}/{}). Retrying after coordinated pause and {:.1f}s backoff...",
                    owner,
                    name,
                    attempt + 1,
                    max_retries,
                    backoff,
                )
                time.sleep(backoff)
            else:
                logger.error("Rate limit exceeded after {} retries: {}/{}", max_retries, owner, name)
                return None

        except (exceptions.ConnectionError, exceptions.ServerError) as exc:
            if attempt < max_retries - 1:
                backoff = (2**attempt) + random.uniform(0.5, 1.5)
                logger.warning(
                    "Network error ({}) on {}/{} (attempt {}/{}). Retrying in {:.1f}s...",
                    type(exc).__name__,
                    owner,
                    name,
                    attempt + 1,
                    max_retries,
                    backoff,
                )
                time.sleep(backoff)
            else:
                logger.error(
                    "Failed to fetch {}/{} after {} retries due to {}: {}",
                    owner,
                    name,
                    max_retries,
                    type(exc).__name__,
                    exc,
                )
                return None

        except exceptions.NotFoundError:
            logger.warning("Not Found: {}/{}", owner, name)
            return None

    return None


if __name__ == "__main__":
    # parse the repositories data file and get the list of repos
    # for generating pages for.

    if not path.exists(REPO_DATA_FILE):
        raise RuntimeError("No config data file found. Exiting.")

    # if the GitHub Access Token isn't found, raise an error
    if not getenv("GH_ACCESS_TOKEN"):
        raise RuntimeError("Access token not present in the env variable `GH_ACCESS_TOKEN`")

    REPOSITORIES = []
    TAGS: Counter = Counter()
    with open(REPO_DATA_FILE, "r") as data_file:
        DATA = toml.load(REPO_DATA_FILE)

        logger.info(
            "Found {} repository entries in {}",
            len(DATA["repositories"]),
            REPO_DATA_FILE,
        )

        # pre-process the URLs and only continue with the list of valid GitHub URLs
        repositories = list(filter(bool, [parse_github_url(url) for url in DATA["repositories"]]))

        # shuffle the order of the repositories
        random.shuffle(repositories)

        # Create shared client and rate limiter
        client = login(token=getenv("GH_ACCESS_TOKEN"))
        rate_limiter = GitHubRateLimiter(client, requests_per_second=1.0)

        # Wrapper to pass shared dependencies
        def process_repo(identifier):
            return get_repository_info(identifier, client, rate_limiter)

        with ThreadPoolExecutor(max_workers=MAX_CONCURRENCY) as executor:
            results = executor.map(process_repo, repositories)

        # filter out repositories with valid data and increment tag counts
        for result in results:
            if result:
                REPOSITORIES.append(result)
                TAGS[result["language"]] += 1

    # write to generated JSON files

    with open(REPO_GENERATED_DATA_FILE, "w") as file_desc:
        json.dump(REPOSITORIES, file_desc)
    logger.info("Wrote data for {} repos to {}", len(REPOSITORIES), REPO_GENERATED_DATA_FILE)

    # use only those tags that have at least three occurrences
    tags = [
        {
            "language": key,
            "count": value,
            "slug": slugify(key, replacements=SLUGIFY_REPLACEMENTS),
        }
        for (key, value) in TAGS.items()
        if value >= 3
    ]
    tags_sorted = sorted(tags, key=itemgetter("count"), reverse=True)
    with open(TAGS_GENERATED_DATA_FILE, "w") as file_desc:
        json.dump(tags_sorted, file_desc)
    logger.info("Wrote {} tags to {}", len(tags), TAGS_GENERATED_DATA_FILE)
