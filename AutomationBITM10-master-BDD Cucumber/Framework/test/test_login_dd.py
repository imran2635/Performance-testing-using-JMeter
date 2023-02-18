import time

import unittest
from selenium import webdriver
from Framework.page.login_page import LoginPage
from Framework.utils import excel_utils


class LoginTest(unittest.TestCase):
    driver = webdriver.Firefox()

    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(3)

    file = "F:\\SQA\\Batch10\\Projects\\AutomationBITM10\\Framework\\data\\test_data.xlsx"
    sheet = "Sheet1"

    number_of_rows = excel_utils.row_count(file, sheet)

    for r in range(2, number_of_rows + 1):
        username_dd = excel_utils.read_data(file, sheet, r, 1)
        password_dd = excel_utils.read_data(file, sheet, r, 2)

        obj = LoginPage(driver)
        obj.login_orange(username_dd, password_dd)

    driver.close()
