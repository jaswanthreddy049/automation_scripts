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

    # Navigate to evobind  section
    Protein= mywait.until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Evobind']")))
    Protein.click()
    
    Actions.send_keys(Keys.ESCAPE).perform()  # Close any pop-up if it appears

    # Verfication of navigation
    expected="https://app-boltzmann-com.web.app/protein-engineering/experiments/peptide-generation/evobind"
    # Check if the current URL matches the expected URL
    if driver.current_url == expected:
        print("Navigation to evobind section successful.")   
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
try:
    exp_name="evobind"
    Experiment_name_input = mywait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='experimentname']")))
    Experiment_name_input.send_keys(exp_name)
    print(f"Experiment name entered successfully.")
    seq= mywait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='sequence']")))
    seq.send_keys("LVTDEAEASKFVEEYDRTSQVVWNEYAGANWNYNTNITTETSKILLQKNMQIAQHTLKYGTQARKFDVNQLQNTTIKRIIKKVQDLERAALPAQELEEYNKILLDMETTYSVATVCHPQGSCLQLEPDLTNVMATSRKYEDLLWAWEGWRDKAGRAILQFYPKYVELINQAARLNGYVDAGDSWRSMYETPSLEQDLERLFQELQPLYLNLHAYVRRALHRHYGAQHINLEGPIPAHLLGNMWAQTWSNIYDLVVPFPSAPSMDTTEAMLKQGWTPRRMFKEADDFFTSLGLLPVPPEFWQKSMLEKPTDGREVVCHASAWDFYNGKDFRIKQCTTVNLEDLVVAHHEMGHIQYFMQYKDLPVALREGANPGFHEAIGDVLALSVSTPKHLHSLNLLSSEGGSDEHDINFLMKMALDKIAFIPFSYLVDQWRWRVFDGSITKENYNQEWWSLRLKYQGLCPPVPRTQGDFDPGAKFHIPSSVPYIRYFVSFIIQFQFHEALCQAAGHTGPLHKCDIYQSKEAGQRLATAMKLGFSRPWPEAMQLITGQPQMSASAMLSYFKPLLDWLRTENELHGEKLGWPQYNWTPNSARSEGPLP")
    print("Sequence entered successfully.")
    pep= mywait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='num_peptides']")))
    pep.send_keys(Keys.CONTROL + 'a')  # Select all text in the input field
    pep.send_keys(Keys.BACKSPACE)  # Clear the input field
    pep.send_keys("0")
    print("Number of peptides entered successfully.")
    seqlen= mywait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='seq_length']")))
    seqlen.send_keys(Keys.CONTROL + 'a')  # Select all text in the input field  
    seqlen.send_keys(Keys.BACKSPACE)  # Clear the input field
    seqlen.send_keys("0")
    print("Sequence length entered successfully.")
    target_res= mywait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='target_resid']")))
    target_res.send_keys(Keys.CONTROL + 'a')  # Select all text in the input field
    target_res.send_keys(Keys.BACKSPACE)  # Clear the input field
    target_res.send_keys("318,319,320,341,347,348,351,355,374,375,421,475,476,477,482,484,487")
    print("Target residues entered successfully.")
    radio= mywait.until(EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='False']")))
    radio.click()
    file_input = mywait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='file']")))
    file_input.send_keys("/Users/likithamaddipati/Downloads/boltpro inputs/General_version_Launch_testing/1.Protein_generation/Peptide Generation/Evobind/hhblits_full_5811711.a3m")
    print("File upload successful.") 
    submit= mywait.until(EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Submit']")))
    submit.click()
    print("Submit button clicked successfully.")
    time.sleep(7)  # Wait for the submission to process
    # Submission verification & table content check
    # Name column verification
    Exp_table = mywait.until(EC.presence_of_element_located((By.XPATH, f"//div[@row-index='0']/descendant::div[contains(text(),'{exp_name}')]")))
    
    if Exp_table.is_displayed():
        print(f"Experiment '{exp_name}' submitted successfully.")
        print("Experiment name is displayed in the table.")
    else:
        print(f"Experiment '{exp_name}' submission failed.")
    
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