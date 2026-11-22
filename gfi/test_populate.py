#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Offline unit tests for gfi.populate.parse_github_url().

These tests only exercise URL parsing; they never touch the GitHub API.
Run them from the repository root:

    uv run python gfi/test_populate.py
"""

import os
import sys
import unittest

import toml

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from gfi.populate import parse_github_url  # noqa: E402

DATA_FILE_PATH = "data/repositories.toml"


class TestParseGitHubUrl(unittest.TestCase):
    """Test the GitHub repository URL parser."""

    @staticmethod
    def test_path_without_scheme():
        """Parse the scheme-less form used by data/repositories.toml."""
        assert parse_github_url("github.com/DeepSourceCorp/good-first-issue") == {
            "owner": "DeepSourceCorp",
            "name": "good-first-issue",
        }

    @staticmethod
    def test_https_url():
        """Parse a regular https://github.com URL."""
        assert parse_github_url("https://github.com/DeepSourceCorp/good-first-issue") == {
            "owner": "DeepSourceCorp",
            "name": "good-first-issue",
        }

    @staticmethod
    def test_http_url():
        """Parse a regular http://github.com URL."""
        assert parse_github_url("http://github.com/DeepSourceCorp/good-first-issue") == {
            "owner": "DeepSourceCorp",
            "name": "good-first-issue",
        }

    @staticmethod
    def test_trailing_slash():
        """Ignore a trailing slash."""
        assert parse_github_url("https://github.com/DeepSourceCorp/good-first-issue/") == {
            "owner": "DeepSourceCorp",
            "name": "good-first-issue",
        }

    @staticmethod
    def test_host_is_case_insensitive():
        """Accept the host regardless of its case, like browsers do."""
        assert parse_github_url("HTTPS://GitHub.com/DeepSourceCorp/good-first-issue") == {
            "owner": "DeepSourceCorp",
            "name": "good-first-issue",
        }

    @staticmethod
    def test_www_host():
        """Accept the www subdomain of github.com."""
        assert parse_github_url("https://www.github.com/DeepSourceCorp/good-first-issue") == {
            "owner": "DeepSourceCorp",
            "name": "good-first-issue",
        }

    @staticmethod
    def test_surrounding_whitespace():
        """Ignore whitespace around the URL."""
        assert parse_github_url("  github.com/DeepSourceCorp/good-first-issue\n") == {
            "owner": "DeepSourceCorp",
            "name": "good-first-issue",
        }

    @staticmethod
    def test_extra_path_segments():
        """Accept deep links into a repository and keep owner/name only."""
        assert parse_github_url("https://github.com/nodejs/node/issues/42") == {
            "owner": "nodejs",
            "name": "node",
        }
        assert parse_github_url("github.com/nodejs/node/tree/main/lib") == {
            "owner": "nodejs",
            "name": "node",
        }

    @staticmethod
    def test_dot_git_suffix():
        """Accept clone URLs and drop the .git suffix."""
        assert parse_github_url("https://github.com/nodejs/node.git") == {
            "owner": "nodejs",
            "name": "node",
        }

    @staticmethod
    def test_names_with_dots_and_underscores():
        """Keep repository names that contain dots or underscores intact."""
        assert parse_github_url("github.com/reactjs/reactjs.org") == {
            "owner": "reactjs",
            "name": "reactjs.org",
        }
        assert parse_github_url("github.com/dotfiles/dotfiles.github.com") == {
            "owner": "dotfiles",
            "name": "dotfiles.github.com",
        }
        assert parse_github_url("github.com/qmk/qmk_firmware") == {
            "owner": "qmk",
            "name": "qmk_firmware",
        }

    @staticmethod
    def test_lookalike_hosts_rejected():
        """Reject hosts that only contain github.com as a substring."""
        for url in (
            "https://evilgithub.com/acme/widget",
            "https://notgithub.com/acme/widget",
            "https://github.com.evil.io/acme/widget",
            "https://evil.io/github.com/acme/widget",
            "https://githubXcom/acme/widget",
            "https://github.co/acme/widget",
            "https://gist.github.com/acme/widget",
        ):
            assert parse_github_url(url) == {}, url

    @staticmethod
    def test_host_embedded_in_path_rejected():
        """Reject github.com when it only appears in the path of another host."""
        for url in (
            "https://example.com/github.com/acme/widget",
            "https://example.com/redirect?to=github.com/acme/widget",
            "github.com.example.com/acme/widget",
        ):
            assert parse_github_url(url) == {}, url

    @staticmethod
    def test_missing_repository_rejected():
        """Reject URLs that do not contain both an owner and a repository."""
        for url in (
            "github.com",
            "github.com/acme",
            "github.com/acme/",
            "https://github.com/",
            "https://github.com/acme?tab=repositories",
        ):
            assert parse_github_url(url) == {}, url

    @staticmethod
    def test_unsupported_scheme_rejected():
        """Reject non-HTTP schemes, e.g. ssh or a Windows file path."""
        for url in (
            "ftp://github.com/acme/widget",
            "ssh://git@github.com/acme/widget",
            "file://github.com/acme/widget",
        ):
            assert parse_github_url(url) == {}, url

    @staticmethod
    def test_empty_input_rejected():
        """Reject empty and blank input."""
        for url in ("", "   ", "\n\t"):
            assert parse_github_url(url) == {}, repr(url)

    @staticmethod
    def test_non_string_input_rejected():
        """Reject non-string input instead of raising."""
        values = [None, 123, b"github.com/acme/widget", ["github.com/acme/widget"]]
        for value in values:
            assert parse_github_url(value) == {}, repr(value)

    @staticmethod
    def test_dot_segments_rejected():
        """Reject path traversal segments."""
        for url in (
            "https://github.com/../acme",
            "https://github.com/acme/..",
            "https://github.com/./acme",
        ):
            assert parse_github_url(url) == {}, url

    @staticmethod
    def test_existing_repositories_file_is_parsed_completely():
        """Every entry of data/repositories.toml must still parse to owner/name."""
        with open(DATA_FILE_PATH, "r") as file_desc:
            repositories = toml.load(file_desc)["repositories"]

        assert repositories, "data/repositories.toml is empty"

        for url in repositories:
            parsed = parse_github_url(url)
            assert set(parsed) == {"owner", "name"}, url
            assert parsed["owner"] and parsed["name"], url
            # a scheme-less entry must round-trip to the same owner/name path
            assert f"{parsed['owner']}/{parsed['name']}" == url.split("github.com/", 1)[-1].rstrip("/"), url


if __name__ == "__main__":
    unittest.main()
