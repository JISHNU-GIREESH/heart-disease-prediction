# Heart Disease Prediction System - Windows Setup Guide

This guide will help you set up and run the Heart Disease Prediction System on a Windows machine.

## Prerequisites

1.  **Python 3.10+**: Download and install from [python.org](https://www.python.org/downloads/).
    *   **IMPORTANT**: During installation, make sure to check the box **"Add Python to PATH"**.
2.  **Git** (Optional): To clone the repository.

## Installation Steps

### 1. Extract the Project
If you haven't already, extract the ZIP file to a folder (e.g., `C:\Heart-Disease-System`).

### 2. Open Command Prompt
*   Press `Win + R`, type `cmd`, and press Enter.
*   Navigate to your project directory.

### 3. Create a Virtual Environment (Recommended)
This keeps the project dependencies separate from your system.
```cmd
python -m venv venv
venv\Scripts\activate
```

### 4. Install Dependencies
```cmd
pip install -r requirements.txt
```

### 5. Run Database Migrations
This prepares the database structure.
```cmd
python manage.py migrate
```

### 6. Initialize Data (Admin & Dataset)
Run the initialization script to set up the default admin and the heart dataset.
```cmd
python init_db.py
```
*   **Username**: `admin`
*   **Password**: `admin123`

### 7. Start the Server
```cmd
python manage.py runserver
```

### 8. Access the App
Open your browser and go to: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## Troubleshooting

*   **"python is not recognized"**: You forgot to "Add Python to PATH" during installation. Re-install or add it manually to Environment Variables.
*   **Port already in use**: If 8000 is busy, run `python manage.py runserver 8001`.
*   **Missing CSV Error**: Ensure the `media/heart.csv` file exists in the project folder.

---

## Login Details
*   **Admin**: `admin` / `admin123`
*   **User/Doctor**: Use the "Register" link on the home page to create a new account.
