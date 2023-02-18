from selenium.webdriver.common.by import By
from selenium import webdriver
from get_project_root import root_path
import time

def logout_user():
    # Launch Browser
    project_root = root_path(ignore_cwd=True)
    driver_path = project_root + "\Drivers\geckodriver.exe"
    driver = webdriver.Firefox(executable_path=driver_path)
    driver.get("https://automationexercise.com/")

    # Verifying Home Page
    verify_home_page = driver.find_element(By.CSS_SELECTOR,
                                           "#header > div > div > div > div.col-sm-8 > div > ul > li:nth-child(1) > a > i")
    print("1.Verifying Home Page:")
    print(verify_home_page.is_displayed())
    time.sleep(1)

    # Click on 'Signup / Login' button
    signup = driver.find_element(By.CSS_SELECTOR, ".navbar-nav > li:nth-child(4) > a:nth-child(1)")
    signup.click()
    time.sleep(1)

    # Verify that 'Logged in as username' is visible
    verify_login_username = driver.find_element(By.CSS_SELECTOR, ".login-form > h2:nth-child(1)")
    print("2.Verify that 'Logged in as username' is visible")
    print(verify_login_username.is_displayed())

    # Enter correct email address and password
    Enter_name = driver.find_element(By.NAME, "email")
    Enter_name.send_keys("bitm10.0033@yopmail.com")
    time.sleep(1)

    Enter_email = driver.find_element(By.NAME, "password")
    Enter_email.send_keys("12345")
    time.sleep(1)

    # Click 'login' button
    click_login = driver.find_element(By.CSS_SELECTOR, "button.btn:nth-child(4)")
    click_login.click()

    # Verify that 'Logged in as username' is visible
    verify_loggin_as_username = driver.find_element(By.CSS_SELECTOR, ".navbar-nav > li:nth-child(10) > a:nth-child(1)")
    print("3.Verify that 'Logged in as username' is visible")
    print(verify_loggin_as_username.is_displayed())

    # Click 'logout' button
    click_logout = driver.find_element(By.CSS_SELECTOR, ".navbar-nav > li:nth-child(4) > a:nth-child(1)")
    click_logout.click()

    # Verify that user is navigated to login page
    verify_user_navigated_to_login_page = driver.find_element(By.CSS_SELECTOR, ".login-form > h2:nth-child(1)")
    print("3.Verify that user is navigated to login page:")
    print(verify_user_navigated_to_login_page.is_displayed())


logout_user()