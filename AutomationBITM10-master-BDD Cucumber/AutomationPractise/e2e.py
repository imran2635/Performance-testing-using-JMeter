import time

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


@pytest.fixture(scope="module")
def driver():
    # Initialize Chrome driver
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_home_page(driver):
    # Navigate to the URL of the web application
    driver.get("http://automationexercise.com")

    # Verify that the home page is displayed
    assert "Automation Exercise" in driver.title


def test_add_to_cart(driver):
    # Add products to the cart
    # Click 'Products' button
    click_products = driver.find_element(By.CSS_SELECTOR,
                                         "#header > div > div > div > div.col-sm-8 > div > ul > li:nth-child(2) > a")
    click_products.click()
    time.sleep(2)

    # Hover over first product and click 'Add to cart'
    first_product = driver.find_element(By.CSS_SELECTOR,
                                        "body > section:nth-child(3) > div > div > div.col-sm-9.padding-right > div.features_items > div:nth-child(3) > div > div.single-products > div.productinfo.text-center > a")
    actions = ActionChains(first_product)
    actions.move_to_element(first_product)

    # Verify that the products have been added to the cart
    #assert driver.find_element_by_css_selector(".cart-count").text == "1"


def test_checkout(driver):
    # Click the Cart button
    print("Checkout Done")


    # Verify that the cart page is displayed

    # Click the Proceed to Checkout button


    # Verify that the checkout page is displayed
