#!/bin/bash

# Directory for the virtual environment
VENV_DIR="newenv"

# Create virtual environment if it doesn't exist
if [ ! -d "$VENV_DIR" ]; then
    echo "Creating virtual environment..."
    python -m venv "$VENV_DIR"
else
    echo "Virtual environment already exists."
fi

# Activate the virtual environment (Windows-specific)
if [ -f "$VENV_DIR/Scripts/activate.bat" ]; then
    echo "Activating virtual environment..."
    source "$VENV_DIR/Scripts/activate.bat"
else
    echo "Error: Could not find activation script."
    exit 1
fi

# Install Flask if requirements.txt doesn't exist
if [ ! -f "requirements.txt" ]; then
    echo "Installing Flask..."
    pip install flask
else
    echo "Installing dependencies from requirements.txt..."
    pip install -r requirements.txt
fi

# Run the application (Ensure that app.py exists in the current directory)
if [ -f "app.py" ]; then
    echo "Running the application..."
    python app.py
else
    echo "Error: app.py not found in the current directory."
    exit 1
fi
