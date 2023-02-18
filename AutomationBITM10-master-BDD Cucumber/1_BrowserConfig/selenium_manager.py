from selenium import webdriver
import time

driver = webdriver.Chrome()
time.sleep(4)
driver.get("https://google.com")