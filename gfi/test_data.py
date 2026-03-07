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
    """Load data from TOML file with exception handling."""
    try:
        with open(file_path, "r") as file_desc:
            return toml.load(file_desc)
    except Exception as e:
        raise RuntimeError(f"Failed to load TOML file {file_path}: {e}")


def _get_data_from_json(file_path):
    """Load data from JSON file with exception handling."""
    try:
        with open(file_path, "r") as file_desc:
            return json.load(file_desc)
    except Exception as e:
        raise RuntimeError(f"Failed to load JSON file {file_path}: {e}")


class TestDataSanity(unittest.TestCase):
    """Test for sanity of the data file."""

    @staticmethod
    def test_data_file_exists():
        """Verify that the data file exists."""
        assert os.path.exists(DATA_FILE_PATH), f"{DATA_FILE_PATH} not found."

    @staticmethod
    def test_labels_file_exists():
        """Verify that the labels file exists."""
        assert os.path.exists(LABELS_FILE_PATH), f"{LABELS_FILE_PATH} not found."

    @staticmethod
    def test_data_file_sane():
        """Verify that the file is a valid TOML with required data."""
        data = _get_data_from_toml(DATA_FILE_PATH)
        assert "repositories" in data, "Key 'repositories' missing in TOML file."

    @staticmethod
    def test_labels_file_sane():
        """Verify that the labels file is a valid JSON"""
        data = _get_data_from_json(LABELS_FILE_PATH)
        assert "labels" in data, "Key 'labels' missing in JSON file."

    @staticmethod
    def test_no_duplicates():
        """Verify that all entries are unique."""
        data = _get_data_from_toml(DATA_FILE_PATH)
        repos = data.get("repositories", [])
        duplicates = [item for item, count in Counter(repos).items() if count > 1]
        if duplicates:
            print(f"Duplicate entries found: {duplicates}")
        assert len(repos) == len(set(repos)), "Duplicate repository entries found."


if __name__ == "__main__":
    unittest.main()
