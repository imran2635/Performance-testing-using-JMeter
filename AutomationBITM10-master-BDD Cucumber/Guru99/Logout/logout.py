from selenium import webdriver
from selenium.webdriver.common.by import By
from get_project_root import root_path
import time

def logout():
    project_root = root_path(ignore_cwd=True)
    driver_path = project_root + "\Drivers\geckodriver.exe"

    driver = webdriver.Firefox(executable_path=driver_path)
    driver.get("https://demo.guru99.com/v4/index.php")

    # Enter userID
    UserID = driver.find_element(By.NAME, "uid")
    UserID.send_keys("mngr473843")

    # Enter Password
    Password = driver.find_element(By.NAME, "password")
    Password.send_keys("qujYjEm")

    # Click Login
    Login_button = driver.find_element(By.NAME, "btnLogin")
    Login_button.click()

    # Click Logout
    driver.find_element(By.LINK_TEXT, "Log out").click()
    time.sleep(2)

    driver.switch_to.alert.accept()


logout()