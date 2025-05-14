# Flask + PostgreSQL Web App

This is a simple Flask web application with PostgreSQL as the database. It supports basic CRUD operations for managing users.

## Features

- Add a new user
- View all users
- Update user information
- Delete a user
- HTML-based UI using Flask templates

## Requirements

- Python 3.x
- PostgreSQL
- `pip install Flask psycopg2-binary`

## Setup Instructions

### 1. Create the database and table

Run the SQL script:

```bash
psql -U your_db_user -d your_db_name -f schema.sql
```

### 2. Run the app

```bash
export DB_HOST=localhost
export DB_NAME=your_db_name
export DB_USER=your_db_user
export DB_PASSWORD=your_db_password

python app.py
```

### 3. Access in browser

Open [http://localhost:5000](http://localhost:5000) to view the app.
