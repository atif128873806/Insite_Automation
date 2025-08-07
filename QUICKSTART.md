# Quick Start Guide

Get the Insite Automation Bot running in 5 minutes!

## 🚀 Quick Setup

### Option 1: Automated Setup (Recommended)

```bash
# Clone the repository
git clone <repository-url>
cd Insite_Automation

# Run the automated setup
python setup.py
```

### Option 2: Manual Setup

```bash
# Clone the repository
git clone <repository-url>
cd Insite_Automation

# Create virtual environment
python -m venv .venv

# Activate virtual environment
# On Linux/macOS:
source .venv/bin/activate
# On Windows:
.venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```



## 🎯 Run the Bot

```bash
# Activate virtual environment (if not already activated)
source .venv/bin/activate

# Run the bot
python run.py
```

## 📋 Available Modes

Choose from these automation modes:

- **1** - Registration (Complete signup with email verification)
- **2** - Login (Login to existing account)
- **3** - Dashboard Navigation (Navigate dashboard elements)
- **4** - Body Navigation (Navigate body content)
- **5** - Contact Us (Fill contact form)

## 🔧 Troubleshooting

### Chrome Issues
- **Chrome not found**: Install Google Chrome
- **Version mismatch**: The bot automatically handles ChromeDriver versions

### Python Issues
- **Python version**: Requires Python 3.8+
- **Dependencies**: Run `pip install -r requirements.txt`

### Permission Issues
- **Virtual environment**: Ensure you're in the correct venv
- **File permissions**: Check write permissions in project directory

## 📖 Full Documentation

For detailed setup instructions and troubleshooting, see [README.md](README.md).

## 🆘 Need Help?

1. Check the troubleshooting section in README.md
2. Ensure all prerequisites are met
3. Verify your internet connection
4. Check that the target website is accessible 