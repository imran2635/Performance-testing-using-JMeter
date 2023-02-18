from selenium import webdriver
import time


class MultipleWindow():
    def switch_window(self):
        driver = webdriver.Firefox()
        driver.get("https://google.com")
        print("Starting window: " + driver.title)
        time.sleep(3)

        # open a new window
        driver.execute_script("window.open('https://the-internet.herokuapp.com/');")
        time.sleep(5)

        windows = driver.window_handles
        print(windows)

        # switch to the new window
        driver.switch_to.window(windows[1])
        print("Switch to new window: " + driver.title)
        time.sleep(3)

        # switch back to the old window
        driver.switch_to.window(windows[0])
        print("Back to old window: " + driver.title)
        time.sleep(3)

        # switch back to the old window
        driver.switch_to.window(windows[1])
        print("Again switch to new window: " + driver.title)
        time.sleep(3)

        driver.quit()


obj = MultipleWindow()
obj.switch_window()
