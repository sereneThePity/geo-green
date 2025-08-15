"""
Main module for package.

This module contains the core functionality of the application.
"""

import requests
from typing import Union


def add_numbers(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Adds two numbers together.
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        The sum of a and b
        
    Example:
        >>> add_numbers(2, 3)
        5
        >>> add_numbers(1.5, 2.5)
        4.0
    """
    return a + b


def fetch_data(url: str) -> dict:
    """
    Fetches data from a URL and returns it as JSON.
    
    Args:
        url (str): The URL to fetch data from
        
    Returns:
        dict: The JSON response as a dictionary
        
    Raises:
        requests.RequestException: If the request fails
        
    Example:
        >>> data = fetch_data("https://api.github.com/users/octocat")
        >>> print(data["login"])
        octocat
    """
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


if __name__ == "__main__":
    # Example usage when running the module directly
    print(f"2 + 3 = {add_numbers(2, 3)}")
    
    # Example API call (commented out to avoid making requests during testing)
    # try:
    #     github_data = fetch_data("https://api.github.com/users/octocat")
    #     print(f"GitHub user: {github_data['login']}")
    # except requests.RequestException as e:
    #     print(f"Failed to fetch data: {e}")