#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Data file validation tests for repository and labels data."""

import json
import os
import unittest
from collections import Counter
from typing import Any, Dict

import toml

DATA_FILE_PATH = "data/repositories.toml"
LABELS_FILE_PATH = "data/labels.json"


def _load_data_file(file_path: str, file_format: str = "auto") -> Dict[str, Any]:
    """
    Load data from a file (TOML or JSON format).

    Args:
        file_path: Path to the data file to load.
        file_format: File format type - "auto", "toml", or "json".
                    If "auto", determines format from file extension.

    Returns:
        Parsed data as a dictionary.

    Raises:
        FileNotFoundError: If the file does not exist.
        ValueError: If file format is unsupported.
        toml.TomlDecodeError: If TOML file is invalid.
        json.JSONDecodeError: If JSON file is invalid.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Data file not found: {file_path}")

    # Determine file format if not explicitly specified
    if file_format == "auto":
        if file_path.endswith(".toml"):
            file_format = "toml"
        elif file_path.endswith(".json"):
            file_format = "json"
        else:
            raise ValueError(
                f"Unable to determine file format for {file_path}. "
                "Specify format explicitly or use .toml/.json extension."
            )

    try:
        with open(file_path, "r", encoding="utf-8") as file_desc:
            if file_format == "toml":
                return toml.load(file_desc)
            elif file_format == "json":
                return json.load(file_desc)
            else:
                raise ValueError(f"Unsupported file format: {file_format}")
    except (IOError, OSError) as e:
        raise IOError(f"Error reading file {file_path}: {e}") from e


class TestDataSanity(unittest.TestCase):
    """Comprehensive tests for data file integrity and validity."""

    def test_data_file_exists(self) -> None:
        """Verify that the repository data file exists."""
        self.assertTrue(
            os.path.exists(DATA_FILE_PATH),
            f"Repository data file not found at {DATA_FILE_PATH}",
        )

    def test_labels_file_exists(self) -> None:
        """Verify that the labels data file exists."""
        self.assertTrue(
            os.path.exists(LABELS_FILE_PATH),
            f"Labels data file not found at {LABELS_FILE_PATH}",
        )

    def test_data_file_valid_format(self) -> None:
        """Verify that the repository data file is valid TOML."""
        try:
            data = _load_data_file(DATA_FILE_PATH, "toml")
            self.assertIsInstance(data, dict, "TOML file should parse to a dictionary")
        except toml.TomlDecodeError as e:
            self.fail(f"Repository data file is invalid TOML: {e}")
        except IOError as e:
            self.fail(f"Could not read repository data file: {e}")

    def test_labels_file_valid_format(self) -> None:
        """Verify that the labels file is valid JSON."""
        try:
            data = _load_data_file(LABELS_FILE_PATH, "json")
            self.assertIsInstance(data, dict, "JSON file should parse to a dictionary")
        except json.JSONDecodeError as e:
            self.fail(f"Labels file is invalid JSON: {e}")
        except IOError as e:
            self.fail(f"Could not read labels file: {e}")

    def test_data_file_has_required_structure(self) -> None:
        """Verify that the repository data file has the required 'repositories' key."""
        try:
            data = _load_data_file(DATA_FILE_PATH, "toml")
            self.assertIn(
                "repositories",
                data,
                "Repository data file must contain 'repositories' key",
            )
            self.assertIsInstance(
                data["repositories"],
                list,
                "'repositories' must be a list",
            )
        except IOError as e:
            self.fail(f"Could not validate repository data structure: {e}")

    def test_labels_file_has_required_structure(self) -> None:
        """Verify that the labels file has the required 'labels' key."""
        try:
            data = _load_data_file(LABELS_FILE_PATH, "json")
            self.assertIn(
                "labels",
                data,
                "Labels file must contain 'labels' key",
            )
            self.assertIsInstance(
                data["labels"],
                list,
                "'labels' must be a list",
            )
        except IOError as e:
            self.fail(f"Could not validate labels data structure: {e}")

    def test_repositories_have_no_duplicates(self) -> None:
        """Verify that all repository entries are unique."""
        try:
            data = _load_data_file(DATA_FILE_PATH, "toml")
            repos = data.get("repositories", [])
            
            # Find duplicates
            duplicates = [
                item for item, count in Counter(repos).items() if count > 1
            ]
            
            self.assertEqual(
                len(repos),
                len(set(repos)),
                f"Found duplicate repositories: {duplicates}",
            )
        except IOError as e:
            self.fail(f"Could not check for duplicate repositories: {e}")

    def test_labels_have_no_duplicates(self) -> None:
        """Verify that all label entries are unique."""
        try:
            data = _load_data_file(LABELS_FILE_PATH, "json")
            labels = data.get("labels", [])
            
            # Find duplicates
            duplicates = [
                item for item, count in Counter(labels).items() if count > 1
            ]
            
            self.assertEqual(
                len(labels),
                len(set(labels)),
                f"Found duplicate labels: {duplicates}",
            )
        except IOError as e:
            self.fail(f"Could not check for duplicate labels: {e}")

    def test_repositories_not_empty(self) -> None:
        """Verify that the repository list is not empty."""
        try:
            data = _load_data_file(DATA_FILE_PATH, "toml")
            repos = data.get("repositories", [])
            self.assertTrue(
                repos,
                "Repository list must not be empty",
            )
        except IOError as e:
            self.fail(f"Could not validate repository list: {e}")

    def test_labels_not_empty(self) -> None:
        """Verify that the labels list is not empty."""
        try:
            data = _load_data_file(LABELS_FILE_PATH, "json")
            labels = data.get("labels", [])
            self.assertTrue(
                labels,
                "Labels list must not be empty",
            )
        except IOError as e:
            self.fail(f"Could not validate labels list: {e}")


if __name__ == "__main__":
    unittest.main()
