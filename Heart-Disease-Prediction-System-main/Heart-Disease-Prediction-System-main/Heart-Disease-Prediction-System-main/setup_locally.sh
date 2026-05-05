#!/bin/bash

echo "Starting Local Deployment for Heart Disease Prediction System..."

# 1. Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# 2. Run migrations
echo "Running migrations..."
python3 manage.py migrate

# 3. Initialize data
echo "Initializing admin and datasets..."
python3 init_db.py

# 4. Run server
echo "Deployment complete. Starting server on http://127.0.0.1:8001"
python3 manage.py runserver 8001
