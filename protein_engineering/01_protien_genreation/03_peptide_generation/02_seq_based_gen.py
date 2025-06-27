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
    # Navigate to peptide generation section
    antibody= mywait.until(EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Peptide Generation']")))
    antibody.click()
    # Navigate to seq based  peptide  generation section
    Protein= mywait.until(EC.presence_of_element_located((By.XPATH,"//span[normalize-space()='Sequence Based Peptide Generation']")))
    Protein.click()
    
    Actions.send_keys(Keys.ESCAPE).perform()  # Close any pop-up if it appears

    # Verfication of navigation
    expected="https://app-boltzmann-com.web.app/protein-engineering/experiments/peptide-generation/sequence-based-generation"
    # Check if the current URL matches the expected URL
    if driver.current_url == expected:
        print("Navigation to sequence based peptide generation section successful.")   
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
    
# Select Data type
try:
    #Experiment name
    Experiment_name = "peptide generation"
    Experiment_name_input = mywait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='experimentname']")))
    Experiment_name_input.send_keys(Experiment_name)
    print(f"Experiment name '{Experiment_name}' entered successfully.")
    target= mywait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='antigen']")))
    target.send_keys("MYRRVMSLLVALGAIVAALIVLPATTAQAATCATAWSSSSVYTNGGTVSYNGRNYTAKWWTQNERPGTSDVWADKGACGTGGEGPGGNNGFVVSEAQFNQMFPNRNAFYTYKGLTDALSAYPAFAKTGSDEVKKREAAAFLANVSHETGGLFYIKEVNEANYPHYCDTTQSYGCPAGQAAYYGRGPIQLSWNFNYKAAGDALGINLLANPYLVEQDPAVAWKTGLWYWNSQNGPGTMTPHNAIVNNAGFGETIRSINGALECNGGNPAQVQSRINKFTQFTQILGTTTGPNLSC")
    seq= mywait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='noofsequence']")))
    #backspace seq
    seq.send_keys(Keys.CONTROL + 'a')
    seq.send_keys(Keys.BACKSPACE)  # Press backspace to clear the input field
    seq.send_keys("20")
    print("Number of sequences set to 20.")
    max= mywait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='maxpeptide']")))
    #backspace seq
    max.send_keys(Keys.CONTROL + 'a')
    max.send_keys(Keys.BACKSPACE)  # Press backspace to clear the input field
    max.send_keys("20")
    print("Number of sequences set to 20.")
    submit= mywait.until(EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Submit']")))
    submit.click()
    print("Submit button clicked successfully.")
    time.sleep(5)  # Wait for the submission to process
    # Submission verification & table content check
    # Name column verification
    Exp_table = mywait.until(EC.presence_of_element_located((By.XPATH, f"//div[@row-index='0']/descendant::div[contains(text(),'{Experiment_name}')]")))
    
    if Exp_table.is_displayed():
        print(f"Experiment '{Experiment_name}' submitted successfully.")
        print("Experiment name is displayed in the table.")
    else:
        print(f"Experiment '{Experiment_name}' submission failed.")
    
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