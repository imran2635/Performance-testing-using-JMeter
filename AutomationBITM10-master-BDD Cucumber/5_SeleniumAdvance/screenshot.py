from selenium import webdriver
import time

driver = webdriver.Chrome()
time.sleep(4)
driver.get("https://google.com")

driver.get_screenshot_as_file("F:\\SQA\\Batch10\\Projects\\AutomationBITM10\\Screenshot\\Google.png")

driver.close()