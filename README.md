# User Fetcher Application

This application fetches user information from the [JSONPlaceholder API](https://jsonplaceholder.typicode.com/users) and stores it in a CSV file, capturing all user fields and maintaining data integrity.

---

## Features

- Fetches all user records and fields from the API.
- Stores user data in a CSV file, preserving the API response structure.
- Clean, modular, and testable codebase following clean/layered architecture.
- Environment configuration via `.env` file.
- Logging and error handling for production readiness.

---

## Folder Structure

```
src/
  ├── application/
  │     └── services/
  ├── config/
  ├── domain/
  ├── infrastructure/
  │     ├── csv/
  │     └── repository/
  └── main.py
.env
.env.example
.gitignore
README.md
```

---

## Setup Instructions

1. **Clone the repository**

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

   Required packages:
   - `requests`
   - `python-dotenv`

   *(If `requirements.txt` is not present, install manually:)*

   ```bash
   pip install requests python-dotenv
   ```

3. **Configure environment variables**

   - Copy `.env.example` to `.env` and adjust values if needed:

     ```bash
     cp .env.example .env
     ```

   - Ensure the following variables are set in `.env`:

     ```
     USER_API_URL=https://jsonplaceholder.typicode.com/users
     OUTPUT_CSV_PATH=output/users.csv
     LOG_LEVEL=INFO
     ```

4. **Run the application**

   ```bash
   python src/main.py
   ```

   The CSV file will be generated at the path specified by `OUTPUT_CSV_PATH`.

---

## Notes

- The CSV output will include all fields from the API, including nested fields (e.g., address and company) flattened with dot notation.
- Logging output will be shown in the console.
- Ensure you have Python 3.7+ installed.

---

## Environment Variables

See `.env.example` for all required variables.

---

## License

MIT