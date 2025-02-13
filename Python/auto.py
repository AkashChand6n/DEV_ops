import os
import subprocess
import sys

VENV_DIR = "newenv"

def create_virtual_env():
    """Create a virtual environment if it doesn't exist."""
    if not os.path.exists(VENV_DIR):
        print("Creating virtual environment...")
        subprocess.run([sys.executable, "-m", "venv", VENV_DIR])
    else:
        print("Virtual environment already exists.")

def install_requirements():
    """Install required packages from requirements.txt if the file exists, otherwise install Flask."""
    requirements_file = "requirements.txt"
    if os.path.exists(requirements_file):
        print("Installing dependencies from requirements.txt...")
        subprocess.run([os.path.join(VENV_DIR, "Scripts", "pip"), "install", "-r", requirements_file], shell=True)
    else:
        print("No requirements.txt found. Installing Flask directly...")
        # Install Flask directly
        subprocess.run([os.path.join(VENV_DIR, "Scripts", "pip"), "install", "flask"], shell=True)

def run_app():
    """Run the app using the virtual environment's python executable."""
    print("Running the application...")

    # Path to the Python executable in the virtual environment
    python_executable = os.path.join(VENV_DIR, "Scripts", "python.exe") if os.name == "nt" else os.path.join(VENV_DIR, "bin", "python")

    # Run the app (app.py)
    subprocess.run([python_executable, "app.py"], shell=True)

if __name__ == "__main__":
    create_virtual_env()
    install_requirements()
    run_app()
