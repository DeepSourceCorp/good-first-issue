#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import os
import unittest
from collections import Counter

import toml

DATA_FILE_PATH = "data/repositories.toml"
LABELS_FILE_PATH = "data/labels.json"


def _get_data_from_file(file_path):
    """Reads and parses data from a TOML or JSON file with error handling."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Missing required data file: {file_path}")

    try:
        with open(file_path, "r", encoding="utf-8") as file_desc:
            if file_path.endswith(".toml"):
                return toml.load(file_desc)
            elif file_path.endswith(".json"):
                return json.load(file_desc)
            else:
                raise ValueError(f"Unsupported file extension for: {file_path}")
    except (json.JSONDecodeError, toml.TomlDecodeError) as e:
        raise ValueError(f"Syntax error while parsing {file_path}: {e}")


class TestDataSanity(unittest.TestCase):
    """Test for sanity of the data file."""

    def test_data_file_exists(self):
        """Verify that the data file exists."""
        self.assertTrue(os.path.exists(DATA_FILE_PATH), "Data file is missing.")

    def test_labels_file_exists(self):
        """Verify that the labels file exists."""
        self.assertTrue(os.path.exists(LABELS_FILE_PATH), "Labels file is missing.")

    def test_data_file_sane(self):
        """Verify that the file is a valid TOML with required data."""
        data = _get_data_from_file(DATA_FILE_PATH)
        self.assertIn("repositories", data)

    def test_labels_file_sane(self):
        """Verify that the labels file is a valid JSON."""
        data = _get_data_from_file(LABELS_FILE_PATH)
        self.assertIn("labels", data)

    def test_no_duplicates(self):
        """Verify that all entries are unique."""
        data = _get_data_from_file(DATA_FILE_PATH)
        repos = data.get("repositories", [])
        
        # Capture duplicates to provide a helpful error message if the test fails
        duplicates = [item for item, count in Counter(repos).items() if count > 1]
        self.assertEqual(
            len(repos), 
            len(set(repos)), 
            f"Duplicate repositories found: {duplicates}"
        )


if __name__ == "__main__":
    unittest.main()
