#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import os
from algoliasearch.search_client import SearchClient

ALGOLIA_APP_ID = os.getenv("ALGOLIA_APP_ID")
ALGOLIA_API_KEY = os.getenv("ALGOLIA_API_KEY")
ALGOLIA_INDEX_NAME = os.getenv("ALGOLIA_INDEX_NAME")
GENERATED_FILE_NAME = "data/generated.json"

if __name__ == "__main__":
    CLIENT = SearchClient.create(ALGOLIA_APP_ID, ALGOLIA_API_KEY)
    INDEX = CLIENT.init_index(ALGOLIA_INDEX_NAME)

    with open(GENERATED_FILE_NAME) as file_desc:
        RECORDS = json.load(file_desc)

    INDEX.save_objects(RECORDS, {"autoGenerateObjectIDIfNotExist": True})
