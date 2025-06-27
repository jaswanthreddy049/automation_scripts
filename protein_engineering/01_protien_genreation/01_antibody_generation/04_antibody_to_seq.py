from selenium import webdriver
from selenium.webdriver import chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize the Chrome WebDriver
driver = webdriver.Chrome()
driver.get("https://app-boltzmann-com.web.app/")
driver.maximize_window()
# Wait for elements to load using explicit wait
mywait = WebDriverWait(driver, 15, poll_frequency=2)

# Credentials
email = "test@boltzmann.co"
password = "test@1234" 

# Action_chains
Actions = webdriver.ActionChains(driver)


from login import login
login(mywait, driver, email, password)

# Navigate to Protein Engineering section
try:
    Protein_engineering = mywait.until(EC.presence_of_element_located((By.XPATH, "//h6[normalize-space()='Protein Engineering']")))
    Protein_engineering.click()

    # Navigate to protein generation section
    Protein= mywait.until(EC.presence_of_element_located((By.XPATH, "//p[normalize-space()='PROTEIN GENERATION']")))
    Protein.click()
    # Navigate to antibody generation section
    antibody= mywait.until(EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Antibody Generation']")))
    antibody.click()

    # Navigate to antibody to seq generation section
    Protein= mywait.until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Antibody Backbone to Sequence Generation']")))
    Protein.click()
    
    Actions.send_keys(Keys.ESCAPE).perform()  # Close any pop-up if it appears

    # Verfication of navigation
    expected="https://app-boltzmann-com.web.app/protein-engineering/experiments/anti-body-generation/antibody-backbonetosequencegen"
    if driver.current_url == expected:
        print("Navigation to BACKBONE Generation section successful.")   
except Exception as e:
    print(f"Navigation failed due to exception: {e}")

# Select Project
Project = "boltzmann"
#Select_project = mywait.until(EC.presence_of_element_located((By.XPATH, "//label[text()='Select project']/following-sibling::div/child::input")))
Open_project_list = mywait.until(EC.presence_of_element_located((By.XPATH, "//button[@title='Open']")))
Open_project_list.click()
Select_project = mywait.until(EC.presence_of_element_located((By.XPATH, f"//li[text()='{Project}']")))
Select_project.click()
print(f"Project '{Project}' selected successfully.")
exp_list = [
    {"type": "//button[@id='simple-tab-0']", "name": "heavy_chain"},
    {"type": "//button[@id='simple-tab-1']", "name": "light_chain"}
]
# Select Data type
try:
    for i in exp_list:
        Experiment_name_input = mywait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='outlined-basic']")))
        Experiment_name_input.send_keys(i['name'])
        print(f"Experiment name '{i['name']}' entered successfully.")
        # Upload file
        file_input = mywait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='file']")))
        file_input.send_keys("/Users/likithamaddipati/Downloads/boltpro inputs/General_version_Launch_testing/1.Protein_generation/Antibody Generation/Backbone to sequence generation/5f1a.pdb")
        print("File upload successful.") 
        submit= mywait.until(EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Submit']")))
        submit.click()
        print("Submit button clicked successfully.")
        time.sleep(5)  # Wait for the submission to process
        # Submission verification & table content check
        # Name column verification
        Exp_table = mywait.until(EC.presence_of_element_located((By.XPATH, f"//div[@row-index='0']/descendant::div[contains(text(),'{i['name']}')]")))
        
        if Exp_table.is_displayed():
            print(f"Experiment '{i['name']}' submitted successfully.")
            print("Experiment name is displayed in the table.")
        else:
            print(f"Experiment '{i['name']}' submission failed.")
        
        # Project name verification
        TProject_name = mywait.until(EC.presence_of_element_located((By.XPATH, f"//div[@row-index='0']/descendant:: div[@aria-colindex='2' and contains(text(),'{Project}')]")))
        if TProject_name.is_displayed():
            print(f"Project '{Project}' is displayed in the table.")
        else:
            print(f"Project '{Project}' is not displayed in the table.")
        # Status column verification
        Status = ["Pending","Completed","Failed"]

        try:
            Status_ver = mywait.until(EC.presence_of_element_located((By.XPATH, f"//div[@row-index='0']/descendant::div[@aria-colindex='3' and @col-id='status']//span")))
            status_text = Status_ver.text
            if status_text in Status:
                print(f"Experiment is in '{status_text}' state in the table.")
            else:
                    print(f"Experiment has an unexpected status: '{status_text}'")
        except Exception as e:
            print(f"Failed to detect the experiment status due to exception: {e}")
        # Created at column verification
        Created_at = mywait.until(EC.presence_of_element_located((By.XPATH, f"//div[@row-index='0']/descendant::div[@aria-colindex='4']")))
        created_at_text = Created_at.text
        print(f"Experiment is Created at time: {created_at_text}")
        if Created_at.is_displayed():
            print("Created at column is displayed in the table.")
        else:
            print("Created at column is not displayed in the table.")
        # Actions column verification
        Actions_list = ['View','Edit','Delete']
        for action in Actions_list:
            try:
                if action == 'View':
                    action_button = mywait.until(EC.presence_of_element_located((By.XPATH, 
                                            f"//div[@row-index='0']/descendant::div[@col-id='Actions']/child::button[1]")))
                    if action_button.is_displayed():
                        print(f"'{action}' action is available in the Actions column.")
                    else:
                        print(f"'{action}' action is not available in the Actions column.")
                elif action == 'Edit':
                    action_button = mywait.until(EC.presence_of_element_located((By.XPATH, 
                                            f"//div[@row-index='0']/descendant::div[@col-id='Actions']/child::button[2]")))
                    if action_button.is_displayed():
                        print(f"'{action}' action is available in the Actions column.")
                    else:
                        print(f"'{action}' action is not available in the Actions column.")
                else:
                    action_button = mywait.until(EC.presence_of_element_located((By.XPATH, 
                                            f"//div[@row-index='0']/descendant::div[@col-id='Actions']/child::button[3]")))
                    if action_button.is_displayed():
                        print(f"'{action}' action is available in the Actions column.")
                    else:
                        print(f"'{action}' action is not available in the Actions column.")
            except Exception as e:
                print(f"Failed to detect the action buttons due to exception:{e}")


        
            
except Exception as e:
    print(f"Flow failed due to exception: {e}")

    # Close the driver