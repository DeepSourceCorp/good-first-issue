#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import unittest
from collections import Counter
from pathlib import Path

import toml

DATA_FILE_PATH = Path("data/repositories.toml")
LABELS_FILE_PATH = Path("data/labels.json")


def _load_data(file_path, loader):
    """Load a UTF-8 data file and report a useful assertion on failure."""
    try:
        with file_path.open(encoding="utf-8") as file_desc:
            return loader(file_desc)
    except (OSError, ValueError, toml.TomlDecodeError) as error:
        raise AssertionError(f"Unable to load {file_path}: {error}") from error


def _get_data_from_toml(file_path):
    return _load_data(file_path, toml.load)


def _get_data_from_json(file_path):
    return _load_data(file_path, json.load)


class TestDataSanity(unittest.TestCase):
    """Test for sanity of the data file."""

    def test_data_file_exists(self):
        """Verify that the data file exists."""
        self.assertTrue(DATA_FILE_PATH.is_file())

    def test_labels_file_exists(self):
        """Verify that the labels file exists."""
        self.assertTrue(LABELS_FILE_PATH.is_file())

    def test_data_file_sane(self):
        """Verify that the file is a valid TOML with required data."""
        data = _get_data_from_toml(DATA_FILE_PATH)
        self.assertIn("repositories", data)
        self.assertGreater(len(data["repositories"]), 0)

    def test_labels_file_sane(self):
        """Verify that the labels file is a valid JSON"""
        data = _get_data_from_json(LABELS_FILE_PATH)
        self.assertIn("labels", data)
        self.assertGreater(len(data["labels"]), 0)

    def test_no_duplicates(self):
        """Verify that all entries are unique."""
        repositories = _get_data_from_toml(DATA_FILE_PATH).get("repositories", [])
        duplicates = [item for item, count in Counter(repositories).items() if count > 1]
        self.assertEqual(duplicates, [], f"Duplicate repositories: {duplicates}")


if __name__ == "__main__":
    unittest.main()
