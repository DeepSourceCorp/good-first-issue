#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Unit tests for validating the integrity and structure of data files.

This module contains tests that verify:
- The existence of required data files (repositories.toml, labels.json)
- The validity of their contents (valid TOML, valid JSON)
- The uniqueness of repository entries (no duplicate URLs)
"""

import json
import os
import unittest
from collections import Counter
from typing import Any

import toml

DATA_FILE_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "data",
    "repositories.toml",
)
LABELS_FILE_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "data",
    "labels.json",
)


def _load_file(file_path: str) -> Any:
    """Load and parse a data file based on its extension.

    Supports TOML (.toml) and JSON (.json) file formats. Uses absolute
    paths derived from the project root to ensure tests can be run from
    any working directory.

    Args:
        file_path: Absolute path to the data file.

    Returns:
        Parsed contents of the file as a Python dict.

    Raises:
        FileNotFoundError: If the file does not exist at the given path.
        ValueError: If the file extension is not .toml or .json.
        toml.TomlDecodeError: If the TOML file contains invalid syntax.
        json.JSONDecodeError: If the JSON file contains invalid syntax.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Data file not found: {file_path}")

    ext = os.path.splitext(file_path)[1].lower()
    valid_extensions = {".toml", ".json"}

    if ext not in valid_extensions:
        raise ValueError(
            f"Unsupported file extension '{ext}'. "
            f"Expected one of: {', '.join(sorted(valid_extensions))}"
        )

    with open(file_path, "r", encoding="utf-8") as file_desc:
        if ext == ".toml":
            return toml.load(file_desc)
        return json.load(file_desc)


class TestDataSanity(unittest.TestCase):
    """Tests for validating the integrity and structure of data files."""

    def test_data_file_exists(self):
        """Verify that the repositories data file exists."""
        self.assertTrue(
            os.path.exists(DATA_FILE_PATH),
            f"Data file not found: {DATA_FILE_PATH}",
        )

    def test_labels_file_exists(self):
        """Verify that the labels file exists."""
        self.assertTrue(
            os.path.exists(LABELS_FILE_PATH),
            f"Labels file not found: {LABELS_FILE_PATH}",
        )

    def test_data_file_is_valid_toml(self):
        """Verify that the data file is a valid TOML document.

        Catches TOML parsing errors with a descriptive failure message.
        """
        try:
            data = _load_file(DATA_FILE_PATH)
        except FileNotFoundError:
            self.fail(
                f"Data file not found: {DATA_FILE_PATH}. "
                f"Ensure the file exists before running tests."
            )
        except toml.TomlDecodeError as exc:
            self.fail(
                f"Data file contains invalid TOML: {DATA_FILE_PATH}. "
                f"Error: {exc}"
            )
        else:
            self.assertIn(
                "repositories",
                data,
                f"'repositories' key not found in {DATA_FILE_PATH}",
            )

    def test_labels_file_is_valid_json(self):
        """Verify that the labels file is a valid JSON document.

        Catches JSON parsing errors with a descriptive failure message.
        """
        try:
            data = _load_file(LABELS_FILE_PATH)
        except FileNotFoundError:
            self.fail(
                f"Labels file not found: {LABELS_FILE_PATH}. "
                f"Ensure the file exists before running tests."
            )
        except json.JSONDecodeError as exc:
            self.fail(
                f"Labels file contains invalid JSON: {LABELS_FILE_PATH}. "
                f"Error: {exc}"
            )
        else:
            self.assertIn(
                "labels",
                data,
                f"'labels' key not found in {LABELS_FILE_PATH}",
            )

    def test_no_duplicate_repositories(self):
        """Verify that all repository entries are unique.

        If duplicates are found, they are listed in the failure message
        to aid debugging.
        """
        try:
            data = _load_file(DATA_FILE_PATH)
        except FileNotFoundError:
            self.fail(
                f"Data file not found: {DATA_FILE_PATH}. "
                f"Ensure the file exists before running tests."
            )
            return
        except toml.TomlDecodeError as exc:
            self.fail(
                f"Data file contains invalid TOML: {DATA_FILE_PATH}. "
                f"Error: {exc}"
            )
            return

        repos = data.get("repositories", [])
        duplicates = [
            item for item, count in Counter(repos).items() if count > 1
        ]
        self.assertEqual(
            len(repos),
            len(set(repos)),
            f"Found {len(duplicates)} duplicate repository entries: {duplicates}",
        )


if __name__ == "__main__":
    unittest.main()
