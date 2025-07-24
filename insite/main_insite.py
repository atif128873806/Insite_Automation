import time
import insite.insite_url as const
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import subprocess


from insite.email_verifier import EmailVerification
from insite.login import LoginFlow
from .insite_utility.interaction import Interaction
from .insite_utility.contact import ContactUs




# Function to check Chrome version
def get_chrome_version():
    try:
        # Try to get Chrome version using subprocess
        if sys.platform.startswith('linux'):  # just replace with you operating system
            result = subprocess.run(['google-chrome', '--version'], capture_output=True, text=True)
            version = result.stdout.strip().split()[-1].split('.')[0]
            return int(version)
        return None
    except Exception as e:
        print(f"Error getting Chrome version: {e}")
        return None

class Insite:
    def __init__(self, teardown=False):
        self.teardown = teardown
        
        # Get Chrome version
        chrome_version = get_chrome_version()
        print(f"Detected Chrome version: {chrome_version}")
        
        options = uc.ChromeOptions()
        
        # Basic options
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--start-maximized")
        
        # Try to initialize Chrome with version matching
        try:
            print("Attempting to start Chrome with version matching...")
            self.driver = uc.Chrome(
                options=options,
                use_subprocess=True,
                version_main=chrome_version  # Use the detected Chrome version
            )
            self.driver.implicitly_wait(15)
            self.driver.maximize_window()
            print("Chrome started successfully!")
        except Exception as e:
            print(f"Error starting Chrome: {str(e)}")
            print("\nTroubleshooting steps:")
            print("1. Make sure Chrome is installed")
            print("2. Try updating Chrome to the latest version")
            print("3. Try running: pip install --upgrade undetected-chromedriver")
            print("4. Check if there are any Chrome processes running and close them")
            raise

    def __enter__(self):
        return self
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.driver.quit()

    def landing_first_page(self):
        self.driver.get(const.BASE_URL)

    def accept_cokkies(self):
        try:
            accept_cokky = WebDriverWait(self.driver, 15).until(
                EC.element_to_be_clickable((
                    By.ID,
                    'CybotCookiebotDialogBodyButtonAccept'
                ))
            )
            accept_cokky.click()
        except:
            pass

    def get_insite_free(self):
        get_insite_button = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((
                By.XPATH,
                '//*[@id="block-insite-content"]/article/div/div/div[1]/div/div[2]/div/p[4]/a'
            ))
        )
        get_insite_button.click()
        # this is for beta pricing registration
    def click_beta_pricing_plan(self):
        beta_pricing_button = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((
                By.XPATH,
                '//*[@id="block-insite-content"]/article/div/div/div/div/div[2]/div[1]/article/div/div[3]/a'
            ))
        )
        beta_pricing_button.click()
        #this is for personal pricing registration
    def click_personal_pricing_plan(self):
        personal_pricing_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((
                By.XPATH,
                '//*[@id="block-insite-content"]/article/div/div/div/div/div[2]/div[2]/article/div/div[3]/a'
            ))
        )
        personal_pricing_button.click()

    def click_team_pricing_plan(self):
        team_pricing_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((
                By.XPATH,
                '//*[@id="block-insite-content"]/article/div/div/div/div/div[2]/div[3]/article/div/div[3]/a'
            ))
        )
        team_pricing_button.click()

    def email_verification(self, password="YourPassword123!"):
        verification = EmailVerification(driver=self.driver)
        # Get the verification link from the email
        verification_link = verification.perform_verification("automation", "tester")
        # Use the verification link to fill out the form
        verification.fill_verification_form(verification_link, password)

    def onboarding_questioner(self):
        first_question = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((
                By.XPATH,
                '//*[@id="edit-what-s-your-main-reason-for-using-insit-radios"]/div[4]/label'
            ))
        )
        first_question.click()

        other_field = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((
                By.ID, 'edit-what-s-your-main-reason-for-using-insit-other'
            ))
        )
        other_field.send_keys("automation")


        next_btn1 = self.driver.find_element(By.ID, 'edit-wizard-next')
        next_btn1.click()

        next_btn1 = self.driver.find_element(By.ID, 'edit-wizard-next')
        next_btn1.click()

        next_btn1 = self.driver.find_element(By.XPATH, '//*[@id="edit-submit"]')
        next_btn1.click()

        # Verify the onboarding was successful
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'heading'))
            )
            return True
        except Exception as e:
            print(f"Error in onboarding_questioner: {str(e)}")
            return False

    def download_extension(self):
        download_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((
                By.CLASS_NAME, 'button'
            ))
        )
        download_button.click()

        # Wait for the "Add to Chrome" button and click it
        add_chrome = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((
                By.CSS_SELECTOR, 'button[jsname="wQO0od"]'
            ))
        )
        add_chrome.click()
        
        # Wait for the Chrome extension dialog to appear
        time.sleep(3)  # Give some time for the dialog to appear
        
        try:
            import pyautogui
            # Move the mouse to the center of the screen (where the dialog appears)
            screen_width, screen_height = pyautogui.size()
            
            # Press Tab to focus the "Add extension" button (may need adjustment based on your system)
            pyautogui.press('tab')
            time.sleep(0.5)
            
            # Press Enter to confirm
            pyautogui.press('enter')
            print("Extension installation confirmed")

        except Exception as e:
            print(f"Error handling extension dialog: {str(e)}")
            print("You may need to manually confirm the extension installation.")


        time.sleep(10)
        #get all window handles
        tabs = self.driver.window_handles

        if len(tabs) > 1:
            self.driver.switch_to.window(tabs[1])
        else:
            print("no new tab found")


        # self.driver.get("https://api.insite.life/")
        #
        # connect_button = self.driver.find_element(By.CLASS_NAME, 'Button-module_root__8RX49')
        # connect_button.click()


    #loggin
    def login_process(self):
        login = LoginFlow(driver=self.driver)

    #here, Start Dashboard navigation files begins
    def interaction_utilities(self):
        interact = Interaction(driver=self.driver)












