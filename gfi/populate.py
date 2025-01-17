#!/usr/bin/env python
# -*- coding: utf-8 -*-

import itertools
import json
import random
import re
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from operator import itemgetter
from os import getenv, path
from typing import TypedDict, Dict, Union, Sequence, Optional, Mapping

import toml  # Ensure this library is installed: pip install toml

from github3 import exceptions, login  # Ensure this library is installed: pip install github3.py
from numerize import numerize  # Ensure this library is installed: pip install numerize
from emoji import emojize  # Ensure this library is installed: pip install emoji
from slugify import slugify  # Ensure this library is installed: pip install python-slugify
from loguru import logger  # Ensure this library is installed: pip install loguru

# Configuration constants
MAX_CONCURRENCY = 25  # Max number of parallel GitHub requests
MAX_REPOSITORIES = 500  # Max repositories processed in one session
REPO_DATA_FILE = "data/repositories.toml"  # Input file with repository data
REPO_GENERATED_DATA_FILE = "data/generated.json"  # Output file for repository info
TAGS_GENERATED_DATA_FILE = "data/tags.json"  # Output file for tag info
LABELS_DATA_FILE = "data/labels.json"  # File containing labels for issues
ISSUE_STATE = "open"  # Only process open issues
ISSUE_SORT = "created"  # Sort issues by creation date
ISSUE_SORT_DIRECTION = "desc"  # Sort issues in descending order
ISSUE_LIMIT = 10  # Max issues fetched per repository
SLUGIFY_REPLACEMENTS = [["#", "sharp"], ["+", "plus"]]  # Replacements for slug generation

# Ensure the labels file exists
if not path.exists(LABELS_DATA_FILE):
    raise RuntimeError("No labels data file found. Exiting.")

# Load labels data
with open(LABELS_DATA_FILE) as labels_file:
    LABELS_DATA = json.load(labels_file)
    ISSUE_LABELS = LABELS_DATA["labels"]

# Custom exception for missing repositories
class RepoNotFoundException(Exception):
    """Exception raised when a repository is not found."""

# Parse GitHub repository URL
def parse_github_url(url: str) -> dict:
    """Extract owner and name from a GitHub repository URL."""
    match = re.search(r"[http://|https://]?github.com/(?P<owner>[\w\.-]+)/(?P<name>[\w\.-]+)/?", url)
    return match.groupdict() if match else {}

# Type definitions for repository data
class RepositoryIdentifier(TypedDict):
    owner: str
    name: str

RepositoryInfo = Dict[str, Union[str, int, Sequence]]

# Fetch repository information
def get_repository_info(identifier: RepositoryIdentifier) -> Optional[RepositoryInfo]:
    """Fetch information about a repository using its owner and name."""
    owner, name = identifier["owner"], identifier["name"]

    logger.info("Fetching information for {}/{}", owner, name)

    try:
        client = login(token=getenv("GH_ACCESS_TOKEN"))  # Authenticate GitHub client
        repository = client.repository(owner, name)  # Fetch repository

        if repository.archived:
            return None  # Skip archived repositories

        # Fetch issues labeled as "good first issue"
        good_first_issues = set(
            itertools.chain.from_iterable(
                repository.issues(
                    labels=label,
                    state=ISSUE_STATE,
                    number=ISSUE_LIMIT,
                    sort=ISSUE_SORT,
                    direction=ISSUE_SORT_DIRECTION,
                )
                for label in ISSUE_LABELS
            )
        )
        
        logger.info("Found {} good first issues.", len(good_first_issues))

        if good_first_issues and repository.language:
            info = {
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
                "issues": [
                    {
                        "title": issue.title,
                        "url": issue.html_url,
                        "number": issue.number,
                        "comments_count": issue.comments_count,
                        "created_at": issue.created_at.isoformat(),
                    }
                    for issue in good_first_issues
                ],
            }
            return info

    except exceptions.NotFoundError:
        logger.warning("Repository not found: {}/{}", owner, name)
    except exceptions.ForbiddenError:
        logger.warning("Rate-limited: {}/{}", owner, name)
    except exceptions.ConnectionError:
        logger.warning("Connection error: {}/{}", owner, name)

    return None

if __name__ == "__main__":
    # Validate configuration files
    if not path.exists(REPO_DATA_FILE):
        raise RuntimeError("Configuration file not found. Exiting.")

    if not getenv("GH_ACCESS_TOKEN"):
        raise RuntimeError("GitHub Access Token is missing. Please set GH_ACCESS_TOKEN.")

    REPOSITORIES = []
    TAGS = Counter()

    # Load repository data from file
    with open(REPO_DATA_FILE, "r") as data_file:
        DATA = toml.load(data_file)
        repositories = [parse_github_url(url) for url in DATA["repositories"] if parse_github_url(url)]

    random.shuffle(repositories)  # Shuffle repository list

    # Fetch repository information concurrently
    with ThreadPoolExecutor(max_workers=MAX_CONCURRENCY) as executor:
        results = executor.map(get_repository_info, repositories[:MAX_REPOSITORIES])

    for result in results:
        if result:
            REPOSITORIES.append(result)
            TAGS[result["language"]] += 1

    # Write repository data to JSON
    with open(REPO_GENERATED_DATA_FILE, "w") as file:
        json.dump(REPOSITORIES, file)
    logger.info("Saved repository data to {}", REPO_GENERATED_DATA_FILE)

    # Write tag data to JSON
    tags = [
        {
            "language": key,
            "count": value,
            "slug": slugify(key, replacements=SLUGIFY_REPLACEMENTS),
        }
        for key, value in TAGS.items() if value >= 3
    ]

    with open(TAGS_GENERATED_DATA_FILE, "w") as file:
        json.dump(sorted(tags, key=itemgetter("count"), reverse=True), file)
    logger.info("Saved tag data to {}", TAGS_GENERATED_DATA_FILE)