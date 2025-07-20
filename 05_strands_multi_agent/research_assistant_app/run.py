#!/usr/bin/env python3
"""
Run script for the Research Assistant Streamlit app.
This script checks for dependencies and launches the Streamlit app.
"""

import os
import sys
import subprocess

def check_dependencies():
    """Check if all required packages are installed."""
    try:
        import streamlit
        import strands
        import dotenv
        return True
    except ImportError as e:
        print(f"Missing dependency: {e}")
        print("Please install required packages: pip install -r requirements.txt")
        return False

def check_env_file():
    """Check if .env file exists, create from example if not."""
    if not os.path.exists(".env") and os.path.exists(".env.example"):
        print("No .env file found. Creating from .env.example...")
        with open(".env.example", "r") as example:
            with open(".env", "w") as env_file:
                env_file.write(example.read())
        print("Created .env file. Please edit it with your API keys.")
        return False
    return True

def main():
    """Main function to run the app."""
    if not check_dependencies():
        return 1
    
    if not check_env_file():
        print("Please edit the .env file with your API keys before running the app.")
        return 1
    
    print("Starting Research Assistant Streamlit app...")
    subprocess.run(["streamlit", "run", "app.py"])
    return 0

if __name__ == "__main__":
    sys.exit(main())