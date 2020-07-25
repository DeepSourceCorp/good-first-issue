from dataclasses import dataclass
from typing import List


@dataclass
class RepositoryInfo:
    """All the necessary information about a given Repository"""

    name: str
    owner: str
    description: str
    language: str
    url: str
    stars: str
    stars_display: str
    last_modified: str
    id: str
    objectID: str
    issues: List["Issue"]


@dataclass
class Issue:
    title: str
    url: str
    number: str
    created_at: str
