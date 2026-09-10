#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import os
import unittest
from collections import Counter
from datetime import datetime, timezone
from unittest.mock import MagicMock

import toml

from gfi.populate import get_repository_info



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

class TestPopulate(unittest.TestCase):
    """Test repository data population."""

    def test_get_repository_info_languages(self):
        """Verify that the top 3 repository languages are stored."""
        mock_repo = MagicMock()
        mock_repo.language = "Python"
        mock_repo.description = "A test repository"

        # Intentionally not sorted to verify that the code sorts by usage.
        mock_repo.languages.return_value = [
            ("JavaScript", 300),
            ("Python", 1000),
            ("HTML", 100),
            ("TypeScript", 500),
        ]

        info = get_repository_info(
            mock_repo,
            "test-owner",
            "test-repo",
        )

        self.assertEqual(
            info["languages"],
            ["Python", "TypeScript", "JavaScript"],
        )
        self.assertEqual(
            info["slugs"],
            ["python", "typescript", "javascript"],
        )



class TestPopulate(unittest.TestCase):
    """Test repository data population."""

    def test_get_repository_info_languages(self):
        """Verify that the top 3 repository languages are stored."""
        identifier = {
            "owner": "test-owner",
            "name": "test-repo",
        }

        mock_client = MagicMock()
        mock_rate_limiter = MagicMock()
        mock_repo = MagicMock()

        mock_repo.archived = False
        mock_repo.pushed_at = datetime.now(timezone.utc)
        mock_repo.language = "Python"
        mock_repo.description = "A test repository"
        mock_repo.html_url = "https://github.com/test-owner/test-repo"
        mock_repo.stargazers_count = 100
        mock_repo.id = 12345

        # Return no issues so the repository passes the issue check.
        mock_repo.issues.return_value = [MagicMock()]


        # Intentionally unsorted to verify sorting by usage.
        mock_repo.languages.return_value = [
            ("JavaScript", 300),
            ("Python", 1000),
            ("HTML", 100),
            ("TypeScript", 500),
        ]

        mock_client.repository.return_value = mock_repo

        info = get_repository_info(
            identifier,
            mock_client,
            mock_rate_limiter,
        )

        self.assertEqual(
            info["languages"],
            ["Python", "TypeScript", "JavaScript"],
        )
        self.assertEqual(
            info["slugs"],
            ["python", "typescript", "javascript"],
        )

if __name__ == "__main__":
    unittest.main()
