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
│       ├── bodynavigation.py
│       ├── contact.py
│       └── interaction.py  # Interaction utilities
├── .venv/                  # Virtual environment (ignored in .gitignore)
├── requirements.txt        # Project dependencies
├── run.py                  # Main script to run the bot
└── README.md               # This file
```

## Prerequisites

Before setting up the project, ensure you have:

1. **Python 3.8+** installed on your system
2. **Google Chrome browser** installed
3. **Git** (for cloning the repository)

### Installing Chrome by Platform

**Windows:**
- Download from: https://www.google.com/chrome/
- Or install via Chocolatey: `choco install googlechrome`

**macOS:**
- Using Homebrew: `brew install --cask google-chrome`
- Or download from: https://www.google.com/chrome/

**Linux:**
- Ubuntu/Debian: `sudo apt install google-chrome-stable`
- Arch Linux: `sudo pacman -S google-chrome`
- Or download from: https://www.google.com/chrome/

## Setup Instructions

### Quick Start (Recommended)

For a quick setup, use the automated setup script:

```bash
git clone <repository-url>
cd Insite_Automation
python setup.py
```

This will automatically:
- Check prerequisites (Python, Chrome)
- Create virtual environment
- Install dependencies
- Create configuration files
- Show next steps

### Manual Setup

### 1. Clone the Repository

```bash
git clone <repository-url>
cd Insite_Automation
```

### 2. Create and Activate Virtual Environment

**On Linux/macOS:**
```bash
python -m venv .venv
source .venv/bin/activate
```

**On Windows:**
```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```



**Note:** The current implementation uses hardcoded values for Mailosaur, but you can modify `insite/email_verifier.py` to use environment variables if needed.

### 5. Configure Credentials (Required)

Before running the bot, you need to update the credentials in the code:

#### For Login Functionality:
Edit `run.py` line 81 and update the email and password:
```python
login_flow.sign_text("your_email@example.com", "your_password")
```

#### For Email Verification:
The email verification uses Mailosaur for temporary email addresses. The current setup uses:
- API Key: `WeldgqcntKOUdJbW8qWfQLTVFKrwctdu`
- Server ID: `wavlgmb1`

If you want to use your own Mailosaur account, update these values in `insite/email_verifier.py` lines 33-34.

### 6. Test Your Setup (Optional)

Run the cross-platform test suite to verify everything is working:

```bash
python test_cross_platform.py
```

### 7. Run the Bot

```bash
python run.py
```

## Available Modes

The bot supports the following modes:

1. **Registration** - Complete registration process with email verification
2. **Login** - Login to existing account
3. **Dashboard Navigation** - Navigate through dashboard elements
4. **Body Navigation** - Navigate through body content
5. **Contact Us (Form)** - Fill out contact form

## Troubleshooting

### Chrome/ChromeDriver Issues

If you encounter ChromeDriver version mismatch errors:

1. **Update Chrome to the latest version**
2. **Clear Chrome cache and cookies**
3. **Restart your system**
4. **Reinstall dependencies:**
   ```bash
   pip install --upgrade undetected-chromedriver webdriver-manager chromedriver-autoinstaller
   ```

### Common Issues

1. **"Chrome not found" error:**
   - Ensure Google Chrome is installed
   - **Windows**: Download from https://www.google.com/chrome/
   - **macOS**: `brew install --cask google-chrome` or download from website
   - **Linux**: `sudo apt install google-chrome-stable` (Ubuntu/Debian) or `sudo pacman -S google-chrome` (Arch)

2. **Permission errors:**
   - Make sure you have write permissions in the project directory
   - Try running with elevated privileges if needed
   - **Windows**: Run as Administrator if needed
   - **macOS/Linux**: Check file permissions with `ls -la`

3. **Virtual environment issues:**
   - Ensure you're in the correct virtual environment
   - Recreate the virtual environment if needed:
     ```bash
     # Linux/macOS
     rm -rf .venv
     python -m venv .venv
     source .venv/bin/activate
     pip install -r requirements.txt
     
     # Windows
     rmdir /s .venv
     python -m venv .venv
     .venv\Scripts\activate
     pip install -r requirements.txt
     ```

4. **Platform-specific issues:**
   - **Windows**: Ensure Chrome is in PATH or use full path
   - **macOS**: May need to allow Chrome in Security & Privacy settings
   - **Linux**: May need to install additional dependencies for GUI automation

## Requirements

- Python 3.8+
- Google Chrome browser installed
- ChromeDriver (automatically managed by undetected-chromedriver)
- Internet connection for web automation

## Dependencies

The main dependencies are automatically installed via `requirements.txt`:

- `selenium>=4.15.2` - Web automation
- `undetected-chromedriver>=3.5.4` - Undetected Chrome automation
- `chromedriver-autoinstaller>=0.6.0` - Automatic ChromeDriver management
- `mailosaur==7.19.0` - Email verification service
- `pyautogui>=0.9.54` - GUI automation
- `requests>=2.31.0` - HTTP requests
- `webdriver-manager>=4.0.1` - WebDriver management

## Notes

- The bot uses undetected-chromedriver to avoid detection
- ChromeDriver is automatically installed and managed
- Email verification uses Mailosaur for temporary email addresses
- All interactions include random delays to simulate human behavior
- The bot supports multiple pricing plans (Beta, Personal, Team)

## Cross-Platform Testing

The bot has been tested and works on:

- ✅ **Linux** (Ubuntu, Arch Linux, etc.)
- ✅ **Windows** (Windows 10/11)
- ✅ **macOS** (Catalina and later)

### Platform-Specific Notes

**Windows:**
- Chrome is typically installed in `C:\Program Files\Google\Chrome\Application\`
- May need to run as Administrator for some operations
- Use backslashes in paths: `.venv\Scripts\activate`

**macOS:**
- Chrome is typically installed in `/Applications/Google Chrome.app/`
- May need to allow Chrome in Security & Privacy settings
- Use Homebrew for easy installation: `brew install --cask google-chrome`

**Linux:**
- Chrome binary names vary by distribution
- May need additional packages for GUI automation
- Use package manager for installation (apt, pacman, etc.)

## Support

If you encounter issues:

1. Check the troubleshooting section above
2. Ensure all prerequisites are met
3. Verify your internet connection
4. Check that the target website is accessible
5. Check platform-specific notes above
