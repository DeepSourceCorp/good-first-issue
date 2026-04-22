#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import os
import unittest
from collections import Counter
from pathlib import Path
from typing import Any

try:
    import tomllib
except ModuleNotFoundError:
    tomllib = None
    import toml

DATA_FILE_PATH = Path("data/repositories.toml")
LABELS_FILE_PATH = Path("data/labels.json")


def _get_data_from_toml(file_path: Path) -> Any:
    if tomllib is not None:
        with file_path.open("rb") as file_desc:
            return tomllib.load(file_desc)

    with file_path.open("r", encoding="utf-8") as file_desc:
        return toml.load(file_desc)


def _get_data_from_json(file_path: Path) -> Any:
    with file_path.open("r", encoding="utf-8") as file_desc:
        return json.load(file_desc)


class TestDataSanity(unittest.TestCase):
    """Test for sanity of the data file."""

    def test_data_file_exists(self):
        """Verify that the data file exists."""
        self.assertTrue(os.path.exists(DATA_FILE_PATH), f"Expected {DATA_FILE_PATH} to exist")

    def test_labels_file_exists(self):
        """Verify that the labels file exists."""
        self.assertTrue(os.path.exists(LABELS_FILE_PATH), f"Expected {LABELS_FILE_PATH} to exist")

    def test_data_file_sane(self):
        """Verify that the file is a valid TOML with required data."""
        data = _get_data_from_toml(DATA_FILE_PATH)
        self.assertIn("repositories", data)
        self.assertIsInstance(data["repositories"], list)

    def test_labels_file_sane(self):
        """Verify that the labels file is a valid JSON."""
        data = _get_data_from_json(LABELS_FILE_PATH)
        self.assertIn("labels", data)
        self.assertIsInstance(data["labels"], list)

    def test_no_duplicates(self):
        """Verify that all entries are unique."""
        data = _get_data_from_toml(DATA_FILE_PATH)
        repos = data.get("repositories", [])
        duplicates = [item for item, count in Counter(repos).items() if count > 1]
        self.assertEqual([], duplicates, f"Found duplicate repository entries: {duplicates}")


if __name__ == "__main__":
    unittest.main()
