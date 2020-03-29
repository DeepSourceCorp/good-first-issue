#!/usr/bin/env python
# -*- coding: utf-8 -*-

from string import Template
from twython import Twython, TwythonError
from twitter_exception import TweetException
from urllib.parse import quote
from config import LOGGING_CONFIG
import logging.config

logging.config.dictConfig(LOGGING_CONFIG)
LOGGER = logging.getLogger(__name__)

GOOD_FIRST_ISSUE = "good first issue"
ISSUES_HTML_URL = Template("$html_url/labels/$good_first_issue")
TWEET_TEMPLATE = Template(
    "$repo_full_name - $repo_desc.\n\nLanguage: $language\nIssues: $issues_url"
)


class TwitterClient:

    twitter_client = None
    repo_url = None

    def __init__(self, APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET):
        self.twitter_client = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

    def get_repo_url(self, repo_dictionary):
        """ Returns the labelled URL for good first issues """
        self.repo_url = ISSUES_HTML_URL.substitute(
                            html_url=repo_dictionary["url"],
                            good_first_issue=quote(GOOD_FIRST_ISSUE)
                        )
        return self.repo_url

    def tweet_repo(self, repo_dictionary):
        """
        Twitter module
        Raises an exception otherwise
        """

        tweet_string = TWEET_TEMPLATE.substitute(
            repo_full_name=repo_dictionary["repo_full_name"],
            repo_desc=repo_dictionary["repo_description"],
            language=repo_dictionary["language"],
            issues_url=self.repo_url
        )
        try:
            self.twitter_client.update_status(status=tweet_string)
        except TwythonError as e:
            raise twitter_exception.TweetException("%s - %s" % (repo_dictionary["repo_full_name"], e.msg))
