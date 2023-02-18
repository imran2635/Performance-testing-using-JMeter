from selenium import webdriver


def firefox_launch():
    driver = webdriver.Firefox(executable_path="E:\\Offline_Batch_10\\Projects\\geckodriver-v0.32.0-win64"
                                               "\\geckodriver.exe")

    driver.close()


firefox_launch()
