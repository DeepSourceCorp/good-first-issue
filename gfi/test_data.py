#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import os
import unittest
from collections import Counter

import toml

DATA_FILE_PATH = "data/repositories.toml"
LABELS_FILE_PATH = "data/labels.json"


def _load_file(file_path):
    """Load and parse a JSON or TOML file with error handling."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    _, ext = os.path.splitext(file_path)
    try:
        with open(file_path, "r", encoding="utf-8") as file_desc:
            if ext.lower() == ".toml":
                return toml.load(file_desc)
            elif ext.lower() == ".json":
                return json.load(file_desc)
            else:
                raise ValueError(f"Unsupported file format: {ext}")
    except (json.JSONDecodeError, toml.TomlDecodeError) as err:
        raise ValueError(f"Failed to parse {file_path}: {err}") from err
    except Exception as err:
        raise RuntimeError(f"Error reading file {file_path}: {err}") from err


class TestDataSanity(unittest.TestCase):
    """Tests for sanity and structural correctness of the data and label files."""

    def test_data_file_exists(self):
        """Verify that the repository data file exists at the expected path."""
        self.assertTrue(
            os.path.exists(DATA_FILE_PATH),
            f"Repository TOML file does not exist at {DATA_FILE_PATH}"
        )

    def test_labels_file_exists(self):
        """Verify that the labels JSON file exists at the expected path."""
        self.assertTrue(
            os.path.exists(LABELS_FILE_PATH),
            f"Labels JSON file does not exist at {LABELS_FILE_PATH}"
        )

    def test_data_file_sane(self):
        """Verify that the repository data file is a valid TOML and has the 'repositories' key."""
        try:
            data = _load_file(DATA_FILE_PATH)
        except Exception as err:
            self.fail(f"Failed to load or parse repository TOML: {err}")
        self.assertIn("repositories", data, "Repository TOML is missing 'repositories' key")

    def test_labels_file_sane(self):
        """Verify that the labels file is a valid JSON and has the 'labels' key."""
        try:
            data = _load_file(LABELS_FILE_PATH)
        except Exception as err:
            self.fail(f"Failed to load or parse labels JSON: {err}")
        self.assertIn("labels", data, "Labels JSON is missing 'labels' key")

    def test_no_duplicates(self):
        """Verify that all repository entries in repositories.toml are unique."""
        try:
            data = _load_file(DATA_FILE_PATH)
        except Exception as err:
            self.fail(f"Failed to load or parse repository TOML: {err}")
        repos = data.get("repositories", [])
        duplicates = [item for item, count in Counter(repos).items() if count > 1]
        self.assertEqual(
            len(repos),
            len(set(repos)),
            f"Duplicate repository entries found: {duplicates}"
        )


if __name__ == "__main__":
    unittest.main()
