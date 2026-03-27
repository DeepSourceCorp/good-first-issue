#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Utility functions for Good First Issue.

This module provides common utility functions for data processing,
file operations, and other shared functionality.
"""

import json
import re
from pathlib import Path
from typing import Dict, List, Any, Optional, Union
from datetime import datetime, timezone

import toml
from loguru import logger


def parse_github_url(url: str) -> Dict[str, str]:
    """Parse GitHub repository URL and extract owner and name.
    
    Args:
        url: GitHub repository URL (various formats supported)
        
    Returns:
        Dictionary with 'owner' and 'name' keys, or empty dict if invalid
        
    Examples:
        >>> parse_github_url("github.com/owner/repo")
        {'owner': 'owner', 'name': 'repo'}
        >>> parse_github_url("https://github.com/owner/repo")
        {'owner': 'owner', 'name': 'repo'}
    """
    # Pattern matches various GitHub URL formats
    pattern = re.compile(r"[http://|https://]?github\.com/(?P<owner>[\w\.-]+)/(?P<name>[\w\.-]+)/?")
    match = pattern.search(url)
    return match.groupdict() if match else {}


def load_json_file(file_path: Union[str, Path]) -> Dict[str, Any]:
    """Load and parse JSON file with error handling.
    
    Args:
        file_path: Path to JSON file
        
    Returns:
        Parsed JSON data
        
    Raises:
        FileNotFoundError: If file doesn't exist
        json.JSONDecodeError: If JSON is malformed
    """
    file_path = Path(file_path)
    
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError as e:
        raise FileNotFoundError(f"JSON file not found: {file_path}") from e
    except json.JSONDecodeError as e:
        raise json.JSONDecodeError(
            f"Invalid JSON format in {file_path}: {e}",
            e.doc,
            e.pos
        ) from e


def load_toml_file(file_path: Union[str, Path]) -> Dict[str, Any]:
    """Load and parse TOML file with error handling.
    
    Args:
        file_path: Path to TOML file
        
    Returns:
        Parsed TOML data
        
    Raises:
        FileNotFoundError: If file doesn't exist
        toml.TomlDecodeError: If TOML is malformed
    """
    file_path = Path(file_path)
    
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return toml.load(f)
    except FileNotFoundError as e:
        raise FileNotFoundError(f"TOML file not found: {file_path}") from e
    except toml.TomlDecodeError as e:
        raise toml.TomlDecodeError(
            f"Invalid TOML format in {file_path}: {e}"
        ) from e


def save_json_file(
    data: Any, 
    file_path: Union[str, Path], 
    indent: int = 2,
    ensure_ascii: bool = False
) -> None:
    """Save data to JSON file with error handling.
    
    Args:
        data: Data to save
        file_path: Output file path
        indent: JSON indentation
        ensure_ascii: Whether to ensure ASCII encoding
        
    Raises:
        OSError: If file cannot be written
        TypeError: If data is not JSON serializable
    """
    file_path = Path(file_path)
    
    # Create parent directories if they don't exist
    file_path.parent.mkdir(parents=True, exist_ok=True)
    
    try:
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=indent, ensure_ascii=ensure_ascii)
    except (OSError, TypeError) as e:
        logger.error("Failed to save JSON file {}: {}", file_path, e)
        raise


def validate_repository_url(url: str) -> bool:
    """Validate GitHub repository URL format with comprehensive patterns.
    
    Supports various GitHub URL formats:
    - github.com/owner/repo
    - https://github.com/owner/repo
    - http://github.com/owner/repo
    - www.github.com/owner/repo
    
    Args:
        url: Repository URL to validate
        
    Returns:
        True if URL appears to be a valid GitHub repository URL
    """
    if not isinstance(url, str) or not url.strip():
        return False
    
    url = url.strip()
    
    # Comprehensive GitHub URL pattern
    # Supports: github.com/owner/repo, https://github.com/owner/repo, etc.
    pattern = re.compile(
        r'^(?:https?://)?(?:www\.)?github\.com/'
        r'(?P<owner>[A-Za-z0-9](?:[A-Za-z0-9-]{0,38}[A-Za-z0-9])?)'
        r'/(?P<name>[A-Za-z0-9_.-]+)'
        r'/?$',
        re.IGNORECASE
    )
    
    match = pattern.match(url)
    if not match:
        return False
    
    # Additional validation for owner and name constraints
    owner = match.group('owner')
    name = match.group('name')
    
    # GitHub username/repository name constraints
    if not (1 <= len(owner) <= 39):
        return False
    
    if not (1 <= len(name) <= 100):
        return False
    
    # Cannot start or end with hyphen
    if owner.startswith('-') or owner.endswith('-'):
        return False
    
    # Repository name cannot be just dots or hyphens
    if name.replace('.', '').replace('-', '').replace('_', '').strip() == '':
        return False
    
    return True


def filter_valid_urls(urls: List[str]) -> List[str]:
    """Filter list of URLs to keep only valid GitHub repository URLs.
    
    Args:
        urls: List of URLs to filter
        
    Returns:
        List of valid GitHub repository URLs
    """
    valid_urls = []
    invalid_count = 0
    
    for url in urls:
        if validate_repository_url(url):
            valid_urls.append(url)
        else:
            invalid_count += 1
    
    if invalid_count > 0:
        logger.warning("Filtered out {} invalid repository URLs", invalid_count)
    
    return valid_urls


def calculate_days_since(timestamp: datetime) -> int:
    """Calculate number of days since given timestamp.
    
    Args:
        timestamp: Timestamp to calculate from
        
    Returns:
        Number of days since timestamp
    """
    now = datetime.now(timezone.utc)
    return (now - timestamp).days


def format_number(number: int) -> str:
    """Format number with appropriate suffix (K, M, B).
    
    Args:
        number: Number to format
        
    Returns:
        Formatted number string
    """
    if number < 1000:
        return str(number)
    elif number < 1000000:
        return f"{number/1000:.1f}K"
    elif number < 1000000000:
        return f"{number/1000000:.1f}M"
    else:
        return f"{number/1000000000:.1f}B"


def safe_get(dictionary: Dict[str, Any], key: str, default: Any = None) -> Any:
    """Safely get value from dictionary with default.
    
    Args:
        dictionary: Dictionary to get value from
        key: Key to retrieve
        default: Default value if key not found
        
    Returns:
        Value from dictionary or default
    """
    return dictionary.get(key, default) if isinstance(dictionary, dict) else default


def truncate_string(text: str, max_length: int, suffix: str = "...") -> str:
    """Truncate string to maximum length with suffix.
    
    Args:
        text: String to truncate
        max_length: Maximum length
        suffix: Suffix to add if truncated
        
    Returns:
        Truncated string
    """
    if len(text) <= max_length:
        return text
    
    return text[:max_length - len(suffix)] + suffix


def ensure_directory_exists(directory: Union[str, Path]) -> None:
    """Ensure directory exists, create if necessary.
    
    Args:
        directory: Directory path to ensure exists
    """
    Path(directory).mkdir(parents=True, exist_ok=True)


def get_file_size(file_path: Union[str, Path]) -> int:
    """Get file size in bytes.
    
    Args:
        file_path: Path to file
        
    Returns:
        File size in bytes
        
    Raises:
        FileNotFoundError: If file doesn't exist
    """
    file_path = Path(file_path)
    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")
    
    return file_path.stat().st_size


def is_recent_activity(last_push: datetime, max_days: int = 90) -> bool:
    """Check if repository has recent activity.
    
    Args:
        last_push: Last push timestamp
        max_days: Maximum days to consider recent
        
    Returns:
        True if activity is recent
    """
    days_since = calculate_days_since(last_push)
    return days_since <= max_days


def clean_text(text: Optional[str]) -> str:
    """Clean and normalize text.
    
    Args:
        text: Text to clean
        
    Returns:
        Cleaned text
    """
    if not text:
        return ""
    
    # Remove extra whitespace and normalize
    return " ".join(text.strip().split())


def validate_language(language: Optional[str]) -> bool:
    """Validate programming language string.
    
    Args:
        language: Language string to validate
        
    Returns:
        True if language appears valid
    """
    if not language or not isinstance(language, str):
        return False
    
    # Basic validation: non-empty, reasonable length, alphanumeric
    cleaned = clean_text(language)
    return (
        len(cleaned) > 0 and 
        len(cleaned) <= 50 and 
        cleaned.replace(" ", "").replace("-", "").replace("+", "").isalnum()
    )
