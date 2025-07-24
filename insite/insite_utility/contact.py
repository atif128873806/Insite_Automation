
import email
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver

import time

class ContactUs:
    def __init__(self, driver:WebDriver):
        self.driver = driver

    
    def filling_contact(self):

        contact_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((
                By.XPATH, '//*[@id="block-footer-2"]/ul/li[3]/a'
                ))
        )
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", contact_button)
        time.sleep(2)
        contact_button.click()

        input("After the Human Verification. Press Enter for further testing.....")
        time.sleep(5)

        name_field = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((
                By.ID, 'edit-your-name'
            ))
        )
        name_field.send_keys('Automation Tester')

        email_field = self.driver.find_element(By.ID, 'edit-your-email')
        email_field.send_keys('testmail@gmail.com')

        msg_field = self.driver.find_element(By.ID, 'edit-your-message')
        msg_field.send_keys('Just automation testing....................')

        submit_btn = self.driver.find_element(By.ID, 'edit-actions-submit')
        submit_btn.click()
        
        h1_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((
                By.XPATH, '//*[@id="block-insite-content"]/article/div/div/div/div/div/h1[3]'
            ))
        )

        h1_text = h1_element.text

        assert h1_text == "Thank you for contacting us", f"Unexpected H1 text: {h1_text}"

        


        