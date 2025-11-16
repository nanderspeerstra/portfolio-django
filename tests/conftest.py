"""Pytest configuration and shared fixtures for the entire project."""

import os

import django


def pytest_configure():
    """Configure Django settings for pytest."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "portfolio.settings")
    django.setup()
