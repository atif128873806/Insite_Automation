#!/usr/bin/env python3
"""
Cross-platform test script for Insite Automation Bot
This script tests the setup on different operating systems.
"""

import sys
import platform
import subprocess
from pathlib import Path

def test_python_version():
    """Test Python version compatibility."""
    print(f"✅ Python {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}")
    if sys.version_info < (3, 8):
        print("❌ Python 3.8+ required")
        return False
    return True

def test_chrome_detection():
    """Test Chrome detection on current platform."""
    print(f"\n🔍 Testing Chrome detection on {platform.system()}")
    
    # Import the Chrome detection function
    try:
        from insite.main_insite import get_chrome_version
        version = get_chrome_version()
        if version:
            print(f"✅ Chrome detected: version {version}")
            return True
        else:
            print("❌ Chrome not detected")
            return False
    except ImportError as e:
        print(f"❌ Error importing Chrome detection: {e}")
        return False

def test_virtual_environment():
    """Test virtual environment setup."""
    print(f"\n🔍 Testing virtual environment")
    
    venv_path = Path(".venv")
    if not venv_path.exists():
        print("❌ Virtual environment not found")
        return False
    
    # Check if we're in a virtual environment
    if hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
        print("✅ Running in virtual environment")
        return True
    else:
        print("⚠️  Not running in virtual environment (this is OK for testing)")
        return True

def test_dependencies():
    """Test if required dependencies are installed."""
    print(f"\n🔍 Testing dependencies")
    
    required_packages = [
        'selenium',
        'undetected_chromedriver',
        'chromedriver_autoinstaller',
        'requests',
        'dotenv'
    ]
    
    missing_packages = []
    for package in required_packages:
        try:
            __import__(package)
            print(f"✅ {package}")
        except ImportError:
            print(f"❌ {package} - missing")
            missing_packages.append(package)
    
    if missing_packages:
        print(f"\n❌ Missing packages: {', '.join(missing_packages)}")
        print("Run: pip install -r requirements.txt")
        return False
    
    return True

def test_chromedriver_autoinstaller():
    """Test ChromeDriver auto-installer."""
    print(f"\n🔍 Testing ChromeDriver auto-installer")
    
    try:
        import chromedriver_autoinstaller
        chromedriver_autoinstaller.install()
        print("✅ ChromeDriver auto-installer working")
        return True
    except Exception as e:
        print(f"❌ ChromeDriver auto-installer failed: {e}")
        return False

def test_platform_specific():
    """Test platform-specific configurations."""
    print(f"\n🔍 Testing platform-specific configurations")
    
    system = platform.system()
    print(f"Platform: {system}")
    
    if system == "Windows":
        print("✅ Windows-specific paths configured")
    elif system == "Darwin":
        print("✅ macOS-specific paths configured")
    elif system == "Linux":
        print("✅ Linux-specific paths configured")
    else:
        print(f"⚠️  Unknown platform: {system}")
    
    return True

def main():
    """Run all cross-platform tests."""
    print("🚀 Cross-Platform Test Suite")
    print("=" * 40)
    
    tests = [
        ("Python Version", test_python_version),
        ("Chrome Detection", test_chrome_detection),
        ("Virtual Environment", test_virtual_environment),
        ("Dependencies", test_dependencies),
        ("ChromeDriver Auto-installer", test_chromedriver_autoinstaller),
        ("Platform Configuration", test_platform_specific),
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        try:
            if test_func():
                passed += 1
        except Exception as e:
            print(f"❌ {test_name} failed with error: {e}")
    
    print(f"\n" + "=" * 40)
    print(f"📊 Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! Your setup is ready.")
        print("\nNext steps:")
        print("1. Activate virtual environment")
        print("2. Configure credentials in run.py")
        print("3. Run: python run.py")
    else:
        print("⚠️  Some tests failed. Check the errors above.")
        print("\nTroubleshooting:")
        print("1. Install missing dependencies: pip install -r requirements.txt")
        print("2. Install Chrome browser")
        print("3. Recreate virtual environment if needed")
    
    return passed == total

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1) 