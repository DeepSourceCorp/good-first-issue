#!/usr/bin/env python
# -*- coding: utf-8 -*-
import itertools
import json
import random
import re
import time
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from operator import itemgetter
from os import getenv, path
from typing import TypedDict, Dict, Union, Sequence, Optional, Mapping

import toml

from github3 import exceptions, login
from numerize import numerize
from emoji import emojize
from slugify import slugify
from loguru import logger

MAX_CONCURRENCY = 10  # max number of requests to make to GitHub in parallel (reduced to avoid rate limits)
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


RepositoryInfo = Dict["str", Union[str, int, Sequence]]


def get_repository_info(identifier: RepositoryIdentifier) -> Optional[RepositoryInfo]:
    """Get the relevant information needed for the repository from its owner login and name."""
    owner, name = identifier["owner"], identifier["name"]

    logger.info("Getting info for {}/{}", owner, name)

    # create a logged in GitHub client
    client = login(token=getenv("GH_ACCESS_TOKEN"))

    max_retries = 3

    for attempt in range(max_retries):
        try:
            repository = client.repository(owner, name)
            # Don't find issues inside archived repos.
            if repository.archived:
                return None

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
                return info
            else:
                logger.info("\t skipping due to insufficient issues or info")
                return None

        except exceptions.ForbiddenError:
            if attempt < max_retries - 1:
                wait_time = 60 * (attempt + 1)  # 60s, 120s, 180s
                logger.warning("Rate limited on {}/{}. Waiting {}s before retry...",
                             owner, name, wait_time)
                time.sleep(wait_time)
            else:
                logger.error("Rate limit exceeded after {} retries: {}/{}",
                           max_retries, owner, name)
                return None

        except exceptions.NotFoundError:
            logger.warning("Not Found: {}/{}", owner, name)
            return None

        except exceptions.ConnectionError:
            logger.warning("Connection error: {}/{}", owner, name)
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

        with ThreadPoolExecutor(max_workers=MAX_CONCURRENCY) as executor:
            results = executor.map(get_repository_info, repositories)

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
