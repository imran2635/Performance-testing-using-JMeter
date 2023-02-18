from selenium import webdriver
from selenium.webdriver.common.by import By
from get_project_root import root_path


class Login_Guru99():
    global driver

    def login_valid(self):
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

    def login_invalid(self):
        project_root = root_path(ignore_cwd=True)
        driver_path = project_root + "\Drivers\geckodriver.exe"

        driver = webdriver.Firefox(executable_path=driver_path)
        driver.get("https://demo.guru99.com/v4/index.php")

        # Enter userID
        UserID = driver.find_element(By.NAME, "uid")
        UserID.send_keys("")

        # Enter Password
        Password = driver.find_element(By.NAME, "password")
        Password.send_keys("qujYjEm")

        # Click Login
        Login_button = driver.find_element(By.NAME, "btnLogin")
        Login_button.click()

        driver.close()


obj = Login_Guru99()
#obj.login_valid()
obj.login_invalid()

