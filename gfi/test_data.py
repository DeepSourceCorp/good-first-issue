#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import os
import unittest
from collections import Counter

import toml


# Path definitions for the data file and the labels file
DATA_FILE_PATH = "data/repositories.toml"
LABELS_FILE_PATH = "data/labels.json"


def read_file(file_path, loader_func):
    """
    A generic function for reading files. It reads and parses the content of a file based on the specified loading function.

    Args:
        file_path (str): The path of the file to be read.
        loader_func (function): The function used to parse the file content (such as toml.load or json.load).

    Returns:
        The parsed Python object. If there are problems with file reading or parsing, corresponding exceptions will be raised.
    """
    try:
        with open(file_path, "r") as file_descriptor:
            return loader_func(file_descriptor)
    except FileNotFoundError:
        print(f"The file {file_path} does not exist")
        raise
    except (toml.TomlDecodeError, json.JSONDecodeError) as e:
        print(f"The {os.path.splitext(file_path)[1].lstrip('.').upper()} file {file_path} has a parsing error: {e}")
        raise


class TestDataSanity(unittest.TestCase):
    """
    A test class for the sanity of data files.
    """

    def test_data_file_exists(self):
        """
        Verify whether the data file exists.
        """
        self.assertTrue(os.path.exists(DATA_FILE_PATH), f"The data file {DATA_FILE_PATH} does not exist")

    def test_labels_file_exists(self):
        """
        Verify whether the labels file exists.
        """
        self.assertTrue(os.path.exists(LABELS_FILE_PATH), f"The labels file {LABELS_FILE_PATH} does not exist")

    def test_data_file_sane(self):
        """
        Verify that the data file is in valid TOML format and contains the necessary data.
        """
        data = read_file(DATA_FILE_PATH, toml.load)
        self.assertIn("repositories", data)

    def test_labels_file_sane(self):
        """
        Verify that the labels file is in valid JSON format.
        """
        data = read_file(LABELS_FILE_PATH, json.load)
        self.assertIn("labels", data)

    def test_no_duplicates(self):
        """
        Verify that there are no duplicates among all entries.
        """
        data = read_file(DATA_FILE_PATH, toml.load)
        repos = data.get("repositories", [])
        self.assertEqual(len(repos), len(set(repos)))


if __name__ == "__main__":
    unittest.main()
