"""Tests for portfolio app utilities."""

from unittest.mock import patch

from portfolio.version import get_version


class TestVersionModule:
    """Tests for the version module."""

    def test_get_version_from_manifest(self):
        """Test getting version from manifest file."""
        mock_content = '{"."  : "1.2.3"}'
        with patch(
            "pathlib.Path.read_text",
            return_value=mock_content,
        ):
            version = get_version()
            assert version == "1.2.3"

    def test_get_version_default_on_missing_manifest(self):
        """Test that default version is returned when manifest is missing."""
        with patch(
            "pathlib.Path.read_text",
            side_effect=FileNotFoundError(),
        ):
            version = get_version()
            assert version == "dev"

    def test_get_version_default_on_missing_key(self):
        """Test that default version is returned when key is missing."""
        mock_content = '{"other_key": "value"}'
        with patch(
            "pathlib.Path.read_text",
            return_value=mock_content,
        ):
            version = get_version()
            assert version == "dev"
