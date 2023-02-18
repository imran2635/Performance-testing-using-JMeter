from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage():
    def __init__(self, driver):
        self.driver = driver

    def login_orange(self, username, password):
        # wait for element to be present on the page
        username_field = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
            (By.NAME, "username")))

        password_field = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
            (By.NAME, "password")))

        login_button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
            (By.CSS_SELECTOR,
             "#app > div.orangehrm-login-layout > div > div.orangehrm-login-container > div > div.orangehrm-login-slot > div.orangehrm-login-form > form > div.oxd-form-actions.orangehrm-login-action > button")))

        username_field.clear()
        username_field.send_keys(username)

        password_field.clear()
        password_field.send_keys(password)

        login_button.click()
