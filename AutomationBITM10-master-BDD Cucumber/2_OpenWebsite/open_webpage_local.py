from selenium import webdriver


def open_webpage_online():
    driver = webdriver.Firefox(executable_path="E:\\Offline_Batch_10\\Projects\\geckodriver-v0.32.0-win64"
                                               "\\geckodriver.exe")
    driver.get("http://localhost:8080/")
    driver.close()


open_webpage_online()
