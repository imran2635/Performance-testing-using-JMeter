from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given('I am on the login page')
def step_impl(context):
    context.driver = webdriver.Firefox()
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")


@when("I enter my username and password")
def step_impl(context):
    username_field = WebDriverWait(context.driver, 10).until(EC.presence_of_element_located(
        (By.NAME, "username")))

    password_field = WebDriverWait(context.driver, 10).until(EC.presence_of_element_located(
        (By.NAME, "password")))

    username_field.clear()
    username_field.send_keys("Admin")

    password_field.clear()
    password_field.send_keys("admin123")


@when("I click on login button")
def step_impl(context):
    login_button = WebDriverWait(context.driver, 10).until(EC.presence_of_element_located(
        (By.CSS_SELECTOR,
         "#app > div.orangehrm-login-layout > div > div.orangehrm-login-container > div > div.orangehrm-login-slot > div.orangehrm-login-form > form > div.oxd-form-actions.orangehrm-login-action > button")))

    login_button.click()


@then("I should be redirect to dashboard page and close browser")
def step_impl(context):
    print(context.driver.title)
    context.driver.close()
