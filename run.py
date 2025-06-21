#!/usr/bin/env python3
"""
Simple script to run the Flask server
"""
import subprocess
import sys
import os

def install_requirements():
    """Install required packages"""
    print("📦 Installing requirements...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])

def run_server():
    """Run the Flask server"""
    print("🚀 Starting server...")
    os.system("python app.py")

if __name__ == "__main__":
    try:
        install_requirements()
        run_server()
    except KeyboardInterrupt:
        print("\n👋 Server stopped.")
    except Exception as e:
        print(f"❌ Error: {e}")