#!/usr/bin/env python
# -*- coding: utf-8 -*-
import itertools
import json
import logging.config
import random
import re
from collections import Counter
from operator import itemgetter
from os import getenv, path

import toml

from config import LOGGING_CONFIG
from github3 import exceptions, login
from numerize import numerize
from emoji import emojize
from slugify import slugify

REPO_DATA_FILE = "data/repositories.toml"
REPO_GENERATED_DATA_FILE = "data/generated.json"
TAGS_GENERATED_DATA_FILE = "data/tags.json"
GH_URL_PATTERN = re.compile(
    r"[http://|https://]?github.com/(?P<owner>[\w\.-]+)/(?P<name>[\w\.-]+)/?"
)
LABELS_DATA_FILE = "data/labels.json"
ISSUE_STATE = "open"
ISSUE_SORT = "created"
ISSUE_SORT_DIRECTION = "desc"
ISSUE_LIMIT = 10
SLUGIFY_REPLACEMENTS = [["#", "sharp"], ["+", "plus"]]

logging.config.dictConfig(LOGGING_CONFIG)
LOGGER = logging.getLogger(__file__)

if not path.exists(LABELS_DATA_FILE):
    raise RuntimeError("No labels data file found. Exiting.")

with open(LABELS_DATA_FILE) as labels_file:
    LABELS_DATA = json.load(labels_file)

    ISSUE_LABELS = LABELS_DATA["labels"]


class RepoNotFoundException(Exception):
    """Exception class for repo not found."""


def parse_github_url(url):
    """
    Take the GitHub repo URL and return a tuple with
    owner login and repo name.
    """
    match = GH_URL_PATTERN.search(url)
    if match:
        return match.groupdict()
    return {}


def get_repository_info(owner, name):
    """
    Get the relevant information needed for the repository from
    its owner login and name.
    """

    LOGGER.info("Getting info for %s/%s", owner, name)

    access_token = getenv("GITHUB_ACCESS_TOKEN")
    if not access_token:
        raise AssertionError(
            "Access token not present in the env variable `GITHUB_ACCESS_TOKEN`"
        )

    # create a logged in GitHub client
    client = login(token=access_token)

    info = {}

    # get the repository; if the repo is not found, log a warning
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
        LOGGER.info("\t found %d good first issues", len(good_first_issues))
        # check if repo has at least one good first issue
        if good_first_issues and repository.language:
            # store the repo info
            info["name"] = name
            info["owner"] = owner
            info["description"] = emojize(repository.description or "")
            info["language"] = repository.language
            info["slug"] = slugify(
                repository.language, replacements=SLUGIFY_REPLACEMENTS
            )
            info["url"] = repository.html_url
            info["stars"] = repository.stargazers_count
            info["stars_display"] = numerize.numerize(repository.stargazers_count)
            info["last_modified"] = repository.pushed_at.isoformat()
            info["id"] = str(repository.id)
            info["objectID"] = str(repository.id)  # for indexing on algolia

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
        LOGGER.info("\t skipping the repo")
        return None
    except exceptions.NotFoundError:
        LOGGER.warning("Not Found: %s", f"{owner}/{name}")


if __name__ == "__main__":

    # parse the repositories data file and get the list of repos
    # for generating pages for.

    if not path.exists(REPO_DATA_FILE):
        raise RuntimeError("No config data file found. Exiting.")

    REPOSITORIES = []
    TAGS = Counter()
    with open(REPO_DATA_FILE, "r") as data_file:
        DATA = toml.load(REPO_DATA_FILE)

        LOGGER.info(
            "Found %d repository entries in %s",
            len(DATA["repositories"]),
            REPO_DATA_FILE,
        )

        for repository_url in DATA["repositories"]:
            repo_dict = parse_github_url(repository_url)
            if repo_dict:
                repo_details = get_repository_info(
                    repo_dict["owner"], repo_dict["name"]
                )
                if repo_details:
                    REPOSITORIES.append(repo_details)
                    TAGS[repo_details["language"]] += 1

    # shuffle the repository order
    random.shuffle(REPOSITORIES)

    # write to generated JSON files

    with open(REPO_GENERATED_DATA_FILE, "w") as file_desc:
        json.dump(REPOSITORIES, file_desc)
    LOGGER.info(
        "Wrote data for %d repos to %s", len(REPOSITORIES), REPO_GENERATED_DATA_FILE
    )

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
    LOGGER.info("Wrote %d tags to %s", len(tags), TAGS_GENERATED_DATA_FILE)
