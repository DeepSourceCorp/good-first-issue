#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Configuration management for Good First Issue.

This module provides centralized configuration management with support
for environment variables, default values, and validation.
"""

import os
from pathlib import Path
from typing import Dict, Any, Optional, List
from dataclasses import dataclass

from loguru import logger


@dataclass
class GitHubConfig:
    """GitHub API configuration."""
    access_token: str
    requests_per_second: float = 1.0
    max_retries: int = 3
    timeout: int = 30


@dataclass
class ProcessingConfig:
    """Data processing configuration."""
    max_concurrency: int = 5
    max_inactivity_days: int = 90
    min_tag_occurrences: int = 3
    issue_limit: int = 10
    issue_state: str = "open"
    issue_sort: str = "created"
    issue_sort_direction: str = "desc"


@dataclass
class FilePaths:
    """File path configuration."""
    repo_data_file: str = "data/repositories.toml"
    labels_file: str = "data/labels.json"
    generated_data_file: str = "data/generated.json"
    tags_data_file: str = "data/tags.json"


@dataclass
class AppConfig:
    """Main application configuration."""
    github: GitHubConfig
    processing: ProcessingConfig
    file_paths: FilePaths
    log_level: str = "INFO"


class ConfigManager:
    """Manages application configuration with validation and defaults."""
    
    def __init__(self) -> None:
        """Initialize configuration manager."""
        self._config: Optional[AppConfig] = None
    
    def load_config(self) -> AppConfig:
        """Load and validate configuration from environment and defaults.
        
        Returns:
            Validated application configuration
            
        Raises:
            ValueError: If required configuration is missing or invalid
        """
        if self._config:
            return self._config
        
        # Load GitHub configuration
        github_token = os.getenv("GH_ACCESS_TOKEN")
        if not github_token:
            raise ValueError(
                "GitHub access token is required. Set GH_ACCESS_TOKEN environment variable."
            )
        
        github_config = GitHubConfig(
            access_token=github_token,
            requests_per_second=float(os.getenv("GH_REQUESTS_PER_SECOND", "1.0")),
            max_retries=int(os.getenv("GH_MAX_RETRIES", "3")),
            timeout=int(os.getenv("GH_TIMEOUT", "30"))
        )
        
        # Load processing configuration
        processing_config = ProcessingConfig(
            max_concurrency=int(os.getenv("MAX_CONCURRENCY", "5")),
            max_inactivity_days=int(os.getenv("MAX_INACTIVITY_DAYS", "90")),
            min_tag_occurrences=int(os.getenv("MIN_TAG_OCCURRENCES", "3")),
            issue_limit=int(os.getenv("ISSUE_LIMIT", "10")),
            issue_state=os.getenv("ISSUE_STATE", "open"),
            issue_sort=os.getenv("ISSUE_SORT", "created"),
            issue_sort_direction=os.getenv("ISSUE_SORT_DIRECTION", "desc")
        )
        
        # Load file paths
        file_paths = FilePaths(
            repo_data_file=os.getenv("REPO_DATA_FILE", "data/repositories.toml"),
            labels_file=os.getenv("LABELS_FILE", "data/labels.json"),
            generated_data_file=os.getenv("GENERATED_DATA_FILE", "data/generated.json"),
            tags_data_file=os.getenv("TAGS_DATA_FILE", "data/tags.json")
        )
        
        # Create main config
        self._config = AppConfig(
            github=github_config,
            processing=processing_config,
            file_paths=file_paths,
            log_level=os.getenv("LOG_LEVEL", "INFO").upper()
        )
        
        # Validate configuration
        self._validate_config(self._config)
        
        logger.info("Configuration loaded successfully")
        return self._config
    
    def _validate_config(self, config: AppConfig) -> None:
        """Validate configuration values.
        
        Args:
            config: Configuration to validate
            
        Raises:
            ValueError: If configuration is invalid
        """
        # Validate GitHub config
        if config.github.requests_per_second <= 0:
            raise ValueError("GitHub requests per second must be positive")
        
        if config.github.max_retries < 0:
            raise ValueError("GitHub max retries must be non-negative")
        
        # Validate processing config
        if config.processing.max_concurrency <= 0:
            raise ValueError("Max concurrency must be positive")
        
        if config.processing.max_inactivity_days < 0:
            raise ValueError("Max inactivity days must be non-negative")
        
        if config.processing.min_tag_occurrences < 1:
            raise ValueError("Min tag occurrences must be at least 1")
        
        # Validate file paths exist
        self._validate_file_paths(config.file_paths)
        
        # Validate log level
        valid_log_levels = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
        if config.log_level not in valid_log_levels:
            raise ValueError(f"Invalid log level: {config.log_level}")
    
    def _validate_file_paths(self, file_paths: FilePaths) -> None:
        """Validate that required input files exist.
        
        Args:
            file_paths: File path configuration
            
        Raises:
            ValueError: If required files don't exist
        """
        required_files = [
            file_paths.repo_data_file,
            file_paths.labels_file
        ]
        
        missing_files = []
        for file_path in required_files:
            if not Path(file_path).exists():
                missing_files.append(file_path)
        
        if missing_files:
            raise ValueError(f"Required files not found: {missing_files}")
    
    def get_config(self) -> AppConfig:
        """Get current configuration.
        
        Returns:
            Current application configuration
        """
        if not self._config:
            return self.load_config()
        return self._config
    
    def reload_config(self) -> AppConfig:
        """Reload configuration from environment.
        
        Returns:
            Freshly loaded configuration
        """
        self._config = None
        return self.load_config()


# Global configuration manager instance
config_manager = ConfigManager()


def get_config() -> AppConfig:
    """Get application configuration.
    
    Returns:
        Current application configuration
    """
    return config_manager.get_config()


def setup_logging(log_level: str = "INFO") -> None:
    """Setup application logging.
    
    Args:
        log_level: Logging level
    """
    logger.remove()  # Remove default handler
    
    # Add console handler with formatting
    logger.add(
        sink=lambda msg: print(msg, end=""),
        level=log_level,
        format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
               "<level>{level: <8}</level> | "
               "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - "
               "<level>{message}</level>",
        colorize=True
    )
    
    # Add file handler for errors
    logger.add(
        "logs/errors.log",
        level="ERROR",
        format="{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {name}:{function}:{line} - {message}",
        rotation="10 MB",
        retention="30 days",
        compression="zip"
    )
    
    logger.info("Logging configured with level: {}", log_level)
