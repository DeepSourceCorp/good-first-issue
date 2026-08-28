#!/usr/bin/env python
from datetime import datetime, timezone
from unittest import TestCase

from gfi.populate import get_good_first_issues, get_top_languages


class FakeRateLimiter:
    def __init__(self):
        self.calls = 0

    def acquire(self):
        self.calls += 1


class FakeIssue:
    def __init__(self, issue_id, pull_request=False):
        self.id = issue_id
        self.created_at = datetime.now(timezone.utc)
        self.pull_request_urls = {} if pull_request else None

    def __hash__(self):
        return hash(self.id)

    def __eq__(self, other):
        return isinstance(other, FakeIssue) and self.id == other.id


class FakeRepository:
    def __init__(self):
        self.issue = FakeIssue(1)
        self.pull_request = FakeIssue(2, pull_request=True)

    def issues(self, **kwargs):
        return [self.issue, self.pull_request]

    def languages(self):
        return [("Python", 300), ("Vue", 200), ("JavaScript", 100), ("Makefile", 10)]


class TestPopulateHelpers(TestCase):
    def test_good_first_issues_are_unique_and_exclude_pull_requests(self):
        limiter = FakeRateLimiter()

        issues = get_good_first_issues(FakeRepository(), limiter)

        self.assertEqual(issues, {FakeIssue(1)})
        self.assertGreater(limiter.calls, 0)

    def test_top_languages_returns_three_sorted_languages(self):
        limiter = FakeRateLimiter()

        languages = get_top_languages(FakeRepository(), limiter)

        self.assertEqual([language["name"] for language in languages], ["Python", "Vue", "JavaScript"])
        self.assertEqual([language["slug"] for language in languages], ["python", "vue", "javascript"])
        self.assertEqual(limiter.calls, 1)
