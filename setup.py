#!/usr/bin/env python3
"""
Setup script for HotBeansWeb Python backend.
This script installs the required dependencies and initializes the users.json file.
"""

import sys
import subprocess
import json
import os

def main():
    print("Setting up HotBeansWeb Python backend...")
    
    # Check Python version
    python_version = sys.version_info
    if python_version.major < 3 or (python_version.major == 3 and python_version.minor < 6):
        print("Error: Python 3.6 or higher is required")
        sys.exit(1)
    
    # Install required packages
    print("Installing required packages...")
    try:
        subprocess.run([sys.executable, "-m", "pip", "install", "flask", "flask-cors"], check=True)
        print("Packages installed successfully")
    except subprocess.CalledProcessError as e:
        print(f"Error installing packages: {e}")
        sys.exit(1)
    
    # Create 'data' directory and initialize users.json
    data_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')
    os.makedirs(data_dir, exist_ok=True)
    users_file = os.path.join(data_dir, 'users.json')
    
    print("Initializing users.json in the 'data' directory...")
    if not os.path.exists(users_file):
        with open(users_file, "w") as f:
            json.dump([], f)
        print("users.json created")
    else:
        print("users.json already exists")
    
    print("\nSetup complete!")
    print("\nTo start the server, run:")
    print("    python server.py")
    print("\nTo use the authentication system:")
    print("1. Move your HTML/JS/CSS files into the 'static' folder.")
    print("2. Use VSCode Live Server (or any server) to serve the 'static' folder (http://127.0.0.1:5500)")
    print("3. Run the Python server in a terminal (http://127.0.0.1:5000)")
    print("4. Go to http://127.0.0.1:5500/signin.html to create an account")
    print("5. Go to http://127.0.0.1:5500/login.html to log in")

if __name__ == "__main__":
    main()
