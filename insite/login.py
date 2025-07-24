
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.remote.webdriver import WebDriver


class LoginFlow:
    def __init__(self, driver:WebDriver):
        self.driver = driver

    def login_processing(self):
        login_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((
                By.XPATH,
                '//*[@id="block-insite-main-menu"]/ul/li[7]/a'
            ))
        )
        login_button.click()

    def sign_text(self, email, password):
        time.sleep(5)
        tabs = self.driver.window_handles

        if len(tabs) > 1:
            self.driver.switch_to.window(tabs[1])
        else:
            print("no new tab found")

        click_sign_text = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((
                By.XPATH,
                '//*[@id="block-insite-content"]/article/div/div/div/div/div[1]/p/a'
            ))
        )
        click_sign_text.click()

        # connect_button = WebDriverWait(self.driver, 10).until(
        #     EC.element_to_be_clickable((
        #         By.XPATH,
        #         '/html/body/insite-container//div/div[2]/button'
        #     ))
        # )
        # connect_button.click()

        # i skip one step once i will find the solution i will do that

        email_field = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((
                By.ID, 'edit-name'
            ))
        )
        email_field.send_keys(email)

        password_field = self.driver.find_element(By.ID, 'edit-pass')
        password_field.send_keys(password)

        submit_button = self.driver.find_element(By.ID, 'edit-submit')
        submit_button.click()



































