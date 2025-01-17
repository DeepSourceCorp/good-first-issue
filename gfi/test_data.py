#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import os
import unittest
from collections import Counter
from typing import Any

import toml

DATA_FILE_PATH = "data/repositories.toml"
LABELS_FILE_PATH = "data/labels.json"


def _load_toml(file_path: str) -> Any:
    """Load and return data from a TOML file."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"TOML file not found: {file_path}")
    with open(file_path, "r") as file_desc:
        return toml.load(file_desc)


def _load_json(file_path: str) -> Any:
    """Load and return data from a JSON file."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"JSON file not found: {file_path}")
    with open(file_path, "r") as file_desc:
        return json.load(file_desc)


class TestDataSanity(unittest.TestCase):
    """Test for sanity of the data files."""

    def test_data_file_exists(self):
        """Verify that the data file exists and is not empty."""
        self.assertTrue(
            os.path.exists(DATA_FILE_PATH),
            f"Data file does not exist: {DATA_FILE_PATH}",
        )
        self.assertGreater(
            os.path.getsize(DATA_FILE_PATH),
            0,
            f"Data file is empty: {DATA_FILE_PATH}",
        )

    def test_labels_file_exists(self):
        """Verify that the labels file exists and is not empty."""
        self.assertTrue(
            os.path.exists(LABELS_FILE_PATH),
            f"Labels file does not exist: {LABELS_FILE_PATH}",
        )
        self.assertGreater(
            os.path.getsize(LABELS_FILE_PATH),
            0,
            f"Labels file is empty: {LABELS_FILE_PATH}",
        )

    def test_data_file_sane(self):
        """Verify that the data file is a valid TOML with required data."""
        try:
            data = _load_toml(DATA_FILE_PATH)
            self.assertIn("repositories", data, "Missing 'repositories' key in data file.")
            self.assertIsInstance(
                data["repositories"], list, "'repositories' should be a list."
            )
            self.assertGreater(
                len(data["repositories"]),
                0,
                "'repositories' should not be empty.",
            )
        except Exception as e:
            self.fail(f"Error reading or validating data file: {e}")

    def test_labels_file_sane(self):
        """Verify that the labels file is a valid JSON with required data."""
        try:
            data = _load_json(LABELS_FILE_PATH)
            self.assertIn("labels", data, "Missing 'labels' key in labels file.")
            self.assertIsInstance(
                data["labels"], list, "'labels' should be a list."
            )
            self.assertGreater(
                len(data["labels"]),
                0,
                "'labels' should not be empty.",
            )
        except Exception as e:
            self.fail(f"Error reading or validating labels file: {e}")

    def test_no_duplicates(self):
        """Verify that all entries in 'repositories' are unique."""
        data = _load_toml(DATA_FILE_PATH)
        repos = data.get("repositories", [])
        duplicates = [item for item, count in Counter(repos).items() if count > 1]
        self.assertEqual(
            len(repos),
            len(set(repos)),
            f"Found duplicates in repositories: {duplicates}",
        )


if __name__ == "__main__":
    unittest.main()
