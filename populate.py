#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
import json
from os import path
import re
from urllib.parse import urlparse

from github3 import GitHub, exceptions
import toml

REPO_DATA_FILE = "data/repositories.toml"
REPO_GENERATED_DATA_FILE = "data/generated.json"
GH_URL_PATTERN = re.compile(
    r"[http://|https://]?github.com/(?P<owner>[\w\.-]+)/(?P<name>[\w\.-]+)/?"
)
ISSUE_LABELS = ["good first issue"]
ISSUE_STATE = "open"
ISSUE_SORT = "created"
ISSUE_SORT_DIRECTION = "desc"
ISSUE_LIMIT = 10
LOGGER = logging.getLogger(__name__)


class RepoNotFoundException(Exception):
    """Exception class for repo not found."""

    pass


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

    # create an anonymous GitHub client
    client = GitHub()

    info = {}

    # get the repository; if the repo is not found, raise an error
    try:
        repository = client.repository(owner, name)

        # store the repo info
        info["name"] = name
        info["owner"] = owner
        info["language"] = repository.language
        info["url"] = repository.html_url
        info["stars"] = repository.stargazers_count
        info["last_modified"] = repository.last_modified
        info["id"] = str(repository.id)

        # get the latest issues with the tag
        issues = []
        for issue in repository.issues(
            labels=ISSUE_LABELS,
            state=ISSUE_STATE,
            number=ISSUE_LIMIT,
            sort=ISSUE_SORT,
            direction=ISSUE_SORT_DIRECTION,
        ):
            issues.append(
                {
                    "title": issue.title,
                    "url": issue.html_url,
                    "number": issue.number,
                    "body": issue.body,
                    "created_at": issue.created_at.isoformat()
                }
            )

        info["issues"] = issues
        return info
    except exceptions.NotFoundError:
        raise RepoNotFoundException()


if __name__ == "__main__":

    # parse the repositories data file and get the list of repos
    # for generating pages for.

    if not path.exists(REPO_DATA_FILE):
        raise RuntimeError("No config data file found. Exiting.")

    repositories = []
    with open(name := REPO_DATA_FILE, "r") as data_file:
        data = toml.load(name)
        for repository_url in data["repositories"]:
            if repo_dict := parse_github_url(repository_url):
                repositories.append(
                    get_repository_info(repo_dict["owner"], repo_dict["name"])
                )

    # write to generated JSON file
    with open(REPO_GENERATED_DATA_FILE, 'w') as file_desc:
        json.dump(repositories, file_desc)