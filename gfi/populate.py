#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import logging.config
import os
import random
import re
from collections import Counter
from operator import itemgetter
from os import getenv, path

import toml

from config import LOGGING_CONFIG
from github3 import exceptions, login
from numerize import numerize

REPO_DATA_FILE = "data/repositories.toml"
REPO_GENERATED_DATA_FILE = "data/generated.json"
TAGS_GENERATED_DATA_FILE = "data/tags.json"
GH_URL_PATTERN = re.compile(
    r"[http://|https://]?github.com/(?P<owner>[\w\.-]+)/(?P<name>[\w\.-]+)/?"
)
ISSUE_LABELS = ["good first issue"]
ISSUE_STATE = "open"
ISSUE_SORT = "created"
ISSUE_SORT_DIRECTION = "desc"
ISSUE_LIMIT = 10

logging.config.dictConfig(LOGGING_CONFIG)
LOGGER = logging.getLogger(__name__)


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

    access_token = getenv('GITHUB_ACCESS_TOKEN')
    if not access_token:
        raise AssertionError('Access token not present in the env variable `GITHUB_ACCESS_TOKEN`')

    # create a logged in GitHub client
    client = login(token=access_token)

    info = {}

    # get the repository; if the repo is not found, raise an error
    try:
        repository = client.repository(owner, name)

        good_first_issues = list(repository.issues(
                labels=ISSUE_LABELS,
                state=ISSUE_STATE,
                number=ISSUE_LIMIT,
                sort=ISSUE_SORT,
                direction=ISSUE_SORT_DIRECTION,
        ))
        LOGGER.info('\t found %d good first issues', len(good_first_issues))
        # check if repo has at least one good first issue
        if good_first_issues:
            # store the repo info
            info["name"] = name
            info["owner"] = owner
            info["language"] = repository.language
            info["url"] = repository.html_url
            info["stars"] = repository.stargazers_count
            info["stars_display"] = numerize.numerize(repository.stargazers_count)
            info["last_modified"] = repository.last_modified
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
                        "created_at": issue.created_at.isoformat()
                    }
                )

            info["issues"] = issues
            return info
        LOGGER.info('\t skipping the repo')
        return None
    except exceptions.NotFoundError:
        raise RepoNotFoundException()


if __name__ == "__main__":

    # parse the repositories data file and get the list of repos
    # for generating pages for.

    if not path.exists(REPO_DATA_FILE):
        raise RuntimeError("No config data file found. Exiting.")

    REPOSITORIES = []
    TAGS = Counter()
    with open(REPO_DATA_FILE, "r") as data_file:
        DATA = toml.load(REPO_DATA_FILE)

        LOGGER.info("Found %d repository entries in %s", len(DATA["repositories"]), REPO_DATA_FILE)

        for repository_url in DATA["repositories"]:
            repo_dict = parse_github_url(repository_url)
            if repo_dict:
                repo_details = get_repository_info(repo_dict["owner"], repo_dict["name"])
                if repo_details:
                    REPOSITORIES.append(repo_details)
                    TAGS[repo_details['language']] += 1

    # shuffle the repository order
    random.shuffle(REPOSITORIES)

    # write to generated JSON files

    with open(REPO_GENERATED_DATA_FILE, 'w') as file_desc:
        json.dump(REPOSITORIES, file_desc)
    LOGGER.info("Wrote data for %d repos to %s", len(REPOSITORIES), REPO_GENERATED_DATA_FILE)

    tags = [{"language": key, "count": value} for (key, value) in TAGS.items()]
    tags_sorted = sorted(tags, key=itemgetter('count'), reverse=True)
    with open(TAGS_GENERATED_DATA_FILE, 'w') as file_desc:
        json.dump(tags_sorted, file_desc)
    LOGGER.info("Wrote %d tags to %s", len(tags), TAGS_GENERATED_DATA_FILE)

    # populate tag files for hugo
    for tag in tags_sorted:
        tag_name = tag['language']
        os.system(f'hugo new language/{tag_name}.md')
