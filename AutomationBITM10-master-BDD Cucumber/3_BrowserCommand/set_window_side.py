from selenium import webdriver


def set_browser_size():
    driver = webdriver.Firefox(executable_path="E:\\Offline_Batch_10\\Projects\\geckodriver-v0.32.0-win64"
                                               "\\geckodriver.exe")
    driver.set_window_size(768, 1024)
    driver.get("https://demo.opencart.com/index.php")


set_browser_size()
