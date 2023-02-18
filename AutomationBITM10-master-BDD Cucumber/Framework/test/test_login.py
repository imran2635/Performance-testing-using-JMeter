import time

import unittest
from selenium import webdriver
from Framework.page.login_page import LoginPage


class LoginTest(unittest.TestCase):
    driver = webdriver.Firefox()

    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(3)

    obj = LoginPage(driver)
    obj.login_orange("Admin", 'admin123')

    driver.close()



