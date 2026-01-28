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

## Features

- Loads user data from the backend `/api/users` endpoint.
- Displays all user fields in a readable, organized table.
- Handles loading and error states.
