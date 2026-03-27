#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Test suite for data validation and sanity checks.

This module provides comprehensive testing for the Good First Issue project's
data files, ensuring data integrity and format compliance.
"""

import json
import os
import unittest
from collections import Counter
from pathlib import Path
from typing import Any, Dict, List

import toml

# Configuration
DATA_FILE_PATH = "data/repositories.toml"
LABELS_FILE_PATH = "data/labels.json"
GENERATED_DATA_FILE = "data/generated.json"
TAGS_DATA_FILE = "data/tags.json"

# Validation constants
MIN_REPOSITORIES = 100  # Minimum expected repositories
MAX_REPO_NAME_LENGTH = 100
VALID_LABELS_LENGTH_RANGE = (3, 50)
REQUIRED_REPO_FIELDS = ["owner", "name"]
REQUIRED_LABEL_FIELDS = ["labels"]


def _get_data_from_toml(file_path: str) -> Dict[str, Any]:
    """Load and parse TOML data from file.
    
    Args:
        file_path: Path to the TOML file
        
    Returns:
        Parsed TOML data as dictionary
        
    Raises:
        FileNotFoundError: If file doesn't exist
        toml.TomlDecodeError: If TOML is malformed
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file_desc:
            return toml.load(file_desc)
    except FileNotFoundError as e:
        raise FileNotFoundError(f"Data file not found: {file_path}") from e
    except toml.TomlDecodeError as e:
        raise toml.TomlDecodeError(f"Invalid TOML format in {file_path}: {e}") from e


