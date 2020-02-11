#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import unittest
import toml

DATA_FILE_PATH = 'data/repositories.toml'


class TestDataSanity(unittest.TestCase):
    """Test for sanity of the data file."""

    @staticmethod
    def test_data_file_exists():
        """Verify that the data file exists."""
        assert os.path.exists(DATA_FILE_PATH)

    @staticmethod
    def test_data_file_sane():
        """Verify that the file is a valid TOML with required data."""
        with open(DATA_FILE_PATH, 'r') as file_desc:
            data = toml.load(file_desc)
        assert 'repositories' in data


if __name__ == '__main__':
    unittest.main()
