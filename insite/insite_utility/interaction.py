from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver



class Interaction:
    def __init__(self, driver:WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def interact_with_buttons(self):
        # List of button configurations
        button_configs = [
            {
                'name': 'Home',
                'locator': (By.CSS_SELECTOR, 'a[data-drupal-link-system-path="<front>"]'),
                'verification_locator': (By.XPATH, '//*[@id="block-insite-content"]/article/div/div/div[1]/div/div[2]/div/h1'),
                'verification_type': 'visibility'
            },
            {
                'name': 'Using Insite',
                'locator': (By.XPATH, '//*[@id="block-insite-main-menu"]/ul/li[2]/a'),
                'verification_locator': (By.XPATH, '//*[@id="block-insite-content"]/article/div/div/div[1]/div/div/h1'),
                'verification_type': 'visibility'
            },
            {
                'name': 'About Us',
                'locator': (By.XPATH, '//*[@id="block-insite-main-menu"]/ul/li[3]/a'),
                'verification_locator': (By.XPATH, '//*[@id="block-insite-content"]/article/div/div/div/div/div/h2'),
                'verification_type': 'visibility'
            },  
            {
                'name': 'Blog',
                'locator': (By.XPATH, '//*[@id="block-insite-main-menu"]/ul/li[4]/a'),
                'verification_locator': (By.XPATH, '//*[@id="block-insite-page-title"]/h1'),
                'verification_type': 'visibility'
            },
            {
                'name': 'Get Insite For Free',
                'locator': (By.XPATH, '//*[@id="block-insite-main-menu"]/ul/li[5]/a'),
                'verification_locator': (By.XPATH, '//*[@id="block-insite-content"]/article/div/div/div/div/div[1]/h1'),
                'verification_type': 'visibility'
            },
            {
                'name': 'Help',
                'locator': (By.XPATH, '//*[@id="block-insite-main-menu"]/ul/li[6]/a'),
                'verification_locator': (By.XPATH, '//*[@id="block-insite-content"]/article/div/div/div[1]/div/div/h1/span/strong'),
                'verification_type': 'visibility'
            },
            {
                'name': 'Sign In',
                'locator': (By.XPATH, '//*[@id="block-insite-main-menu"]/ul/li[7]/a'),
                'verification_locator': (By.CLASS_NAME,
                                         'heading'),
                'verification_type': 'visibility'
            }



            # Add more button configurations as needed
        ]

        for config in button_configs:
            try:
                # Click the button
                button = self.wait.until(EC.element_to_be_clickable(config['locator']))
                button.click()
                
                # Verify the interaction
                if config['verification_type'] == 'visibility':
                    self.wait.until(EC.visibility_of_element_located(config['verification_locator']))
                else:
                    self.wait.until(EC.presence_of_element_located(config['verification_locator']))
                
                print(f"\n  ✓ {config['name']} button interaction successful")
                
            except Exception as e:
                print(f"\n  ✗ Failed to interact with {config['name']} button: {str(e)}")
                raise

    # You can add more interaction methods here if needed