def _get_data_from_json(file_path: str) -> Dict[str, Any]:
    """Load and parse JSON data from file.
    
    Args:
        file_path: Path to the JSON file
        
    Returns:
        Parsed JSON data as dictionary
        
    Raises:
        FileNotFoundError: If file doesn't exist
        json.JSONDecodeError: If JSON is malformed
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file_desc:
            return json.load(file_desc)
    except FileNotFoundError as e:
        raise FileNotFoundError(f"Data file not found: {file_path}") from e
    except json.JSONDecodeError as e:
        raise json.JSONDecodeError(f"Invalid JSON format in {file_path}: {e}", e.doc, e.pos) from e


class TestDataSanity(unittest.TestCase):
    """Comprehensive test suite for data file sanity and integrity."""

    def setUp(self) -> None:
        """Set up test fixtures before each test method."""
        self.data_dir = Path("data")
        self.required_files = [
            DATA_FILE_PATH,
            LABELS_FILE_PATH
        ]

    def test_data_files_exist(self) -> None:
        """Verify that all required data files exist."""
        missing_files = []
        for file_path in self.required_files:
            if not os.path.exists(file_path):
                missing_files.append(file_path)
        
        self.assertFalse(missing_files, 
                       f"Missing required data files: {', '.join(missing_files)}")

    def test_data_file_sane(self) -> None:
        """Verify that the repositories TOML file is valid and contains required data."""
        data = _get_data_from_toml(DATA_FILE_PATH)
        
        # Check required top-level keys
        self.assertIn("repositories", data, 
                      "Missing 'repositories' key in TOML file")
        
        # Validate repositories list
        repositories = data["repositories"]
        self.assertIsInstance(repositories, list, 
                           "'repositories' should be a list")
        self.assertGreaterEqual(len(repositories), MIN_REPOSITORIES,
                              f"Should have at least {MIN_REPOSITORIES} repositories")
        
        # Validate repository URLs format with comprehensive patterns
        invalid_urls = []
        valid_schemes = {"http://", "https://", ""}
        valid_domains = {"github.com/", "www.github.com/"}
        
        for repo_url in repositories:
            # Basic type and empty validation
            if not isinstance(repo_url, str) or not repo_url.strip():
                invalid_urls.append(f"Invalid type/empty: {repo_url}")
                continue
            
            repo_url = repo_url.strip()
            
            # Use regex for more robust validation
            try:
                from gfi.utils import validate_repository_url
            except ImportError:
                # Fallback to basic validation if utils not available
                def validate_repository_url(url: str) -> bool:
                    return bool(url and isinstance(url, str) and 
                               (url.startswith("github.com/") or 
                                url.startswith("https://github.com/") or
                                url.startswith("http://github.com/")))
            
            if not validate_repository_url(repo_url):
                invalid_urls.append(f"Invalid format: {repo_url}")
                continue
            
            # Additional structural validation
            if repo_url.count("/") < 2:
                invalid_urls.append(f"Missing owner/name: {repo_url}")
                continue
        
        self.assertFalse(invalid_urls,
                       f"Invalid repository URLs found: {invalid_urls[:5]}...")

    def test_labels_file_sane(self) -> None:
        """Verify that the labels JSON file is valid and contains required data."""
        data = _get_data_from_json(LABELS_FILE_PATH)
        
        # Check required top-level keys
        self.assertIn("labels", data,
                      "Missing 'labels' key in JSON file")
        
        # Validate labels list
        labels = data["labels"]
        self.assertIsInstance(labels, list,
                           "'labels' should be a list")
        self.assertGreater(len(labels), 0,
                          "Labels list should not be empty")
        
        # Validate individual labels
        invalid_labels = []
        for label in labels:
            if not isinstance(label, str):
                invalid_labels.append(label)
                continue
            
            label_len = len(label.strip())
            if not (VALID_LABELS_LENGTH_RANGE[0] <= label_len <= VALID_LABELS_LENGTH_RANGE[1]):
                invalid_labels.append(f"{label} (length: {label_len})")
        
        self.assertFalse(invalid_labels,
                       f"Invalid labels found: {invalid_labels}")

    def test_no_duplicates(self) -> None:
        """Verify that all repository entries are unique."""
        data = _get_data_from_toml(DATA_FILE_PATH)
        repos = data.get("repositories", [])
        
        # Find duplicates
        repo_counts = Counter(repos)
        duplicates = [repo for repo, count in repo_counts.items() if count > 1]
        
        if duplicates:
            duplicate_info = [(repo, count) for repo, count in repo_counts.items() if count > 1]
            self.fail(f"Found {len(duplicates)} duplicate repositories: {duplicate_info[:5]}...")
        
        # Ensure no empty or whitespace-only entries
        invalid_entries = [repo for repo in repos if not isinstance(repo, str) or not repo.strip()]
        self.assertFalse(invalid_entries,
                       f"Found invalid repository entries: {invalid_entries}")

    def test_generated_files_structure(self) -> None:
        """Test structure of generated files if they exist."""
        generated_files = [GENERATED_DATA_FILE, TAGS_DATA_FILE]
        
        for file_path in generated_files:
            if os.path.exists(file_path):
                try:
                    data = _get_data_from_json(file_path)
                    self.assertIsInstance(data, list,
                                      f"Generated file {file_path} should contain a list")
                    
                    if file_path == GENERATED_DATA_FILE:
                        # Test repository data structure
                        for repo in data[:3]:  # Check first 3 entries
                            self.assertIsInstance(repo, dict,
                                                "Repository entries should be dictionaries")
                            required_fields = ["name", "owner", "url", "language"]
                            for field in required_fields:
                                self.assertIn(field, repo,
                                            f"Missing required field '{field}' in repository data")
                    
                    elif file_path == TAGS_DATA_FILE:
                        # Test tags data structure
                        for tag in data[:3]:  # Check first 3 entries
                            self.assertIsInstance(tag, dict,
                                                "Tag entries should be dictionaries")
                            required_tag_fields = ["language", "count", "slug"]
                            for field in required_tag_fields:
                                self.assertIn(field, tag,
                                            f"Missing required field '{field}' in tag data")
                            
                            self.assertIsInstance(tag["count"], int,
                                                "Tag count should be an integer")
                            self.assertGreater(tag["count"], 0,
                                             "Tag count should be positive")
                
                except (json.JSONDecodeError, FileNotFoundError) as e:
                    self.fail(f"Error reading generated file {file_path}: {e}")


if __name__ == "__main__":
    # Configure unittest for better output
    unittest.main(verbosity=2, exit=False)
