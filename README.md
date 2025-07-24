# Insite Bot

A Selenium-based automation bot for interacting with the Insite platform.

## Project Structure

```
insiteBot/
├── insite/                  # Main package
│   ├── __init__.py
│   ├── main_insite.py      # Main bot class
│   ├── login.py            # Login functionality
│   ├── email_verifier.py   # Email verification
│   ├── insite_url.py       # URL constants
│   └── insite_utility/     # Utility modules
│       └── interaction.py  # Interaction utilities
├── .venv/                  # Virtual environment (ignored in .gitignore)
├── requirements.txt        # Project dependencies
├── run.py                  # Main script to run the bot
└── README.md               # This file
```

## Setup

1. **Create a virtual environment (recommended):**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the bot:**
   ```bash
   python run.py
   ```

## Configuration

Update the following in the code as needed:
- Email and password in `run.py`
- Any URL constants in `insite/insite_url.py`

## Requirements

- Python 3.8+
- Google Chrome browser installed
- ChromeDriver (automatically managed by undetected-chromedriver)
