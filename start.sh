#!/bin/bash

# Start the frontend on port 8080
cd ./frontend
echo "Starting frontend..."
python3 -m http.server 8080 &

# Start the server on port 5000
cd ../backend
echo "Starting backend..."
python3 server.py