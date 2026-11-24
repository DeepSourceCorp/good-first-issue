#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import os
import unittest
from collections import Counter

import toml

from gfi.populate import parse_github_url

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


class TestParseGithubUrl(unittest.TestCase):
    """Tests for GitHub repository URL parsing."""

    def test_parse_url_without_protocol(self):
        result = parse_github_url("github.com/owner/repo")

        self.assertEqual(
            result,
            {"owner": "owner", "name": "repo"},
        )

    def test_parse_url_with_https(self):
        result = parse_github_url("https://github.com/owner/repo")

        self.assertEqual(
            result,
            {"owner": "owner", "name": "repo"},
        )

    def test_parse_url_with_http(self):
        result = parse_github_url("http://github.com/owner/repo")

        self.assertEqual(
            result,
            {"owner": "owner", "name": "repo"},
        )

    def test_reject_invalid_url(self):
        result = parse_github_url("texto-aleatorio")

        self.assertEqual(result, {})

    def test_reject_url_with_invalid_prefix(self):
        result = parse_github_url("prefixo-github.com/owner/repo")

        self.assertEqual(result, {})

    def test_reject_url_with_extra_path(self):
        result = parse_github_url("https://github.com/owner/repo/issues")

        self.assertEqual(result, {})

if __name__ == "__main__":
    unittest.main()
