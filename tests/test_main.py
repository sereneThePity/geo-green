"""
Tests for the main module.
"""

from unittest.mock import Mock, patch

import pytest
import requests

# Import the functions we want to test
from geo_green.main import add_numbers, fetch_data


class TestAddNumbers:
    """Tests for the add_numbers function."""

    def test_add_integers(self):
        """Test adding two integers."""
        result = add_numbers(2, 3)
        assert result == 5

    def test_add_floats(self):
        """Test adding two floats."""
        result = add_numbers(1.5, 2.5)
        assert result == 4.0

    def test_add_mixed_types(self):
        """Test adding integer and float."""
        result = add_numbers(2, 1.5)
        assert result == 3.5

    def test_add_negative_numbers(self):
        """Test adding negative numbers."""
        result = add_numbers(-2, 3)
        assert result == 1

    def test_add_zero(self):
        """Test adding with zero."""
        result = add_numbers(5, 0)
        assert result == 5


class TestFetchData:
    """Tests for the fetch_data function."""

    @patch("geo_green.main.requests.get")
    def test_fetch_data_success(self, mock_get):
        """Test successful data fetching."""
        # Mock the response
        mock_response = Mock()
        mock_response.json.return_value = {"login": "octocat", "id": 583231}
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response

        # Test the function
        result = fetch_data("https://api.github.com/users/octocat")

        # Assertions
        assert result == {"login": "octocat", "id": 583231}
        mock_get.assert_called_once_with("https://api.github.com/users/octocat")

    @patch("geo_green.main.requests.get")
    def test_fetch_data_http_error(self, mock_get):
        """Test fetch_data with HTTP error."""
        # Mock the response to raise an exception
        mock_response = Mock()
        mock_response.raise_for_status.side_effect = requests.RequestException(
            "404 Not Found"
        )
        mock_get.return_value = mock_response

        # Test that the function raises the exception
        with pytest.raises(requests.RequestException):
            fetch_data("https://api.github.com/nonexistent")


# Additional test to verify package imports work correctly
def test_package_import():
    """Test that the package can be imported correctly."""
    import geo_green

    assert hasattr(geo_green, "add_numbers")
    assert geo_green.__version__ == "0.1.0"
