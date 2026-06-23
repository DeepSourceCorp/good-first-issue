#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import os
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


class TestPopulateIssues(unittest.TestCase):
    def test_get_repository_info_filters_prs(self):
        from unittest.mock import MagicMock
        from datetime import datetime, timezone
        from gfi.populate import get_repository_info, GitHubRateLimiter

        # Mock repository object
        mock_repo = MagicMock()
        mock_repo.archived = False
        mock_repo.pushed_at = datetime.now(timezone.utc)
        mock_repo.language = "Python"
        mock_repo.description = "Test repo"
        mock_repo.html_url = "https://github.com/owner/name"
        mock_repo.stargazers_count = 100
        mock_repo.id = 12345
        
        # Mock issues returned: 1 real issue, 1 PR
        mock_issue = MagicMock()
        mock_issue.title = "Good first issue"
        mock_issue.html_url = "https://github.com/owner/name/issues/1"
        mock_issue.number = 1
        mock_issue.comments_count = 0
        mock_issue.created_at = datetime.now(timezone.utc)
        mock_issue.pull_request_urls = None  # Not a PR
        
        mock_pr = MagicMock()
        mock_pr.title = "PR contribution"
        mock_pr.html_url = "https://github.com/owner/name/pull/2"
        mock_pr.number = 2
        mock_pr.comments_count = 0
        mock_pr.created_at = datetime.now(timezone.utc)
        mock_pr.pull_request_urls = {"url": "https://api.github.com/repos/owner/name/pulls/2"}  # Is a PR
        
        mock_repo.issues.return_value = [mock_issue, mock_pr]
        
        # Mock client
        mock_client = MagicMock()
        mock_client.repository.return_value = mock_repo
        mock_client.rate_limit.return_value = {
            'resources': {
                'core': {
                    'remaining': 1000,
                    'limit': 5000,
                    'reset': 0
                }
            }
        }
        
        rate_limiter = GitHubRateLimiter(mock_client, requests_per_second=100.0)
        
        info = get_repository_info(
            {"owner": "owner", "name": "name"},
            mock_client,
            rate_limiter
        )
        
        # Verify that only the real issue was kept (the PR was filtered out)
        self.assertIsNotNone(info)
        assert info is not None
        self.assertEqual(len(info["issues"]), 1)
        self.assertEqual(info["issues"][0]["number"], 1)


if __name__ == "__main__":
    unittest.main()
