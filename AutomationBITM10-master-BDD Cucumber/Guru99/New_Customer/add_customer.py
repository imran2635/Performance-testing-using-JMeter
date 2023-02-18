from selenium import webdriver
from selenium.webdriver.common.by import By
from get_project_root import root_path
from selenium.webdriver.common.keys import Keys
import time


def add_customer_valid():
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

    New_customer = driver.find_element(By.LINK_TEXT, "New Customer")
    New_customer.click()
    time.sleep(5)

    customer_name = driver.find_element(By.NAME, "name")
    customer_name.send_keys("Superman")

    gender_female = driver.find_element(By.CSS_SELECTOR,
                                        "body > table > tbody > tr > td > table > tbody > tr:nth-child(5) > "
                                        "td:nth-child(2) > input[type=radio]:nth-child(2)")
    gender_female.click()
    time.sleep(4)

    driver.find_element(By.ID, "dob").send_keys("1111")
    driver.find_element(By.ID, "dob").send_keys(Keys.TAB)
    driver.find_element(By.ID, "dob").send_keys("2020")

    address = driver.find_element(By.NAME, "addr")
    address.send_keys("Dhaka")


# add_customer_valid()


def add_customer_valid_customer_name():
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

    New_customer = driver.find_element(By.LINK_TEXT, "New Customer")
    New_customer.click()
    time.sleep(5)

    customer_name = driver.find_element(By.NAME, "name")
    customer_name.send_keys("")

    gender_female = driver.find_element(By.CSS_SELECTOR,
                                        "body > table > tbody > tr > td > table > tbody > tr:nth-child(5) > "
                                        "td:nth-child(2) > input[type=radio]:nth-child(2)")
    gender_female.click()
    time.sleep(4)

    customer_name_error_message_actual = driver.find_element(By.ID, "message").text

    customer_name_error_message_expected = "Customer name must not be blank"

    try:
        assert customer_name_error_message_expected == customer_name_error_message_actual
        print("Customer name[Blank] Assert Passed")

    except:
        print("Customer name[Blank] Assert Failed")

    # First Character Space
    customer_name.send_keys(" superman")
    customer_name_error_message_actual = driver.find_element(By.ID, "message").text

    customer_name_error_message_expected = "First character can not have space"

    try:
        assert customer_name_error_message_expected == customer_name_error_message_actual
        print("Customer name[Space] Assert Passed")

    except:
        print("Customer name[Space] Assert Failed")


    # Number
    customer_name.send_keys("123321")
    customer_name_error_message_actual = driver.find_element(By.ID, "message").text

    customer_name_error_message_expected = "Numbers are not allowed"

    try:
        assert customer_name_error_message_expected == customer_name_error_message_actual
        print("Customer name[Number] Assert Passed")

    except:
        print("Customer name[Number] Assert Failed")

    driver.close()


add_customer_valid_customer_name()
