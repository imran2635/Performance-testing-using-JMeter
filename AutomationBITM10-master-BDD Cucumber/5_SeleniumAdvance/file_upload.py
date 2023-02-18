from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from get_project_root import root_path
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class FileUpload():
    def upload(self):
        project_root = root_path(ignore_cwd=True)
        driver = webdriver.Firefox()
        driver.get("https://the-internet.herokuapp.com/upload")

        choose_file_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.ID, "file-upload")))

        file = project_root + "\Screenshot\Google.png"

        choose_file_button.send_keys(file)

        upload_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.ID, "file-submit")))

        upload_button.click()

        success_message = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, "/html/body/div[2]/div/div/h3"))).text

        try:
            assert "File Uploaded!" == success_message
            print("File Upload Success")
        except:
            print("File Upload failed")

        time.sleep(5)

        driver.close()


obj = FileUpload()
obj.upload()
