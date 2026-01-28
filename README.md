# User Data Table Application

This project provides a production-ready, clean-architecture solution for displaying user data stored in a CSV file via a web interface.

---

## Structure

- **Backend (Python, Clean Architecture)**
  - Reads user data from a CSV file.
  - Serves user data via a REST API endpoint (`/api/users`).
  - Configurable via `.env` and `.env.example`.

- **Frontend (React + TypeScript)**
  - Loads user data from the backend API.
  - Displays all user fields in a readable, organized table.
  - Configurable via `.env` and `.env.example`.

---

## Prerequisites

- Python 3.8+
- Node.js (v18+ recommended)
- npm

---

## Backend Setup

1. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

2. Copy `.env.example` to `.env` and configure as needed:
    ```bash
    cp .env.example .env
    ```

3. Run the CSV fetch/export process (required for initial data):
    ```bash
    python src/main.py

    # This will fetch all users from the JSONPlaceholder API and write them to the CSV file
    # specified by OUTPUT_CSV_PATH in your .env file.
    # The backend will serve data from this file.
    ```

4. Start the API server:
    ```bash
    uvicorn src.interfaces.api:app --reload
    # The API will be available at http://localhost:8000/api/users
    ```

---

## Frontend Setup

1. Enter the frontend directory:
    ```bash
    cd frontend
    ```

2. Install dependencies:
    ```bash
    npm install
    ```

3. Copy `.env.example` to `.env` and configure the backend API URL if needed:
    ```bash
    cp .env.example .env
    ```

4. Start the frontend:
    ```bash
    npm start

    # The app will run at http://localhost:3000 and expects the backend API at REACT_APP_API_URL.
    ```

---

## Troubleshooting

- If you see CORS errors, ensure the backend is running and CORS is enabled (see `src/interfaces/api.py`).
- If the table does not load, check that `REACT_APP_API_URL` in `frontend/.env` matches your backend URL and port.
- Ensure the CSV file exists and is readable by the backend.

---

## Configuration

- All environment variables are managed via `.env` and `.env.example` files in both backend and frontend.
- Backend:
  - `USER_API_URL`: Source API for fetching users (used by fetch/export script).
  - `OUTPUT_CSV_PATH`: Path to the CSV file (e.g., `output/users.csv`).
  - `LOG_LEVEL`: Logging level (`DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL`).
- Frontend:
  - `REACT_APP_API_URL`: Backend API base URL.

---

## How to Run End-to-End

1. Ensure Python dependencies are installed (`pip install -r requirements.txt`).
2. Ensure Node.js dependencies are installed in `frontend/` (`npm install`).
3. Copy `.env.example` to `.env` and adjust as needed.
4. Run the backend CSV fetcher: `python src/main.py`
5. Start the backend API: `uvicorn src.interfaces.api:app --reload`
6. Start the frontend: `cd frontend && npm start`
7. Visit [http://localhost:3000](http://localhost:3000) to view the user table.

## Notes

- The backend fetches all user fields from the JSONPlaceholder API and writes them to CSV with no data loss or transformation.
- The CSV output matches the API response structure, including all nested fields.
- All configuration is managed via `.env` files.
- Logging is enabled and configurable via `LOG_LEVEL`.
- The backend and frontend are decoupled and can be deployed independently.

---

## CORS

CORS is enabled in the backend for development. Adjust allowed origins in `src/interfaces/api.py` for production.

---

## Features

- Loads user data from a CSV file.
- Renders all user fields in a table view.
- Organized, readable, and production-ready.
- Clean, modular, and testable codebase.

---

## License

MIT