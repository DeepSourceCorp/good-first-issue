#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""GitHub API utilities for Good First Issue.

This module provides specialized GitHub API functionality including
rate limiting, repository analysis, and issue fetching.
"""

import threading
import time
from datetime import datetime, timezone
from typing import List, Optional, Set, Dict, Any

from github3 import exceptions, login
from loguru import logger

from .config import get_config
from .utils import calculate_days_since, is_recent_activity


class GitHubRateLimiter:
    """Thread-safe rate limiter for GitHub API requests.
    
    This class manages GitHub API rate limits by coordinating requests
    across multiple threads and implementing proactive pausing when
    the remaining quota is low.
    """

    def __init__(self, client, requests_per_second: float = 1.0) -> None:
        """Initialize the rate limiter.
        
        Args:
            client: GitHub API client instance
            requests_per_second: Maximum requests per second to allow
        """
        self._client = client
        self._lock = threading.Lock()
        self._min_interval = 1.0 / requests_per_second
        self._last_request_time = 0.0
        self._remaining: Optional[int] = None
        self._reset_time: Optional[float] = None
        self._paused_until = 0.0

    def acquire(self) -> None:
        """Block until it's safe to make an API request."""
        with self._lock:
            # Check for coordinated pause
            current_time = time.time()
            if current_time < self._paused_until:
                wait_time = self._paused_until - current_time
                logger.info("Waiting {:.0f}s for rate limit reset", wait_time)
                time.sleep(wait_time)

            # Refresh rate limit info periodically
            if self._remaining is None or self._remaining % 100 == 0:
                self._update_rate_limit()

            # Proactive pause if quota low
            if self._remaining is not None and self._remaining < 100:
                if self._reset_time:
                    wait_time = max(0, self._reset_time - time.time() + 5)
                    if wait_time > 0:
                        logger.warning("Low quota ({}). Pausing {:.0f}s", self._remaining, wait_time)
                        self._paused_until = time.time() + wait_time
                        time.sleep(wait_time)
                        self._remaining = None

            # Enforce minimum interval
            elapsed = time.time() - self._last_request_time
            if elapsed < self._min_interval:
                time.sleep(self._min_interval - elapsed)

            self._last_request_time = time.time()
            if self._remaining:
                self._remaining -= 1

    def _update_rate_limit(self) -> None:
        """Update rate limit information from GitHub API."""
        try:
            info = self._client.rate_limit()['resources']['core']
            self._remaining = info['remaining']
            self._reset_time = info['reset']
            logger.debug("Rate limit: {}/{}", self._remaining, info['limit'])
        except Exception as e:
            logger.warning("Failed to check rate limit: {}", e)

    def report_rate_limit_hit(self) -> None:
        """Call when ForbiddenError received - triggers coordinated pause."""
        with self._lock:
            self._update_rate_limit()
            if self._reset_time:
                wait_time = max(60, self._reset_time - time.time() + 5)
            else:
                wait_time = 60
            self._paused_until = time.time() + wait_time
            self._remaining = 0
            logger.warning("Rate limit hit. All workers pause for {:.0f}s", wait_time)


