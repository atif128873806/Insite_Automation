#!/usr/bin/env python3
"""
Setup script for Insite Automation Bot
This script automates the initial setup process for new users.
"""

import os
import sys
import subprocess
import platform
from pathlib import Path

def check_python_version():
    """Check if Python version is compatible."""
    if sys.version_info < (3, 8):
        print("❌ Error: Python 3.8+ is required")
        print(f"Current version: {sys.version}")
        return False
    print(f"✅ Python {sys.version_info.major}.{sys.version_info.minor} detected")
    return True

def check_chrome():
    """Check if Chrome is installed."""
    chrome_paths = [
        'google-chrome-stable',
        'google-chrome',
        'chromium',
        'chrome'
    ]
    
    for chrome in chrome_paths:
        try:
            result = subprocess.run([chrome, '--version'], 
                                  capture_output=True, text=True)
            if result.returncode == 0:
                print(f"✅ Chrome detected: {result.stdout.strip()}")
                return True
        except FileNotFoundError:
            continue
    
    print("❌ Chrome not found!")
    print("Please install Google Chrome:")
    if platform.system() == "Linux":
        if os.path.exists("/etc/arch-release"):
            print("  sudo pacman -S google-chrome")
        elif os.path.exists("/etc/debian_version"):
            print("  sudo apt install google-chrome-stable")
        else:
            print("  Install Google Chrome from https://www.google.com/chrome/")
    elif platform.system() == "Darwin":  # macOS
        print("  Option 1: Using Homebrew:")
        print("    brew install --cask google-chrome")
        print("  Option 2: Download from:")
        print("    https://www.google.com/chrome/")
    elif platform.system() == "Windows":
        print("  Download from: https://www.google.com/chrome/")
        print("  Or install via Chocolatey:")
        print("    choco install googlechrome")
    else:
        print("  Download from https://www.google.com/chrome/")
    return False

def create_venv():
    """Create virtual environment."""
    venv_path = Path(".venv")
    if venv_path.exists():
        print("✅ Virtual environment already exists")
        return True
    
    print("Creating virtual environment...")
    try:
        subprocess.run([sys.executable, "-m", "venv", ".venv"], check=True)
        print("✅ Virtual environment created")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to create virtual environment: {e}")
        return False

def install_dependencies():
    """Install Python dependencies."""
    print("Installing dependencies...")
    
    # Determine the correct pip path
    if platform.system() == "Windows":
        pip_path = ".venv\\Scripts\\pip"
    else:
        pip_path = ".venv/bin/pip"
    
    try:
        subprocess.run([pip_path, "install", "-r", "requirements.txt"], check=True)
        print("✅ Dependencies installed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install dependencies: {e}")
        return False

def create_env_file():
    """Create .env file template."""
    env_path = Path(".env")
    if env_path.exists():
        print("✅ .env file already exists")
        return True
    
    print("Creating .env file template...")
    env_content = """# Mailosaur Configuration (Optional)
# Uncomment and update these values if you want to use your own Mailosaur account
# MAILOSAUR_API_KEY=your_api_key_here
# MAILOSAUR_SERVER_ID=your_server_id_here

# Note: The current implementation uses hardcoded values
# If you want to use environment variables, update insite/email_verifier.py
"""
    
    try:
        with open(".env", "w") as f:
            f.write(env_content)
        print("✅ .env file created")
        return True
    except Exception as e:
        print(f"❌ Failed to create .env file: {e}")
        return False

def show_next_steps():
    """Show next steps for the user."""
    print("\n" + "="*50)
    print("🎉 Setup completed successfully!")
    print("="*50)
    print("\nNext steps:")
    print("1. Activate the virtual environment:")
    if platform.system() == "Windows":
        print("   .venv\\Scripts\\activate")
    else:
        print("   source .venv/bin/activate")
    
    print("\n2. Configure your credentials:")
    print("   - Edit run.py line 81 to update login credentials")
    print("   - Update email_verifier.py if you want to use your own Mailosaur account")
    
    print("\n3. Run the bot:")
    print("   python run.py")
    
    print("\n4. Choose your desired mode:")
    print("   1 - Registration")
    print("   2 - Login")
    print("   3 - Dashboard Navigation")
    print("   4 - Body Navigation")
    print("   5 - Contact Us (Form)")
    
    print("\nFor more information, see README.md")

def main():
    """Main setup function."""
    print("🚀 Insite Automation Bot Setup")
    print("="*40)
    
    # Check prerequisites
    if not check_python_version():
        sys.exit(1)
    
    if not check_chrome():
        print("\n⚠️  Please install Chrome and run this script again")
        sys.exit(1)
    
    # Create virtual environment
    if not create_venv():
        sys.exit(1)
    
    # Install dependencies
    if not install_dependencies():
        sys.exit(1)
    
    # Create .env file
    create_env_file()
    
    # Show next steps
    show_next_steps()

if __name__ == "__main__":
    main() 