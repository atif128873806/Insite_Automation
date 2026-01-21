import os
import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import subprocess
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

main_directory = os.path.join(sys.path[0])

def open_chrome_profile():
    subprocess.Popen(
        [
            "google-chrome-stable",   # or "chromium"
            "--remote-debugging-port=8989",
            "--user-data-dir=" + os.path.join(main_directory, "chrome_profile"),
            "--disable-background-networking",
            "--disable-sync",
            "--disable-features=CloudMessaging",
            "--disable-logging",
            "--log-level=3",
        ]
    )

open_chrome_profile()

def main():
    opt = Options()
    opt.add_experimental_option("debuggerAddress", "localhost:8989")
    driver = webdriver.Chrome(options=opt)
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/shadow-dom.html")

    content = driver.find_element(By.ID, "content")

        # Execute JavaScript to get shadow root
    shadow_root = driver.execute_script(
        "return arguments[0].shadowRoot", content
    )

    # Find element inside shadow DOM
    text_element = shadow_root.find_element(By.CSS_SELECTOR, "p")

    print("Text inside shadow DOM:", text_element.text)

    # Assertion
    # assert text_element.text == "Hello Shadow DOM", "Text does not match!"

    driver.quit()


if __name__ == "__main__":
    main()
