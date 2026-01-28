import logging
import sys
import os

# Ensure src/ is in the Python path for absolute imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from config.config import Config
from infrastructure.repository.user_repository import UserRepository
from application.services.user_service import UserService
from infrastructure.csv.csv_writer import CSVWriter

def setup_logging(log_level: str):
    logging.basicConfig(
        level=getattr(logging, log_level.upper(), logging.INFO),
        format="%(asctime)s [%(levelname)s] %(message)s"
    )

def main():
    # Load configuration
    config = Config()
    setup_logging(config.LOG_LEVEL)
    logging.info("Starting user fetch and CSV export process.")

    # Initialize repository and service
    user_repository = UserRepository(config.USER_API_URL)
    user_service = UserService(user_repository)

    try:
        users = user_service.get_all_users()
        logging.info(f"Fetched {len(users)} users from API.")
        CSVWriter.write_users_to_csv(users, config.OUTPUT_CSV_PATH)
        logging.info(f"User data written to CSV at {config.OUTPUT_CSV_PATH}")
    except Exception as e:
        logging.error(f"An error occurred: {e}", exc_info=True)

if __name__ == "__main__":
    main()