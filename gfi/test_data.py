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

    def test_data_file_exists(self):
        """Verify that the data file exists."""
        assert os.path.exists(DATA_FILE_PATH), f"Data file not found: {DATA_FILE_PATH}"

    def test_labels_file_exists(self):
        """Verify that the labels file exists."""
        assert os.path.exists(LABELS_FILE_PATH), f"Labels file not found: {LABELS_FILE_PATH}"

    def test_data_file_sane(self):
        """Verify that the file is a valid TOML with required data."""
        data = _get_data_from_toml(DATA_FILE_PATH)
        self.assertIn("repositories", data)

    def test_labels_file_sane(self):
        """Verify that the labels file is a valid JSON"""
        data = _get_data_from_json(LABELS_FILE_PATH)
        self.assertIn("labels", data)

    def test_no_duplicates(self):
        """Verify that all entries are unique."""
        data = _get_data_from_toml(DATA_FILE_PATH)
        repos = data.get("repositories", [])
        duplicates = [item for item, count in Counter(repos).items() if count > 1]
        self.assertEqual(len(repos), len(set(repos)), f"Duplicate repos found: {duplicates}")


if __name__ == "__main__":
    unittest.main()
