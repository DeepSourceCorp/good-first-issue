#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Starting from the most recent addition in `data/repositories.toml`, if
the repo has not been tweeted about in the past `GoodFirstTwitter.TWEET_AGAIN`
(90) days, tweet it. In a single session, only `GoodFirstTwitter.TWEET_LIMIT`
(5) tweets are allowed.

https://jsonbin.io/ is used for storing a persistent record of all tweets.
"""

from datetime import datetime, timedelta
import logging
import os
import sys

from config import LOGGING_CONFIG
from populate import get_repository_info, parse_github_url, REPO_DATA_FILE

import requests
import toml
from twython import Twython
from superjson import json

logging.config.dictConfig(LOGGING_CONFIG)
LOGGER = logging.getLogger("tweet.py")


def get_json_bin(json_bin_id, json_bin_key):
    """Downloads JSON stored at `json_bin_id`"""
    url = f"https://api.jsonbin.io/b/{json_bin_id}/latest/"
    headers = {"secret-key": json_bin_key}
    resp = requests.get(url, headers=headers)
    if resp.status_code != 200:
        LOGGER.WARNING("Failed to fetch old tweets. Aborting!")
        sys.exit()
    LOGGER.info("<%s>: Successfully fetched JSONBIN: %s", resp.status_code, resp.text)
    return json.loads(resp.text)


def update_json_bin(new, json_bin_id, json_bin_key):
    """Updates JSON storeed at `json_bin_id`"""
    url = f"https://api.jsonbin.io/b/{json_bin_id}"
    headers = {"secret-key": json_bin_key, "Content-Type": "application/json"}
    resp = requests.put(url, headers=headers, data=json.dumps(new))
    if resp.status_code != 200:
        LOGGER.warning(
            "Failed to update tweet DB. <%s>: %s", resp.status_code, resp.text
        )
    LOGGER.info("Successfully updated JSONBIN: %s", resp.text)


class GoodFirstTwitter:
    def __init__(self):
        self.twitter = Twython(APP_KEY, APP_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
        self.tweeted_already = get_json_bin(JSON_BIN_ID, JSON_BIN_KEY)
        self.tweeted_repos = {}
        self.tweet_count = 0
        self.TWEET_LIMIT = 1
        self.TWEET_AGAIN = 90  # Days

    def tweeted_recently(self, name):
        last_tweeted = self.tweeted_already[name]["last_tweeted"]
        return datetime.now() - last_tweeted < timedelta(days=self.TWEET_AGAIN)

    def should_tweet(self, name):
        return name not in self.tweeted_already or not self.tweeted_recently(name)

    def tweet(self, repo):
        try:
            status = (
                f"{ repo['name'] } needs your help. Start contributing to"
                f" issues marked #goodfirstissues {repo['url']} #oss"
                f" #{repo['language']}"
            )
            self.twitter.update_status(status=status)
        except:  # noqa: PYL-W0703
            LOGGER.exception("<%s>: Couldn't tweet status", repo["name"])
            return

        self.tweeted_repos[repo["name"]] = {
            "last_tweeted": datetime.now(),
            "description": repo["description"],
            "language": repo["language"],
            "url": repo["url"],
        }
        self.tweet_count += 1
        LOGGER.info("[%s] Tweeted successfully: %s", self.tweet_count, status)

    def update_tweeted_list(self):
        all_tweeted_repos = {**self.tweeted_already, **self.tweeted_repos}
        update_json_bin(all_tweeted_repos, JSON_BIN_ID, JSON_BIN_KEY)

    def spread_the_word(self, repo_urls):
        for url in repo_urls:
            parsed = parse_github_url(url)
            owner, name = parsed["owner"], parsed["name"]
            if self.should_tweet(name):
                repo = get_repository_info(owner, name)
                if repo:
                    self.tweet(repo)
            if self.tweet_count > self.TWEET_LIMIT:
                return


def main():
    with open(REPO_DATA_FILE, "r") as fd:
        repos = toml.load(fd)["repositories"]
    repos.reverse()  # Start with the latest additions

    client = GoodFirstTwitter()
    client.spread_the_word(repos)
    client.update_tweeted_list()


if __name__ == "__main__":
    APP_KEY = os.getenv("TWITTER_APP_KEY")
    APP_SECRET = os.getenv("TWITTER_APP_SECRET")
    ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
    ACCESS_TOKEN_SECRET = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

    if not (APP_KEY and APP_SECRET and ACCESS_TOKEN and ACCESS_TOKEN_SECRET):
        # Keys are only in production build. Don't tweet in preview/dev.
        LOGGER.warning("Twitter keys not found. Aborting!")
        sys.exit()

    JSON_BIN_ID = os.getenv("JSON_BIN_ID")
    JSON_BIN_KEY = os.getenv("JSON_BIN_KEY")
    if not (JSON_BIN_ID and JSON_BIN_KEY):
        LOGGER.warning("JSON_BIN keys not found. Aborting!")
        sys.exit()

    main()
