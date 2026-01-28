import requests
from typing import List, Dict, Any
from domain.models import User


class UserRepository:
    """
    Repository for fetching users from the JSONPlaceholder API.
    """

    def __init__(self, api_url: str):
        self.api_url = api_url

    def fetch_all_users(self) -> List[User]:
        response = requests.get(self.api_url, timeout=10)
        response.raise_for_status()
        users_data = response.json()
        if not isinstance(users_data, list):
            raise ValueError("API response is not a list of users")
        return [User.from_dict(user) for user in users_data]

    def fetch_all_users_raw(self) -> List[Dict[str, Any]]:
        """
        Fetches all users as raw dictionaries (for CSV writing).
        """
        response = requests.get(self.api_url, timeout=10)
        response.raise_for_status()
        users_data = response.json()
        if not isinstance(users_data, list):
            raise ValueError("API response is not a list of users")
        return users_data