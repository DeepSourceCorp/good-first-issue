#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import os
import re
import unittest
from collections import Counter

import toml

DATA_FILE_PATH = "data/repositories.toml"
LABELS_FILE_PATH = "data/labels.json"


def _get_data_from_toml(file_path):
    with open(file_path, "r") as file_desc:
        return toml.load(file_desc)


def _get_data_from_json(file_path):
    with open(file_path, "r") as file_desc:
        return json.load(file_desc)


class TestDataSanity(unittest.TestCase):
    """Test for sanity of the data file."""

    @staticmethod
    def test_data_file_exists():
        """Verify that the data file exists."""
        assert os.path.exists(DATA_FILE_PATH)

    @staticmethod
    def test_labels_file_exists():
        """Verify that the labels file exists."""
        assert os.path.exists(LABELS_FILE_PATH)

    @staticmethod
    def test_data_file_sane():
        """Verify that the file is a valid TOML with required data."""
        data = _get_data_from_toml(DATA_FILE_PATH)
        assert "repositories" in data

    @staticmethod
    def test_labels_file_sane():
        """Verify that the labels file is a valid JSON"""
        data = _get_data_from_json(LABELS_FILE_PATH)
        assert "labels" in data

    @staticmethod
    def test_no_duplicates():
        """Verify that all entries are unique."""
        data = _get_data_from_toml(DATA_FILE_PATH)
        repos = data.get("repositories", [])
        print([item for item, count in Counter(repos).items() if count > 1])
        assert len(repos) == len(set(repos))


class TestGitHubUrlPattern(unittest.TestCase):
    """Test for the GitHub URL regex pattern used in populate.py."""

    PATTERN = re.compile(r"(?:https?://)?github\.com/(?P<owner>[\w.-]+)/(?P<name>[\w.-]+)/?")

    @staticmethod
    def _parse(url: str) -> dict:
        match = TestGitHubUrlPattern.PATTERN.search(url)
        return match.groupdict() if match else {}

    @staticmethod
    def test_standard_https_url():
        """Parse a standard https://github.com URL."""
        result = TestGitHubUrlPattern._parse("https://github.com/DeepSourceCorp/good-first-issue")
        assert result == {"owner": "DeepSourceCorp", "name": "good-first-issue"}, result

    @staticmethod
    def test_http_url():
        """Parse an http://github.com URL."""
        result = TestGitHubUrlPattern._parse("http://github.com/DeepSourceCorp/good-first-issue")
        assert result == {"owner": "DeepSourceCorp", "name": "good-first-issue"}, result

    @staticmethod
    def test_url_without_protocol():
        """Parse a github.com URL without protocol."""
        result = TestGitHubUrlPattern._parse("github.com/DeepSourceCorp/good-first-issue")
        assert result == {"owner": "DeepSourceCorp", "name": "good-first-issue"}, result

    @staticmethod
    def test_url_with_trailing_slash():
        """Parse a URL with a trailing slash."""
        result = TestGitHubUrlPattern._parse("https://github.com/nodejs/node/")
        assert result == {"owner": "nodejs", "name": "node"}, result

    @staticmethod
    def test_owner_with_dots():
        """Parse a URL where owner contains dots."""
        result = TestGitHubUrlPattern._parse("https://github.com/terraform-providers/terraform-provider-aws")
        assert result == {"owner": "terraform-providers", "name": "terraform-provider-aws"}, result

    @staticmethod
    def test_non_github_url():
        """Return empty dict for non-GitHub URLs."""
        result = TestGitHubUrlPattern._parse("https://gitlab.com/owner/repo")
        assert result == {}, result

    @staticmethod
    def test_invalid_url():
        """Return empty dict for completely unrelated strings."""
        result = TestGitHubUrlPattern._parse("this is not a url")
        assert result == {}, result


if __name__ == "__main__":
    unittest.main()
