#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import unittest
import toml

DATA_FILE_PATH = 'data/repositories.toml'


def _get_data_from_toml(file_path):
    with open(file_path, 'r') as file_desc:
        return toml.load(file_desc)


class TestDataSanity(unittest.TestCase):
    """Test for sanity of the data file."""

    @staticmethod
    def test_data_file_exists():
        """Verify that the data file exists."""
        assert os.path.exists(DATA_FILE_PATH)

    @staticmethod
    def test_data_file_sane():
        """Verify that the file is a valid TOML with required data."""
        data = _get_data_from_toml(DATA_FILE_PATH)
        assert 'repositories' in data

    @staticmethod
    def test_no_duplicates():
        """Verify that all entries are unique."""
        data = _get_data_from_toml(DATA_FILE_PATH)
        repos = data.get('repositories', [])
        assert len(repos) == len(set(repos))


if __name__ == '__main__':
    unittest.main()