class GitHubRepository:
    """Wrapper for GitHub repository with enhanced functionality."""
    
    def __init__(self, owner: str, name: str, client, rate_limiter: GitHubRateLimiter) -> None:
        """Initialize repository wrapper.
        
        Args:
            owner: Repository owner
            name: Repository name
            client: GitHub API client
            rate_limiter: Rate limiter instance
        """
        self.owner = owner
        self.name = name
        self._client = client
        self._rate_limiter = rate_limiter
        self._repository = None
        
    def _get_repository(self):
        """Get repository object with caching."""
        if self._repository is None:
            self._rate_limiter.acquire()
            self._repository = self._client.repository(self.owner, self.name)
        return self._repository
    
    def is_archived(self) -> bool:
        """Check if repository is archived.
        
        Returns:
            True if repository is archived
        """
        try:
            repo = self._get_repository()
            return repo.archived
        except Exception as e:
            logger.warning("Failed to check archived status for {}/{}: {}", 
                          self.owner, self.name, e)
            return True  # Skip if we can't determine
    
    def is_active(self, max_days: int = 90) -> bool:
        """Check if repository has recent activity.
        
        Args:
            max_days: Maximum days to consider active
            
        Returns:
            True if repository is active
        """
        try:
            repo = self._get_repository()
            return is_recent_activity(repo.pushed_at, max_days)
        except Exception as e:
            logger.warning("Failed to check activity for {}/{}: {}", 
                          self.owner, self.name, e)
            return False
    
    def get_language(self) -> Optional[str]:
        """Get repository primary language.
        
        Returns:
            Primary language or None if not available
        """
        try:
            repo = self._get_repository()
            return repo.language
        except Exception as e:
            logger.warning("Failed to get language for {}/{}: {}", 
                          self.owner, self.name, e)
            return None
    
    def get_issues_with_labels(self, labels: List[str], limit: int = 10) -> Set:
        """Get issues matching any of the specified labels.
        
        Args:
            labels: List of labels to search for
            limit: Maximum issues per label
            
        Returns:
            Set of issue objects
        """
        issues = set()
        
        for label in labels:
            try:
                self._rate_limiter.acquire()
                issues_for_label = self._repository.issues(
                    labels=label,
                    state="open",
                    number=limit,
                    sort="created",
                    direction="desc",
                )
                issues.update(issues_for_label)
            except Exception as e:
                logger.warning("Failed to fetch issues for label '{}' in {}/{}: {}", 
                              label, self.owner, self.name, e)
                continue
        
        return issues
    
    def get_repository_info(self) -> Optional[Dict[str, Any]]:
        """Get comprehensive repository information.
        
        Returns:
            Repository information dict or None if unavailable
        """
        try:
            repo = self._get_repository()
            
            return {
                "name": repo.name,
                "owner": repo.owner.login,
                "description": repo.description or "",
                "language": repo.language,
                "url": repo.html_url,
                "stars": repo.stargazers_count,
                "forks": repo.fork_count,
                "open_issues": repo.open_issues_count,
                "created_at": repo.created_at.isoformat(),
                "updated_at": repo.updated_at.isoformat(),
                "pushed_at": repo.pushed_at.isoformat(),
                "archived": repo.archived,
                "size": repo.size,
                "id": str(repo.id),
            }
        except Exception as e:
            logger.error("Failed to get repository info for {}/{}: {}", 
                        self.owner, self.name, e)
            return None


class GitHubClient:
    """Enhanced GitHub client with rate limiting and error handling."""
    
    def __init__(self, access_token: str, requests_per_second: float = 1.0) -> None:
        """Initialize GitHub client.
        
        Args:
            access_token: GitHub access token
            requests_per_second: Request rate limit
        """
        self._client = login(token=access_token)
        self._rate_limiter = GitHubRateLimiter(self._client, requests_per_second)
        
    def get_repository(self, owner: str, name: str) -> GitHubRepository:
        """Get repository wrapper.
        
        Args:
            owner: Repository owner
            name: Repository name
            
        Returns:
            Repository wrapper instance
        """
        return GitHubRepository(owner, name, self._client, self._rate_limiter)
    
    def test_connection(self) -> bool:
        """Test GitHub API connection.
        
        Returns:
            True if connection is successful
        """
        try:
            self._rate_limiter.acquire()
            user = self._client.me()
            logger.info("Successfully connected to GitHub as: {}", user.login)
            return True
        except Exception as e:
            logger.error("Failed to connect to GitHub: {}", e)
            return False
    
    def get_rate_limit_info(self) -> Dict[str, Any]:
        """Get current rate limit information.
        
        Returns:
            Rate limit information
        """
        try:
            self._rate_limiter.acquire()
            limits = self._client.rate_limit()
            return {
                "core": {
                    "limit": limits["resources"]["core"]["limit"],
                    "remaining": limits["resources"]["core"]["remaining"],
                    "reset": limits["resources"]["core"]["reset"],
                }
            }
        except Exception as e:
            logger.error("Failed to get rate limit info: {}", e)
            return {}


def create_github_client() -> GitHubClient:
    """Create GitHub client from configuration.
    
    Returns:
        Configured GitHub client
        
    Raises:
        ValueError: If configuration is invalid
    """
    config = get_config()
    return GitHubClient(
        access_token=config.github.access_token,
        requests_per_second=config.github.requests_per_second
    )
