# This is for to automate the email verification
# first we install the Mailosaur library
# we used random email so in every execution the email is automatically change


import secrets




from mailosaur import MailosaurClient
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
from mailosaur.models import SearchCriteria
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time


load_dotenv()

class EmailVerification:
    def __init__(self, driver:WebDriver):
        self.driver = driver

    def perform_verification(self, first_name, last_name):

        # Load environment variables from .env file
        # from dotenv import load_dotenv
        load_dotenv()
        
        # Get environment variables
        api_key = "WeldgqcntKOUdJbW8qWfQLTVFKrwctdu"
        server_id = "wavlgmb1"
        
        # Validate environment variables
        if not api_key or not server_id:
            raise ValueError("""
            Missing required environment variables.
            Please create a .env file with the following variables:
            MAILOSAUR_API_KEY=your_api_key_here
            MAILOSAUR_SERVER_ID=your_server_id_here
            """)

        # Instantiate Mailosaur client with api key
        mailosaur = MailosaurClient(api_key)

        # Generate a random string for email
        random_string = ''.join(secrets.choice('abcdefghijklmnopqrstuvwxyz0123456789') for _ in range(10))
        email_address = f'{random_string}@{server_id}.mailosaur.net'

        # 1 fill the form
        iframe = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((
                By.TAG_NAME, "iframe"
            ))
        )
        self.driver.switch_to.frame(iframe)

        # fill the form
        def human_type(element, text):
            for character in text:
                element.send_keys(character)
                time.sleep(random.uniform(0.1, 0.3))  # Random delay between keystrokes

            # Random delay before starting

        time.sleep(random.uniform(1.0, 2.5))

        # Fill first name with delay
        first_name_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'first_name'))
        )
        human_type(first_name_field, first_name)

        # Random delay between fields
        time.sleep(random.uniform(0.5, 1.5))

        # Fill last name with delay
        last_name_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'last_name'))
        )
        human_type(last_name_field, last_name)

        # Random delay between fields
        time.sleep(random.uniform(0.8, 2.0))

        # Fill email with delay
        email_address_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'email'))
        )
        human_type(email_address_field, email_address)

        # Random delay before clicking submit
        time.sleep(random.uniform(1.0, 3.0))

        # Click submit with scroll
        beta_pricing_confirm_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="cb-body"]/div/div[2]/div/button/span'))
        )
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",
                                   beta_pricing_confirm_button)
        time.sleep(random.uniform(0.5, 1.5))  # Small delay after scroll
        self.driver.execute_script("arguments[0].click();", beta_pricing_confirm_button)

        time.sleep(random.uniform(0.5, 2))
        beta_pricing_final_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((
                By.CSS_SELECTOR, 'button[data-cb-id="review_submit"]'
            ))
        )

        beta_pricing_final_button.click()

        print(f"Waiting for email to be sent to: {email_address}")
        
        # 2 - Create the search criteria for the email
        criteria = SearchCriteria()
        criteria.sent_to = email_address
        
        # 3 - Wait for email with a single 30-second delay
        print("Waiting 30 seconds for email to arrive...")
        time.sleep(30)  # Wait 30 seconds for email to arrive
        
        try:
            email = mailosaur.messages.get(server_id, criteria)
            if email is None:
                raise Exception("No email received after waiting")
                
            print(f"Email found with subject: {email.subject}")
            
            # 4 - Extract the verification link from the email
            # Get the email body from text.body
            if hasattr(email, 'text') and email.text and hasattr(email.text, 'body') and email.text.body:
                email_body = email.text.body
            else:
                raise Exception("No email body content found in expected location (email.text.body)")
                
            # Look for a URL in the email body
            import re
            # This regex looks for common URL patterns in the email
            urls = re.findall(r'https?://\S+', email_body)
            
            if urls:
                # Get the first URL that looks like a verification link
                verification_link = next((url for url in urls if 'verify' in url.lower() or 'confirmation' in url.lower()), urls[0])
                
                # Return the verification link for use in another function
                return verification_link
            else:
                raise Exception("No verification URLs found in the email")

        except Exception as e:
            print(f"Error processing email: {str(e)}")
            print("Email text content:", getattr(email, 'text', 'No text content available'))
            raise

    def fill_verification_form(self, verification_link, password):

        try:
            # Open the verification link in the current browser window
            self.driver.get(verification_link)
            
            # Wait for the login button and click it
            login_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, 'edit-submit'))
            )
            login_button.click()
            
            # Wait for the page to load after clicking
            time.sleep(3)

            password_one_input = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((
                    By.ID, 'edit-pass-pass1'
                ))
            )
            password_one_input.send_keys(password)

            password_two_input = self.driver.find_element(By.ID, 'edit-pass-pass2')
            password_two_input.send_keys(password)

            final_save_btn = self.driver.find_element(By.ID, 'edit-submit')
            final_save_btn.click()

        except Exception as e:
            print(f"Error filling verification form: {str(e)}")
            raise


