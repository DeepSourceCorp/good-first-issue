#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import annotations

import json
import os
import unittest
from collections import Counter
from typing import Any

import toml

from gfi.populate import GH_URL_PATTERN

DATA_FILE_PATH = "data/repositories.toml"
LABELS_FILE_PATH = "data/labels.json"
GENERATED_JSON_PATH = "data/generated.json"
TAGS_JSON_PATH = "data/tags.json"

REQUIRED_REPO_KEYS = frozenset(
    {
        "name",
        "owner",
        "description",
        "language",
        "slug",
        "url",
        "stars",
        "stars_display",
        "last_modified",
        "id",
        "issues",
    }
)
REQUIRED_ISSUE_KEYS = frozenset(
    {"title", "url", "number", "comments_count", "created_at"}
)
REQUIRED_TAG_KEYS = frozenset({"language", "count", "slug"})


def _get_data_from_toml(file_path: str) -> dict[str, Any]:
    with open(file_path, encoding="utf-8") as file_desc:
        return toml.load(file_desc)


def _get_data_from_json(file_path: str) -> Any:
    with open(file_path, encoding="utf-8") as file_desc:
        return json.load(file_desc)


def _assert_github_repo_urls(urls: list[str]) -> None:
    for url in urls:
        assert GH_URL_PATTERN.search(
            url
        ), f"Repository entry does not look like a GitHub repo path: {url!r}"


class TestDataSanity(unittest.TestCase):
    """Tests for sanity of configuration and generated data files."""

    def test_data_file_exists(self) -> None:
        assert os.path.exists(DATA_FILE_PATH)

    def test_labels_file_exists(self) -> None:
        assert os.path.exists(LABELS_FILE_PATH)

    def test_generated_json_exists(self) -> None:
        assert os.path.exists(GENERATED_JSON_PATH)

    def test_tags_json_exists(self) -> None:
        assert os.path.exists(TAGS_JSON_PATH)

    def test_data_file_sane(self) -> None:
        data = _get_data_from_toml(DATA_FILE_PATH)
        assert "repositories" in data
        repos = data["repositories"]
        assert isinstance(repos, list)
        assert all(isinstance(u, str) for u in repos)
        _assert_github_repo_urls(repos)

    def test_labels_file_sane(self) -> None:
        data = _get_data_from_json(LABELS_FILE_PATH)
        assert isinstance(data, dict)
        assert "labels" in data
        labels = data["labels"]
        assert isinstance(labels, list)
        assert len(labels) > 0
        assert all(isinstance(lab, str) and lab.strip() for lab in labels)

    def test_no_duplicate_repositories(self) -> None:
        data = _get_data_from_toml(DATA_FILE_PATH)
        repos = data.get("repositories", [])
        dupes = [item for item, count in Counter(repos).items() if count > 1]
        assert not dupes, f"Duplicate repository URLs: {dupes}"

    def test_generated_json_schema(self) -> None:
        raw = _get_data_from_json(GENERATED_JSON_PATH)
        assert isinstance(raw, list)
        assert len(raw) > 0
        ids_seen: set[str] = set()
        for repo in raw:
            assert isinstance(repo, dict)
            missing = REQUIRED_REPO_KEYS - repo.keys()
            assert not missing, f"Repo missing keys {missing}: {repo.get('owner')}/{repo.get('name')}"
            repo_id = repo["id"]
            assert isinstance(repo_id, str)
            assert repo_id not in ids_seen, f"Duplicate repository id: {repo_id}"
            ids_seen.add(repo_id)
            issues = repo["issues"]
            assert isinstance(issues, list)
            for issue in issues:
                assert isinstance(issue, dict)
                imiss = REQUIRED_ISSUE_KEYS - issue.keys()
                assert not imiss, f"Issue missing keys {imiss} in {repo_id}"

    def test_tags_json_schema(self) -> None:
        raw = _get_data_from_json(TAGS_JSON_PATH)
        assert isinstance(raw, list)
        assert len(raw) > 0
        slugs: set[str] = set()
        for tag in raw:
            assert isinstance(tag, dict)
            assert not (REQUIRED_TAG_KEYS - tag.keys())
            assert isinstance(tag["language"], str)
            assert isinstance(tag["slug"], str)
            assert isinstance(tag["count"], int)
            assert tag["count"] >= 1
            assert tag["slug"] not in slugs
            slugs.add(tag["slug"])

    def test_each_tag_slug_has_repositories(self) -> None:
        repos = _get_data_from_json(GENERATED_JSON_PATH)
        tags = _get_data_from_json(TAGS_JSON_PATH)
        counts = Counter(str(r["slug"]) for r in repos)
        for tag in tags:
            slug = tag["slug"]
            assert counts[slug] >= 1, (
                f"tags.json lists {tag['language']!r} ({slug!r}) but no repository uses that slug"
            )


if __name__ == "__main__":
    unittest.main()
