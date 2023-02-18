import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from get_project_root import root_path


def all_alert_demo():
    project_root = root_path(ignore_cwd=True)
    driver_path = project_root + "\Drivers\geckodriver.exe"

    driver = webdriver.Firefox(executable_path=driver_path)
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")

    # Normal Alert
    driver.find_element(By.CSS_SELECTOR, "li:nth-of-type(1) > button").click()
    time.sleep(3)
    # Click on OK button
    driver.switch_to.alert.accept()

    # Confirmation Alert
    driver.find_element(By.CSS_SELECTOR, "li:nth-of-type(2) > button").click()
    time.sleep(2)
    # CLick ok Cancel button
    driver.switch_to.alert.dismiss()

    # Prompt Alert
    driver.find_element(By.CSS_SELECTOR, "li:nth-of-type(3) > button").click()
    time.sleep(2)

    driver.switch_to.alert.send_keys("Test Automation")
    time.sleep(2)

    driver.switch_to.alert.accept()


all_alert_demo()
