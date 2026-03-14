#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import os
import unittest
from collections import Counter

import toml

DATA_FILE_PATH = "data/repositories.toml"
LABELS_FILE_PATH = "data/labels.json"
GENERATED_FILE_PATH = "data/generated.json"


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

    @staticmethod
    def test_issues_count_field():
        """Verify that each repo in generated.json has a valid issues_count field."""
        if not os.path.exists(GENERATED_FILE_PATH):
            return
        data = _get_data_from_json(GENERATED_FILE_PATH)
        for repo in data:
            assert "issues_count" in repo, f"Missing issues_count in {repo.get('name')}"
            assert isinstance(repo["issues_count"], int), f"issues_count is not int in {repo.get('name')}"
            assert repo["issues_count"] >= len(repo["issues"]), (
                f"issues_count < len(issues) in {repo.get('name')}"
            )


if __name__ == "__main__":
    unittest.main()
