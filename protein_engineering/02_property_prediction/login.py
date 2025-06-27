import time
from selenium import webdriver
from selenium.webdriver import chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
def login(mywait,driver,email,password):
    # Login process
    try:
        email_input = mywait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='email']")))
        password_input = mywait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='password']")))

        email_input.send_keys(email)
        password_input.send_keys(password)

        login_button = mywait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Login']")))
        login_button.click()

        # Post-login verification
        logo = mywait.until(EC.presence_of_element_located((By.XPATH, "//img[@alt='Logo']")))
        homepage = mywait.until(EC.presence_of_element_located((By.XPATH, "//h6[normalize-space()='HomePage']")))

        if logo.is_displayed():
            print("Logo is present. Login is successful.")
        elif homepage.is_displayed() and homepage.text == "HomePage":
            print("HomePage is present. Login is successful.")
        else:
            print("Login failed.")

    except Exception as e:
        print(f"Login failed due to exception: {e}")