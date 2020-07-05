#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from pathlib import Path
from itertools import count

import requests
import toml

STARS_GT = os.getenv("STARS_GT", "1000")
GOOD_FIRST_ISSUES_GT = os.getenv("GOOD_FIRST_ISSUES_GT", "5")
GITHUB_ACCESS_TOKEN = os.getenv("GITHUB_ACCESS_TOKEN")


def main():
    repositories = []
    query_params = [
        f"stars:>{STARS_GT}",
        f"good-first-issues:>{GOOD_FIRST_ISSUES_GT}",
    ]
    query = "+".join(query_params)
    per_page = 100
    headers = {}
    if GITHUB_ACCESS_TOKEN:
        headers = {"headers": f"token {GITHUB_ACCESS_TOKEN}"}
    for page in count(1):
        response = requests.get(
            (
                "https://api.github.com/search/repositories"
                f"?q={query}&sort=stars&page={page}&per_page={per_page}"
            ),
            headers=headers,
        )
        response.raise_for_status()
        result = response.json()
        if "items" not in result or result["items"] == []:
            break
        repositories.extend(repo["html_url"] for repo in result["items"])

    repo_data_file = Path(__file__).parent / ".." / "data" / "repositories.toml"
    with repo_data_file.open() as file_desc:
        existing_repos = toml.load(file_desc)["repositories"]
    repositories = [
        *existing_repos,
        *list(set(repositories).difference(existing_repos)),
    ]
    print(toml.dumps({"repositories": repositories}).replace('"', "'"))


if __name__ == "__main__":
    main()
