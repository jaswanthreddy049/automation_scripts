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

    # Navigate to property generation section
    Property= mywait.until(EC.presence_of_element_located((By.XPATH, "//p[normalize-space()='PROPERTY PREDICTION']")))
    Property.click()
    # Navigate to antibody section
    antibody= mywait.until(EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Enzyme']")))
    antibody.click()
    Actions.send_keys(Keys.ESCAPE).perform()  # Close any pop-up if it appears
    # Verfication of navigation
    expected="https://app-boltzmann-com.web.app/protein-engineering/experiments/enzymes/unified-enzyme"
    # Check if the current URL matches the expected URL
    if driver.current_url == expected:
        print("Navigation to Enzymes section successful.")   
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
# Data_types

# Data_types
Data_types = ['Upload file'] #'Sequence','Upload file',
Select_categories = ['Function prediction'] #,'Toxicity','Allergenicity','Antigenicity','Epitope'
"""
# === Reusable Helpers ===
def fill_field(field_id, value):
    input_elem = mywait.until(EC.presence_of_element_located((By.ID, field_id)))
    input_elem.send_keys(Keys.CONTROL + 'a')
    input_elem.send_keys(Keys.BACKSPACE)
    input_elem.send_keys(value)
    print(f"{field_id.capitalize()} input successful.")

def Values():
    fill_field("PH prediction", "10")
    fill_field("Enzyme solubility", "10")
    fill_field("Tmpred enzymes", "10")
    fill_field("Function prediction", "10")
    fill_field("Substrate prediction", "10")
    return "10", "10", "10","10" ,"10"
    """
    
# Select Data type
try:
    for data_type in Data_types: 
        for Category in Select_categories:

            #Experiment name
            Experiment_name = 'Enzymes_Automated_' + data_type + '_' + Category
            experiment_name_input = mywait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='experimentname']")))
            experiment_name_input.send_keys(Experiment_name)

            # Select category
            if Category == 'All':
                category_element = mywait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='checkbox']")))
                category_element.click()
                print("Category 'All' selected successfully.")
            else:
                category_element = mywait.until(EC.presence_of_element_located((By.XPATH, f"//span[normalize-space()='{Category}']")))
                category_element.click()
                print(f"Category '{Category}' selected successfully.")


            # Select data type
            #data_type_element = mywait.until(EC.presence_of_element_located((By.XPATH, f"//button[normalize-space()='{data_type}']")))
            #data_type_element.click()
            #print(f"Data type '{data_type}' selected successfully.")
            if data_type=='Sequence' and Category== 'All' or Category=="Substrate prediction":
                # Input sequence    
                seq= mywait.until(EC.presence_of_element_located((By.XPATH, "//button[@id='simple-tab-0']")))
                seq.click()
                print("Sequence tab selected successfully.")
                # Input light and heavy chain sequences
                seq='0'
                sequence_input = mywait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='sequence']")))
                sequence_input.send_keys(seq)
                print(" entered successfully.")
                Substrate="0"
                antigen_seq= mywait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='AntigenSequence']")))
                antigen_seq.send_keys(Substrate)
                print("Substrate sequence entered successfully.")
            elif data_type=="Sequence" and Category != "Substrate prediction":
                # Input sequence    
                seq= mywait.until(EC.presence_of_element_located((By.XPATH, "//button[@id='simple-tab-0']")))
                seq.click()
                print("Sequence tab selected successfully.")
                # Input light and heavy chain sequences
                seq='0'
                sequence_input = mywait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='sequence']")))
                sequence_input.send_keys(seq)
                print(" entered successfully.")
            elif data_type =="Upload file":
                # Upload file
                # Click on the upload file tab  
                file=mywait.until(EC.presence_of_element_located((By.XPATH, "//button[@id='simple-tab-1']")))
                file.click()
                print("Upload file tab selected successfully.")
                # Upload file
                file_input = mywait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='file']")))
                file_input.send_keys("/Users/likithamaddipati/Downloads/boltpro inputs/General_version_Launch_testing/2.Property_prediction/Enzyme/Function_prediction_input.csv")
                print("File upload successful.")
            else:
                # Dataset selection
                data=mywait.until(EC.presence_of_element_located((By.XPATH, "//button[@id='simple-tab-2']")))
                data.click()
                print("Dataset tab selected successfully.")
                dataset_list = mywait.until(EC.presence_of_element_located((By.XPATH, "//div[@name='dataset']//button[@title='Open']")))
                dataset_list.click()
                Dataset = ' '
                dataset_option = mywait.until(EC.presence_of_element_located((By.XPATH, f"//p[normalize-space()='{Dataset}']")))
                dataset_option.click()
                
                print(f"Dataset '{Dataset}' selected successfully.")
            # Submit the form
            submit_button = mywait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Submit']")))
            submit_button.click()
            time.sleep(5)
            
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
# Close the browser
print("Test completed. Closing the browser.")
driver.quit()
