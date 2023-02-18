from selenium.webdriver.common.by import By
from selenium import webdriver
import time


def register_user():
    # Make browser Headless
    firefox_options = webdriver.FirefoxOptions()
    firefox_options.headless = True

    driver = webdriver.Firefox(executable_path="F:\\SQA\\Batch10\\Projects\\AutomationBITM10\\Drivers\\geckodriver.exe", options=firefox_options)
    driver.get("https://automationexercise.com/")

    # Verifying Home Page
    verify_home_page = driver.find_element(By.CSS_SELECTOR , "#header > div > div > div > div.col-sm-8 > div > ul > li:nth-child(1) > a > i")
    print("1.Verifying Home Page:")
    print(verify_home_page.is_displayed())
    time.sleep(1)

    # Click on 'Signup / Login' button
    signup = driver.find_element(By.CSS_SELECTOR,".navbar-nav > li:nth-child(4) > a:nth-child(1)")
    signup.click()
    time.sleep(1)

    # Verify 'New User Signup!' is visible
    verify_new_user_signup = driver.find_element(By.CSS_SELECTOR, "#form > div > div > div:nth-child(3) > div > h2")
    print("2.Verify 'New User Signup!' is visible: " )
    print(verify_new_user_signup.is_displayed())
    time.sleep(1)

    # Enter name and email address
    Enter_name = driver.find_element(By.NAME, "name")
    Enter_name.send_keys("Arafat")
    time.sleep(1)

    Enter_email = driver.find_element(By.CSS_SELECTOR, "#form > div > div > div:nth-child(3) > div > form > input[type=email]:nth-child(3)")
    Enter_email.send_keys("bitm10.00371112@yopmail.com")
    #time.sleep(1)

    # Click 'Signup' button
    Signup = driver.find_element(By.CSS_SELECTOR, "#form > div > div > div:nth-child(3) > div > form > button")
    Signup.click()

    # Verify that 'ENTER ACCOUNT INFORMATION' is visible
    verify_enter_account_info = driver.find_element(By.CSS_SELECTOR, "#form > div > div > div > div.login-form > h2 > b")
    print("3.Verify 'ENTER ACCOUNT INFORMATION!' is visible:")
    print(verify_enter_account_info.is_displayed())
    #time.sleep(1)

    # Select Title (Check Box)
    mr_mrs = driver.find_element(By.ID, "id_gender1")
    mr_mrs.click()

    # Enter Password
    password = driver.find_element(By.ID, "password")
    password.send_keys("12345")
    #time.sleep(1)

    # Enter Date of Birth
    day = driver.find_element(By.ID, "days")
    day.send_keys("12")

    month = driver.find_element(By.ID, "months")
    month.send_keys("Ja")

    year = driver.find_element(By.ID, "years")
    year.send_keys("20")

    # Select checkbox 'Sign up for our newsletter!'
    newsletter = driver.find_element(By.ID, "newsletter")
    newsletter.click()

    # Select checkbox 'Receive special offers from our partners!'
    partner = driver.find_element(By.ID, "optin")
    partner.click()

    #  Fill details: First name, Last name, Company, Address, Address2, Country, State, City, Zipcode, Mobile Number
    # Enter first name
    First_name = driver.find_element(By.ID, "first_name")
    First_name.send_keys("Arafat")
    #time.sleep(1)

    # Enter last name
    Last_name = driver.find_element(By.ID, "last_name")
    Last_name.send_keys("Ali")
    #time.sleep(1)

    # Enter Company
    Company_name = driver.find_element(By.ID, "company")
    Company_name.send_keys("Bismillah Tradings Ltd.")
    #time.sleep(1)

    # Enter Address1
    Address1 = driver.find_element(By.NAME, "address1")
    Address1.send_keys("Street 21/2, PO Box 5200, Bismillah Tradings Ltd.")
    #time.sleep(1)

    # Enter Address2
    Address2 = driver.find_element(By.NAME, "address2")
    Address2.send_keys("Kamal Sarani, Dhaka")
    #time.sleep(1)

    # Enter Country
    Country = driver.find_element(By.NAME, "country")
    Country.send_keys("U")
    #time.sleep(1)

    # Enter State
    State = driver.find_element(By.NAME, "state")
    State.send_keys("Oklahoma")
    #time.sleep(1)

    # Enter City
    City = driver.find_element(By.NAME, "city")
    City.send_keys("Los Angeles")
    #time.sleep(1)

    # Enter Zipcode
    Zipcode= driver.find_element(By.NAME, "zipcode")
    Zipcode.send_keys("90001")
    #time.sleep(1)

    # Enter Mobile Number
    Mobile_number = driver.find_element(By.NAME, "mobile_number")
    Mobile_number.send_keys("+880 1796105264")
    #time.sleep(2)

    # Click to Create Account
    Create_Account = driver.find_element(By.CSS_SELECTOR, "button.btn:nth-child(22)")
    Create_Account.click()
    time.sleep(1)

    # Verify that 'ACCOUNT CREATED!' is visible
    Verify_account_created = driver.find_element(By.CSS_SELECTOR,
                                                    "#form > div > div > div > h2 > b")
    print("4.Verify that 'ACCOUNT CREATED!' is visible:")
    print(Verify_account_created.is_displayed())
    time.sleep(1)

    # Click 'Continue' button
    Click_Continue = driver.find_element(By.CSS_SELECTOR, "#form > div > div > div > div > a")
    Click_Continue.click()
    #time.sleep(2)

    # Skipping add
    driver.refresh()

    driver.find_element(By.LINK_TEXT, "Continue").click()

    # Verify that 'Logged in as username' is visible
    verify_loggin_as_username = driver.find_element(By.CSS_SELECTOR, ".navbar-nav > li:nth-child(10) > a:nth-child(1)")
    print("5.Verify that 'Logged in as username' is visible")
    print(verify_loggin_as_username.is_displayed())

    # Click 'Delete Account' button
    click_delete_account = driver.find_element(By.CSS_SELECTOR, ".navbar-nav > li:nth-child(5) > a:nth-child(1)")
    click_delete_account.click()

    # Verify that 'ACCOUNT DELETED!' is visible
    verify_account_deleted = driver.find_element(By.CSS_SELECTOR, ".title > b:nth-child(1)")
    print("6.Verify that 'ACCOUNT DELETED!' is visible")
    print(verify_account_deleted.is_displayed())


register_user()
