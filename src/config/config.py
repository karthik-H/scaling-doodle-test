import os
from dotenv import load_dotenv

class Config:
    """
    Loads configuration from .env file and environment variables.
    """
    def __init__(self, env_path: str = ".env"):
        load_dotenv(env_path)
        self.USER_API_URL = os.getenv("USER_API_URL")
        self.OUTPUT_CSV_PATH = os.getenv("OUTPUT_CSV_PATH")
        self.LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

        if not self.USER_API_URL:
            raise ValueError("USER_API_URL is not set in environment variables or .env file")
        if not self.OUTPUT_CSV_PATH:
            raise ValueError("OUTPUT_CSV_PATH is not set in environment variables or .env file")