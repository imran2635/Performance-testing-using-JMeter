from selenium.webdriver.common.by import By
from selenium import webdriver
import time
from selenium.webdriver import ActionChains


def add_to_cart():
    driver = webdriver.Firefox(executable_path="F:\\SQA\\Batch10\\Projects\\AutomationBITM10\\Drivers\\geckodriver.exe")
    driver.get("https://automationexercise.com/")

    # Verify that home page is visible successfully
    home_page_visibility = driver.find_element(By.CSS_SELECTOR, "#header > div > div > div > div.col-sm-8 > div > ul > li:nth-child(1) > a")
    print("1.Verify that home page is visible successfully:")
    print(home_page_visibility.is_displayed())

    # Click 'Products' button
    click_products = driver.find_element(By.CSS_SELECTOR, "#header > div > div > div > div.col-sm-8 > div > ul > li:nth-child(2) > a")
    click_products.click()
    time.sleep(2)

    # Hover over first product and click 'Add to cart'
    first_product = driver.find_element(By.CSS_SELECTOR, "body > section:nth-child(3) > div > div > div.col-sm-9.padding-right > div.features_items > div:nth-child(3) > div > div.single-products > div.productinfo.text-center > a")
    actions = ActionChains(first_product)
    actions.move_to_element(first_product)

    # Click to add to cart
    driver.find_element(By.CLASS_NAME, "btn btn-default add-to-cart").click()

    # Click 'Continue Shopping' button
    click_conitue_shopping = driver.find_element(By.CLASS_NAME, "btn btn-success close-modal btn-block").click()

    # Hover over second product and click 'Add to cart'
    second_product = driver.find_element(By.CSS_SELECTOR, "body > section:nth-child(3) > div > div > div.col-sm-9.padding-right > div > div:nth-child(4) > div > div.single-products > div.productinfo.text-center > img")
    actions = ActionChains(second_product)
    actions.move_to_element(second_product)

    # Click to add to cart
    driver.find_element(By.CLASS_NAME, "btn btn-default add-to-cart").click()

    # Click 'View Cart' button
    view_cart = driver.find_element(By.CSS_SELECTOR, "#cartModal > div > div > div.modal-body > p:nth-child(2) > a > u")
    view_cart.click()
    time.sleep(2)

    # Verify both products are added to Cart
    verify_product1 = driver.find_element(By.CSS_SELECTOR, "#product-1 > td.cart_description > h4 > a")
    print("2.Verify first products is added to Cart:")
    print(home_page_visibility.is_displayed())

    verify_product2 = driver.find_element(By.CSS_SELECTOR, "#product-2 > td.cart_description > h4 > a")
    print("3.Verify second products is added to Cart:")
    print(home_page_visibility.is_displayed())

    # Verify their prices, quantity and total price
    verify_p1_price = driver.find_element(By.CSS_SELECTOR, "#product-1 > td.cart_price > p")
    verify_p1_quantity = driver.find_element(By.CSS_SELECTOR, "#product-1 > td.cart_quantity > button")
    verify_p1_total = driver.find_element(By.CSS_SELECTOR, "#product-1 > td.cart_total > p")
    print("4.Verify their prices, quantity and total price:")
    print(verify_p1_price.is_displayed())


add_to_cart()