from typing import List, Dict, Any
from infrastructure.repository.user_repository import UserRepository


class UserService:
    """
    Service layer for user-related business logic.
    """

    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def get_all_users(self) -> List[Dict[str, Any]]:
        """
        Fetch all users as raw dictionaries for CSV writing.
        """
        return self.user_repository.fetch_all_users_raw()