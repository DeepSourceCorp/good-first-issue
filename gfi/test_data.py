#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import os
import unittest
from collections import Counter
from pathlib import Path

import toml

DATA_FILE_PATH = "data/repositories.toml"
LABELS_FILE_PATH = "data/labels.json"


class DataFileLoader:
    """Utility class for loading data files with caching."""
    
    _cache = {}
    
    @classmethod
    def load_toml(cls, file_path):
        """Load and cache TOML file data."""
        if file_path not in cls._cache:
            with open(file_path, "r") as file_desc:
                cls._cache[file_path] = toml.load(file_desc)
        return cls._cache[file_path]
    
    @classmethod
    def load_json(cls, file_path):
        """Load and cache JSON file data."""
        if file_path not in cls._cache:
            with open(file_path, "r") as file_desc:
                cls._cache[file_path] = json.load(file_desc)
        return cls._cache[file_path]


class TestDataSanity(unittest.TestCase):
    """Test for sanity of the data files with optimized performance."""

    def setUp(self):
        """Set up test fixtures."""
        self.data_path = Path(DATA_FILE_PATH)
        self.labels_path = Path(LABELS_FILE_PATH)

    def test_data_file_exists(self):
        """Verify that the data file exists."""
        self.assertTrue(self.data_path.exists(), f"Data file not found: {DATA_FILE_PATH}")

    def test_labels_file_exists(self):
        """Verify that the labels file exists."""
        self.assertTrue(self.labels_path.exists(), f"Labels file not found: {LABELS_FILE_PATH}")

    def test_data_file_sane(self):
        """Verify that the file is a valid TOML with required data."""
        data = DataFileLoader.load_toml(DATA_FILE_PATH)
        self.assertIn("repositories", data, "Missing 'repositories' key in data file")

    def test_labels_file_sane(self):
        """Verify that the labels file is a valid JSON"""
        data = DataFileLoader.load_json(LABELS_FILE_PATH)
        self.assertIn("labels", data, "Missing 'labels' key in labels file")

    def test_no_duplicates(self):
        """Verify that all repository entries are unique."""
        data = DataFileLoader.load_toml(DATA_FILE_PATH)
        repos = data.get("repositories", [])
        
        # Find duplicates efficiently
        seen = set()
        duplicates = set()
        for repo in repos:
            if repo in seen:
                duplicates.add(repo)
            else:
                seen.add(repo)
        
        if duplicates:
            print(f"Duplicate repositories found: {list(duplicates)}")
        
        self.assertEqual(len(repos), len(set(repos)), 
                        f"Found {len(duplicates)} duplicate repositories")

    def test_file_permissions(self):
        """Verify that files are readable."""
        self.assertTrue(os.access(DATA_FILE_PATH, os.R_OK), 
                       f"Data file is not readable: {DATA_FILE_PATH}")
        self.assertTrue(os.access(LABELS_FILE_PATH, os.R_OK), 
                       f"Labels file is not readable: {LABELS_FILE_PATH}")


if __name__ == "__main__":
    unittest.main()