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
    antibody= mywait.until(EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Antibody']")))
    antibody.click()
    Actions.send_keys(Keys.ESCAPE).perform()  # Close any pop-up if it appears
    # Verfication of navigation
    expected="https://app-boltzmann-com.web.app/protein-engineering/experiments/antibody/antibody-property-prediction"
    # Check if the current URL matches the expected URL
    if driver.current_url == expected:
        print("Navigation to antibody section successful.")   
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
Data_types = ['Data_set'] #'Upload File','Data_set','Sequence'
Select_categories = ['All'] #,'Toxicity','Allergenicity','Antigenicity','Epitope'

# === Reusable Helpers ===
"""def fill_field(field_id, value):
    input_elem.send_keys(Keys.BACKSPACE)
    input_elem.send_keys(value)
    print(f"{field_id.capitalize()} input successful.")
def Values():
    fill_field("Thermal Stability ESM", "10")
    fill_field("Thermal Stability Protbert", "10")
    fill_field("Solubility ESM", "10")
    fill_field("Antigen Antibody Binding","10")
    fill_field("CDR Prediction","10")
    return "10", "10", "10","10","10"
    """
    
# Select Data type
try:
    for data_type in Data_types:
        for Category in Select_categories:
            #Experiment name
            Experiment_name = 'antibody_Automate_' + data_type + '_' + Category
            experiment_name_input = mywait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='experimentname']")))
            experiment_name_input.send_keys(Experiment_name)

            # Select category
            if Category == 'All':
                category_element = mywait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='MuiBox-root css-1lekzkb']//input[@type='checkbox']")))
                category_element.click()
                print("Category 'All' selected successfully.")
            else:
                category_element = mywait.until(EC.presence_of_element_located((By.XPATH, f"//input[@value='{Category}']")))
                category_element.click()
                print(f"Category '{Category}' selected successfully.")

            # Select data type
            #data_type_element = mywait.until(EC.presence_of_element_located((By.XPATH, f"//button[normalize-space()='{data_type}']")))
            #data_type_element.click()
            #print(f"Data type '{data_type}' selected successfully.")

            if data_type=='Sequence' and Category== 'All' or Category=="Antigen Antibody Binding":
                # Input sequence    
                seq= mywait.until(EC.presence_of_element_located((By.XPATH, "//button[@id='simple-tab-0']")))
                seq.click()
                print("Sequence tab selected successfully.")
                # Input light and heavy chain sequences
                light='0'
                sequence_input = mywait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='lightchain']")))
                sequence_input.send_keys(light)
                print("Light chain sequence entered successfully.")
                heavy="0"
                sequence_input = mywait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='heavychain']")))
                sequence_input.send_keys(heavy)
                print("Light and Heavy chain sequences entered successfully.")
                antigen="0"
                antigen_seq= mywait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='AntigenSequence']")))
                antigen_seq.send_keys(antigen)
                print("Antigen sequence entered successfully.")
            elif data_type=="Sequence":
                # Input sequence    
                light='0'
                seq= mywait.until(EC.presence_of_element_located((By.XPATH, "//button[@id='simple-tab-0']")))
                seq.click()
                sequence_input = mywait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='lightchain']")))
                sequence_input.send_keys(light)
                print("Light chain sequence entered successfully.")
                heavy="0"
                sequence_input = mywait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='heavychain']")))
                sequence_input.send_keys(heavy)
                print("Light and Heavy chain sequences entered successfully.")
            elif data_type =="Upload file" and Category == 'All' or Category == "Antigen Antibody Binding":
                # Upload file
                # Click on the upload file tab  
                file=mywait.until(EC.presence_of_element_located((By.XPATH, "//button[@id='simple-tab-1']")))
                file.click()
                print("Upload file tab selected successfully.")
                # Upload file
                file_input = mywait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='file']")))
                file_input.send_keys("/Users/likithamaddipati/Downloads/boltpro inputs/General_version_Launch_testing/2.Property_prediction/Antibody Properties/Input.csv")
                print("File upload successful.")    
                antigen="0"
                antigen_seq= mywait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='AntigenSequence']")))
                antigen_seq.send_keys(antigen)
                print("Antigen sequence entered successfully.")
            elif data_type =="Upload file" and Category != "Antigen Antibody Binding":
                # Upload file
                # Click on the upload file tab  
                file=mywait.until(EC.presence_of_element_located((By.XPATH, "//button[@id='simple-tab-1']")))
                file.click()
                print("Upload file tab selected successfully.")
                # Upload file
                file_input = mywait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='file']")))
                file_input.send_keys("/Users/likithamaddipati/Downloads/boltpro inputs/General_version_Launch_testing/2.Property_prediction/Antibody Properties/Input.csv")
                print("File upload successful.")
                
            elif data_type == 'Data_set' and Category == 'All' or Category == "Antigen Antibody Binding":
                # Dataset selection
                data=mywait.until(EC.presence_of_element_located((By.XPATH, "//button[@id='simple-tab-2']")))
                data.click()
                print("Dataset tab selected successfully.")
                dataset_list = mywait.until(EC.presence_of_element_located((By.XPATH, "//div[@name='dataset']//button[@title='Open']")))
                dataset_list.click()
                Dataset = 'wdra91_valset'
                dataset_option = mywait.until(EC.presence_of_element_located((By.XPATH, f"//p[normalize-space()='{Dataset}']")))
                dataset_option.click()
                antigen="0"
                antigen_seq= mywait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='AntigenSequence']")))
                antigen_seq.send_keys(antigen)
                print("Antigen sequence entered successfully.")
                
                print(f"Dataset '{Dataset}' selected successfully.")
            else:
                # Dataset selection
                data=mywait.until(EC.presence_of_element_located((By.XPATH, "//button[@id='simple-tab-2']")))
                data.click()
                print("Dataset tab selected successfully.")
                dataset_list = mywait.until(EC.presence_of_element_located((By.XPATH, "//div[@name='dataset']//button[@title='Open']")))
                dataset_list.click()
                Dataset = 'wdra91_valset'
                dataset_option = mywait.until(EC.presence_of_element_located((By.XPATH, f"//p[normalize-space()='{Dataset}']")))
                dataset_option.click()
                print(f"Dataset '{Dataset}' selected successfully.")

            # Submit the form
            submit_button = mywait.until(EC.element_to_be_clickable((By.XPATH,"//button[@type='submit']")))
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
        
            # Reset the form for the next iteration
    print("All experiments submitted successfully.")
    driver.quit    
                
except Exception as e:
    print(f"Flow failed due to exception: {e}")

