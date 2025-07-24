from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver

import time

class BodyNavigation:

    def __init__(self, webdriver:WebDriver):
            self.driver = webdriver
            self.wait = WebDriverWait(self.driver, 10)


    def interact_with_body(self):
        body_configs = [
             {
                  'name': 'Try insite for free',
                  'locator': (By.XPATH, '//*[@id="block-insite-content"]/article/div/div/div[1]/div/div[2]/div/p[4]/a'),
                  'verification_locator': (By.XPATH, '//*[@id="block-insite-content"]/article/div/div/div/div/div[1]/h1'),
                  'verification_type': 'visibility',
                  'scroll_locator' : (By.XPATH, '//*[@id="block-insite-content"]/article/div/div/div[3]/div/div/div[4]/div/div[2]/div/p[4]/a')
             },
             {
                  'name': 'Try insite for free 2nd button',
                  'locator': (By.XPATH, '//*[@id="block-insite-content"]/article/div/div/div[3]/div/div/div[4]/div/div[2]/div/p[4]/a'),
                  'verification_locator': (By.XPATH, '//*[@id="block-insite-content"]/article/div/div/div/div/div[1]/h1'),
                  'verification_type': 'visibility',
                  'scroll_locator' : (By.XPATH, '//*[@id="block-insite-content"]/article/div/div/div[6]/div/div/p[4]/a')
             },
              {
                  'name': 'Team demo video link text',
                  'locator': (By.XPATH, '//*[@id="block-insite-content"]/article/div/div/div[6]/div/div/p[2]/a'),
                  'verification_locator': (By.XPATH, '//*[@id="title"]/h1/yt-formatted-string'),
                  'verification_type': 'visibility',
                  'scroll_locator' : (By.XPATH, '//*[@id="block-insite-content"]/article/div/div/div[6]/div/div/p[4]/a')
             },
             {
                  'name': 'Try insite for free 3rd button',
                  'locator': (By.XPATH, '//*[@id="block-insite-content"]/article/div/div/div[6]/div/div/p[4]/a'),
                  'verification_locator': (By.XPATH, '//*[@id="block-insite-content"]/article/div/div/div/div/div[1]/h1'),
                  'verification_type': 'visibility',
                  'scroll_locator' : (By.XPATH, '//*[@id="block-insite-content"]/article/div/div/div[6]/div/div/p[4]/a')
             },
             {
                  'name': 'Available in the chrome Web Store',
                  'locator': (By.XPATH, '//*[@id="footer"]/div[1]/div/div/a'),
                  'verification_locator': (By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div/main/div/section[1]/section/div/div[1]/div[1]/h1'),
                  'verification_type': 'visibility',
                  'scroll_locator' : (By.XPATH, '//*[@id="block-insite-content"]/article/div/div/div[6]/div/div/p[4]/a')
             },
              {
                  'name': 'Terms of service',
                  'locator': (By.XPATH, '//*[@id="block-footer-2"]/ul/li[1]/a'),
                  'verification_locator': (By.XPATH, '//*[@id="block-insite-content"]/article/div/div/div/div/div/h1'),
                  'verification_type': 'visibility',
                  'scroll_locator' : (By.XPATH, '//*[@id="block-insite-content"]/article/div/div/div[6]/div/div/p[4]/a')
             },
             {
                  'name': 'Privacy policy',
                  'locator': (By.XPATH, '//*[@id="block-footer-2"]/ul/li[2]/a'),
                  'verification_locator': (By.XPATH, '//*[@id="h.q2iel6fdo8ke"]/span'),
                  'verification_type': 'visibility',
                  'scroll_locator' : (By.XPATH, '//*[@id="block-insite-content"]/article/div/div/div[6]/div/div/p[4]/a')
             },
             {
                  'name': 'Instagram link',
                  'locator': (By.XPATH, '//*[@id="footer"]/div[2]/div/div/ul/li[1]/a/div/div'),
                  'scroll_locator' : (By.XPATH, '//*[@id="block-insite-content"]/article/div/div/div[6]/div/div/p[4]/a')
             },
             {
                  'name': 'Linkedin link',
                  'locator': (By.XPATH, '//*[@id="footer"]/div[2]/div/div/ul/li[2]/a/div/div'),
                  'scroll_locator' : (By.XPATH, '//*[@id="block-insite-content"]/article/div/div/div[6]/div/div/p[4]/a')
             },
              {
                  'name': 'Twitter link',
                  'locator': (By.XPATH, '//*[@id="footer"]/div[2]/div/div/ul/li[3]/a/div/div'),
                  'scroll_locator' : (By.XPATH, '//*[@id="block-insite-content"]/article/div/div/div[6]/div/div/p[4]/a')
             },
          
          

        ]

        original_handle = self.driver.current_window_handle  # Store the original tab handle

        for config in body_configs:
         try:
                  # click the button
                  button = WebDriverWait(self.driver, 10).until(
                       EC.element_to_be_clickable(config['locator'])
                  )
                  button.click()

                  # Wait for possible new tab
                  time.sleep(2)
                  handles = self.driver.window_handles
                  if len(handles) > 1:
                      self.driver.switch_to.window(handles[-1])  # Switch to new tab

                      #verify the interaction (optional)
                      if 'verification_locator' in config:
                          if config.get('verification_type', 'visibility') == 'visibility':
                              self.wait.until(EC.visibility_of_element_located(config['verification_locator']))
                          else:
                              self.wait.until(EC.presence_of_element_located(config['verification_locator']))

                      print(f"\n ✓ {config['name']} button click successful")

                      # Close the new tab after verification
                      self.driver.close()
                      # Switch back to the original tab
                      self.driver.switch_to.window(original_handle)
                  else:
                      #verify the interaction in the current tab (optional)
                      if 'verification_locator' in config:
                          if config.get('verification_type', 'visibility') == 'visibility':
                              self.wait.until(EC.visibility_of_element_located(config['verification_locator']))
                          else:
                              self.wait.until(EC.presence_of_element_located(config['verification_locator']))

                      print(f"\n ✓ {config['name']} button click successful")

                  self.driver.get('https://www.insite.life/') 

                  element = WebDriverWait(self.driver, 10).until(
                       EC.visibility_of_element_located(config['scroll_locator'])
                  )
                  # Scroll to the element
                  time.sleep(2)
                  self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)

                  time.sleep(1)


                  
         except Exception as e:
                  err = f"\nFailed to interact with {config['name']} button: {str(e)}"
                  print(err)  # This code is only for debugging purposes
                  raise




