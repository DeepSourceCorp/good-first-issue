#!/usr/bin/env python
# -*- coding: utf-8 -*-

from twython import TwythonError


class TweetException(TwythonError):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return 'TweetException, {0} '.format(self.message)
        return 'TweetException has been raised'
