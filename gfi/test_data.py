#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import os
import unittest
from collections import Counter

import toml

DATA_FILE_PATH = "data/repositories.toml"
LABELS_FILE_PATH = "data/labels.json"


def _load_file_data(file_path):
    """Generic helper to load TOML or JSON files with proper error handling."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File '{file_path}' does not exist.")

    with open(file_path, "r", encoding="utf-8") as file_desc:
        try:
            if file_path.endswith(".toml"):
                return toml.load(file_desc)
            elif file_path.endswith(".json"):
                return json.load(file_desc)
            else:
                raise ValueError(f"Unsupported file format for '{file_path}'. Only .toml and .json are supported.")
        except (toml.TomlDecodeError, json.JSONDecodeError) as e:
            raise ValueError(f"Error parsing file '{file_path}': {e}")


class TestDataSanity(unittest.TestCase):
    """Test for sanity of the data file."""

    def test_data_file_exists(self):
        """Verify that the data file exists."""
        self.assertTrue(os.path.exists(DATA_FILE_PATH), f"Data file missing: {DATA_FILE_PATH}")

    def test_labels_file_exists(self):
        """Verify that the labels file exists."""
        self.assertTrue(os.path.exists(LABELS_FILE_PATH), f"Labels file missing: {LABELS_FILE_PATH}")

    def test_data_file_sane(self):
        """Verify that the file is a valid TOML with required data."""
        data = _load_file_data(DATA_FILE_PATH)
        self.assertIn("repositories", data, "'repositories' key not found in TOML data.")

    def test_labels_file_sane(self):
        """Verify that the labels file is a valid JSON."""
        data = _load_file_data(LABELS_FILE_PATH)
        self.assertIn("labels", data, "'labels' key not found in JSON data.")

    def test_no_duplicates(self):
        """Verify that all entries are unique."""
        data = _load_file_data(DATA_FILE_PATH)
        repos = data.get("repositories", [])
        
        # Count occurrences to find duplicates
        duplicates = [item for item, count in Counter(repos).items() if count > 1]
        
        # Assert no duplicates exist, showing which ones are duplicated if it fails
        self.assertEqual(
            len(repos), 
            len(set(repos)), 
            f"Duplicate entries found in repositories: {duplicates}"
        )


if __name__ == "__main__":
    unittest.main()
    
