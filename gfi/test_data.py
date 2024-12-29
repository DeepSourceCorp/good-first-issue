#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import os
import unittest
from collections import Counter
from typing import Any
import toml

DATA_FILE_PATH = os.getenv("DATA_FILE_PATH", "data/repositories.toml")
LABELS_FILE_PATH = os.getenv("LABELS_FILE_PATH", "data/labels.json")


def _get_data(file_path: str, file_type: str = "toml") -> Any:
    """Read and parse a file of the given type."""
    try:
        with open(file_path, "r") as file_desc:
            if file_type == "toml":
                return toml.load(file_desc)
            elif file_type == "json":
                return json.load(file_desc)
            else:
                raise ValueError(f"Unsupported file type: {file_type}")
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
    except (toml.TomlDecodeError, json.JSONDecodeError) as e:
        raise ValueError(f"Invalid {file_type.upper()} format in {file_path}: {e}")


class TestDataSanity(unittest.TestCase):
    """Test for sanity of the data and labels files."""

    def test_data_file_exists(self):
        """Verify that the data file exists."""
        self.assertTrue(os.path.exists(DATA_FILE_PATH), "Data file does not exist")

    def test_labels_file_exists(self):
        """Verify that the labels file exists."""
        self.assertTrue(os.path.exists(LABELS_FILE_PATH), "Labels file does not exist")

    def test_data_file_sane(self):
        """Verify that the data file is a valid TOML and contains required data."""
        data = _get_data(DATA_FILE_PATH, "toml")
        self.assertIn("repositories", data, "Missing 'repositories' in data file")

    def test_labels_file_sane(self):
        """Verify that the labels file is a valid JSON and contains required labels."""
        data = _get_data(LABELS_FILE_PATH, "json")
        self.assertIn("labels", data, "Missing 'labels' in labels file")

    def test_no_duplicates(self):
        """Verify that there are no duplicate entries in repositories."""
        data = _get_data(DATA_FILE_PATH, "toml")
        repos = data.get("repositories", [])
        duplicates = [item for item, count in Counter(repos).items() if count > 1]
        self.assertEqual(len(duplicates), 0, f"Duplicate entries found: {duplicates}")


if __name__ == "__main__":
    unittest.main()
