import time

import unittest
from selenium import webdriver
from Framework.page.login_page import LoginPage
from Framework.page.myInfo_page import MyinfoPage


class MyInfoTest(unittest.TestCase):
    driver = webdriver.Firefox()

    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(3)

    obj = LoginPage(driver)
    obj.login_orange("Admin", 'admin123')
    time.sleep(5)

    obj = MyinfoPage(driver)
    obj.test_myinfo("Mr", "admin123", "Test")
    time.sleep(3)

    driver.close()
