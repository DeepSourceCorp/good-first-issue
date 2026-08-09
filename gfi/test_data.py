#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Sanity check tests for repository TOML and label JSON data files."""

import json
import unittest
from collections import Counter
from pathlib import Path
from typing import Any, Callable, Dict

import toml

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE_PATH = BASE_DIR / "data" / "repositories.toml"
LABELS_FILE_PATH = BASE_DIR / "data" / "labels.json"


def _load_data_file(file_path: Path, loader: Callable[[Any], Dict[str, Any]]) -> Dict[str, Any]:
    """Safely load and parse a data file (TOML or JSON)."""
    try:
        with open(file_path, "r", encoding="utf-8") as file_desc:
            return loader(file_desc)
    except FileNotFoundError:
        raise FileNotFoundError(f"Required data file missing: '{file_path}'")
    except (json.JSONDecodeError, toml.TomlDecodeError) as err:
        raise ValueError(f"Failed to parse '{file_path}': {err}")
    except OSError as err:
        raise OSError(f"Error reading file '{file_path}': {err}")


class TestDataSanity(unittest.TestCase):
    """Test suite verifying sanity and integrity of data and labels files."""

    data_file_exists: bool
    labels_file_exists: bool
    toml_data: Dict[str, Any]
    json_data: Dict[str, Any]

    @classmethod
    def setUpClass(cls) -> None:
        """Load data files once before running test cases."""
        cls.data_file_exists = DATA_FILE_PATH.is_file()
        cls.labels_file_exists = LABELS_FILE_PATH.is_file()

        cls.toml_data = (
            _load_data_file(DATA_FILE_PATH, toml.load) if cls.data_file_exists else {}
        )
        cls.json_data = (
            _load_data_file(LABELS_FILE_PATH, json.load) if cls.labels_file_exists else {}
        )

    def test_data_file_exists(self) -> None:
        """Verify that the repositories data file exists."""
        self.assertTrue(
            self.data_file_exists,
            f"Data file '{DATA_FILE_PATH}' does not exist.",
        )

    def test_labels_file_exists(self) -> None:
        """Verify that the labels file exists."""
        self.assertTrue(
            self.labels_file_exists,
            f"Labels file '{LABELS_FILE_PATH}' does not exist.",
        )

    def test_data_file_sane(self) -> None:
        """Verify that the repositories file is valid TOML and contains required keys."""
        self.assertIn(
            "repositories",
            self.toml_data,
            f"Key 'repositories' not found in '{DATA_FILE_PATH}'",
        )
        self.assertIsInstance(
            self.toml_data.get("repositories"),
            list,
            "'repositories' field should be a list",
        )

    def test_labels_file_sane(self) -> None:
        """Verify that the labels file is valid JSON and contains required keys."""
        self.assertIn(
            "labels",
            self.json_data,
            f"Key 'labels' not found in '{LABELS_FILE_PATH}'",
        )
        self.assertIsInstance(
            self.json_data.get("labels"),
            list,
            "'labels' field should be a list",
        )

    def test_no_duplicates(self) -> None:
        """Verify that all repository entries in the TOML file are unique."""
        repos = self.toml_data.get("repositories", [])
        duplicates = [item for item, count in Counter(repos).items() if count > 1]
        self.assertEqual(
            len(repos),
            len(set(repos)),
            f"Duplicate repository entries found: {duplicates}",
        )


if __name__ == "__main__":
    unittest.main()

