import os
import csv
import logging
from typing import List, Dict, Any
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

# Load environment variables
load_dotenv(os.getenv("ENV_PATH", ".env"))
CSV_PATH = os.getenv("OUTPUT_CSV_PATH", "users.csv")

app = FastAPI(
    title="User Data API",
    description="API to serve user data from CSV for frontend table view",
    version="1.0.0"
)

# Allow CORS for frontend (adjust origins as needed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, restrict this!
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def read_users_from_csv(csv_path: str) -> List[Dict[str, Any]]:
    if not os.path.exists(csv_path):
        logging.error(f"CSV file not found at {csv_path}")
        raise FileNotFoundError(f"CSV file not found at {csv_path}")
    with open(csv_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        return [row for row in reader]

@app.get("/api/users", response_model=List[Dict[str, Any]])
def get_users():
    """
    Returns all users from the CSV file.
    """
    try:
        users = read_users_from_csv(CSV_PATH)
        return users
    except FileNotFoundError as e:
        logging.error(str(e))
        raise HTTPException(status_code=404, detail="User data not found")
    except Exception as e:
        logging.error(f"Error reading users from CSV: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail="Internal server error")