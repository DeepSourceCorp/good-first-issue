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

import toml
from functools import partial

from github3 import exceptions, login
from numerize import numerize
from emoji import emojize
from slugify import slugify
from loguru import logger

MAX_CONCURRENCY = 25  # max number of requests to make to GitHub in parallel
MAX_REPOSITORIES = 500  # max number of repositories populated in one session
REPO_DATA_FILE = "data/repositories.toml"
REPO_GENERATED_DATA_FILE = "data/generated.json"
TAGS_GENERATED_DATA_FILE = "data/tags.json"
GH_URL_PATTERN = re.compile(r"^(?:https?://)?(?:www\.)?github\.com/(?P<owner>[\w\.-]+)/(?P<name>[\w\.-]+)/?$")
LABELS_DATA_FILE = "data/labels.json"
ISSUE_STATE = "open"
ISSUE_SORT = "created"
ISSUE_SORT_DIRECTION = "desc"
ISSUE_LIMIT = 10
SLUGIFY_REPLACEMENTS = [["#", "sharp"], ["+", "plus"]]

if not path.exists(LABELS_DATA_FILE):
    raise RuntimeError("No labels data file found. Exiting.")

with open(LABELS_DATA_FILE) as labels_file:
    LABELS_DATA = json.load(labels_file)

    ISSUE_LABELS = LABELS_DATA["labels"]


class RepoNotFoundException(Exception):
    """Exception class for repo not found."""


def parse_github_url(url: str) -> dict:
    """Take the GitHub repo URL and return a tuple with owner login and repo name."""
    match = GH_URL_PATTERN.search(url)
    if match:
        return match.groupdict()
    return {}


class RepositoryIdentifier(TypedDict):
    owner: str
    name: str


RepositoryInfo = Dict[str, Union[str, int, Sequence]]


def get_repository_info(identifier: RepositoryIdentifier, client=None) -> Optional[RepositoryInfo]:
    """Get the relevant information needed for the repository from its owner login and name."""
    owner, name = identifier["owner"], identifier["name"]

    logger.info(f"Getting info for {owner}/{name}")

    # create a logged in GitHub client if not provided
    if client is None:
        client = login(token=getenv("GH_ACCESS_TOKEN"))

    info: RepositoryInfo = {}

    # get the repository; if the repo is not found, log a warning
    try:
        repository = client.repository(owner, name)
        # Don't find issues inside archived repos.
        if repository.archived:
            return None

        # collect issues across labels and deduplicate by url
        issues_list = []
        seen_issue_urls = set()
        for label in ISSUE_LABELS:
            for issue in repository.issues(labels=label, state=ISSUE_STATE, sort=ISSUE_SORT, direction=ISSUE_SORT_DIRECTION):
                if len(issues_list) >= ISSUE_LIMIT:
                    break
                url = getattr(issue, 'html_url', None)
                if url and url not in seen_issue_urls:
                    seen_issue_urls.add(url)
                    issues_list.append(issue)

        good_first_issues = issues_list
        logger.info(f"\t found {len(good_first_issues)} good first issues")
        # check if repo has at least one good first issue
        if good_first_issues and repository.language:
            # store the repo info
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

            # get the latest issues with the tag
            issues = []
            for issue in good_first_issues:
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
        else:
            logger.info("\t skipping due to insufficient issues or info")
    except exceptions.NotFoundError:
        logger.warning(f"Not Found: {owner}/{name}")
    except exceptions.ForbiddenError:
        logger.warning(f"Skipped due to rate-limits: {owner}/{name}")
    except exceptions.ConnectionError:
        logger.warning(f"Skipped due to connection errors: {owner}/{name}")

    return info


def load_repositories_file(file_path: str) -> dict:
    with open(file_path, "r") as data_file:
        return toml.load(data_file)


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
    DATA = load_repositories_file(REPO_DATA_FILE)

    logger.info(f"Found {len(DATA.get('repositories', []))} repository entries in {REPO_DATA_FILE}")

    # pre-process the URLs and only continue with the list of valid GitHub URLs
    repositories = list(filter(bool, [parse_github_url(url) for url in DATA.get("repositories", [])]))

    # shuffle the order of the repositories
    random.shuffle(repositories)

    # create a shared GitHub client for all workers
    shared_client = login(token=getenv("GH_ACCESS_TOKEN"))

    with ThreadPoolExecutor(max_workers=MAX_CONCURRENCY) as executor:
        results = executor.map(partial(get_repository_info, client=shared_client), repositories[:MAX_REPOSITORIES])

    # filter out repositories with valid data and increment tag counts
    for result in results:
        if result:
            REPOSITORIES.append(result)
            lang = result.get("language")
            if lang:
                TAGS[lang] += 1

    # write to generated JSON files

    with open(REPO_GENERATED_DATA_FILE, "w") as file_desc:
        json.dump(REPOSITORIES, file_desc)
    logger.info(f"Wrote data for {len(REPOSITORIES)} repos to {REPO_GENERATED_DATA_FILE}")

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
    logger.info(f"Wrote {len(tags)} tags to {TAGS_GENERATED_DATA_FILE}")
