# User Data Table Frontend

This is the React frontend for displaying user data from the backend CSV API.

## Prerequisites

- Node.js (v18+ recommended)
- Backend API running (see root README for backend instructions)

## Setup

```bash
cd frontend
cp .env.example .env
npm install
```

## Running the App

```bash
npm start
```

The app will run at [http://localhost:3000](http://localhost:3000) and expects the backend API at the URL specified in `.env` (`REACT_APP_API_URL`).

## Configuration

- `.env` contains the backend API URL. Adjust as needed for your environment.

## Environment Variables

- `REACT_APP_API_URL`: The backend API base URL (e.g., `http://localhost:8000`). This is loaded from `.env` and `.env.example`.

## Error Handling & Logging

- The UI displays loading and error states if the backend is unreachable or returns an error.
- All API errors are surfaced in the UI for visibility.

## Production Usage

- Ensure the backend is running and accessible at the URL specified in `.env`.
- For production deployments, configure CORS and API URLs appropriately.

## Linting & Code Quality

- Run `npm run lint` to check for code style issues.
- All code follows official React and TypeScript style guides.

## Features

- Loads user data from the backend `/api/users` endpoint.
- Displays all user fields in a readable, organized table.
- Handles loading and error states.
