import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MyinfoPage():
    def __init__(self, driver):
        self.driver = driver

    def test_myinfo(self, firstName,middleName,lastName):

        self.driver.find_element(By.CSS_SELECTOR, ".oxd-sidepanel-body .oxd-main-menu-item-wrapper:nth-of-type(6) .oxd-main-menu-item--name").click()
        time.sleep(4)

        firstname_field = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
            (By.NAME, "firstName")))
        
        middlename_field = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
            (By.NAME, "middleName")))
        
        lastname_field  = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
            (By.NAME, "lastName")))

        save_button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, ".orangehrm-edit-employee-content .orangehrm-vertical-padding:nth-of-type(1) .oxd-button--secondary"
        )))

        firstname_field.click()
        firstname_field.clear()
        firstname_field.send_keys(firstName)

        middlename_field.click()
        middlename_field.clear()
        middlename_field.send_keys(middleName)

        lastname_field.click()
        lastname_field.clear()
        lastname_field.send_keys(lastName)

        save_button.click()



