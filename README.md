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

3. Run the CSV fetch/export process (if needed):
    ```bash
    python src/main.py
    ```

4. Start the API server:
    ```bash
    uvicorn src.interfaces.api:app --reload
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
    ```

---

## Configuration

- All environment variables are managed via `.env` and `.env.example` files in both backend and frontend.
- Backend:
  - `USER_API_URL`: Source API for fetching users (used by fetch/export script).
  - `OUTPUT_CSV_PATH`: Path to the CSV file.
  - `LOG_LEVEL`: Logging level.
- Frontend:
  - `REACT_APP_API_URL`: Backend API base URL.

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