import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from get_project_root import root_path


def check_state():
    project_root = root_path(ignore_cwd=True)
    driver_path = project_root + "\Drivers\geckodriver.exe"

    driver = webdriver.Firefox(executable_path=driver_path)
    driver.get("https://demo.guru99.com/v4/index.php")

    # Fine UserID
    UserID = driver.find_element(By.NAME, "uid")

    # Check Display Status
    display_status = UserID.is_displayed()
    # print(display_status)

    # Check Enable Status
    enable_status = UserID.is_enabled()
    # print(enable_status)

    if display_status == True and enable_status == True:
        UserID.send_keys("mngr473843")
        time.sleep(5)

    driver.get("https://the-internet.herokuapp.com/checkboxes")
    time.sleep(3)

    checkbox2 = driver.find_element(By.XPATH, "//form[@id='checkboxes']/input[2]")
    checked_status = checkbox2.is_selected()

    if checked_status:
        print("Test Passed.")
    else:
        print("Test Failed.")

    driver.close()


check_state()
