# writing python program to fetch and generate csv file of result
"""
Developed by Shiven Saini :)
Tools used :- Python, Selenium
Website to launch :- https://cbseresults.nic.in/class12/Class12th21.htm
"""

# Importing required Selenium Libraries
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Defining Function which will handle basically all the fetching stuff & computations.
def fetch_detail(roll, school_code):

    # Selecting and filling Roll No.
    roll_xpath = '/html/body/table[3]/tbody/tr/td/font/center[2]/form/div[1]/center/table/tbody/tr[1]/td[2]/input'
    Roll_Entry = wait.until(EC.presence_of_element_located((By.XPATH, roll_xpath)))
    Roll_Entry.click()
    Roll_Entry.send_keys(f'{roll}')

    # Clicking School Code and entering value!
    code_xpath = '/html/body/table[3]/tbody/tr/td/font/center[2]/form/div[1]/center/table/tbody/tr[2]/td[2]/input'
    Code_Entry = wait.until(EC.presence_of_element_located((By.XPATH, code_xpath)))
    Code_Entry.click()
    Code_Entry.send_keys(f'{school_code}')

    # Clicking Submit
    submit_xpath =  '/html/body/table[3]/tbody/tr/td/font/center[2]/form/div[1]/center/table/tbody/tr[3]/td/input[1]'
    Submit_Btn = wait.until(EC.presence_of_element_located((By.XPATH, submit_xpath)))
    Submit_Btn.click()

    # Fetching Candidate Name
    name_xpath = '/html/body/div/table[1]/tbody/tr[2]/td[2]/font/b'
    Name_Text = wait.until(EC.presence_of_element_located((By.XPATH, name_xpath)))
    std_name = Name_Text.text

    # Computing Total marks of 5 Subjects (Excluding additional Subjects)
    global Total_Marks
    Total_Marks = 0
    for i in range(2,7):
        subi_xpath = f'/html/body/div/div/center/table/tbody/tr[{i}]/td[5]/font'
        subi_Text = wait.until(EC.presence_of_element_located((By.XPATH, subi_xpath)))
        Total_Marks += int(subi_Text.text)

    # Computing Percentage etc.
    Percentage = (Total_Marks/500)*100
    Percentage = round(Percentage, 1)

    with open('candidate_list.csv', 'a') as file:
        file.write(f'\n{roll},{std_name},{Total_Marks},{Percentage}')

    Total_Marks = Percentage = 0
    # Clicking on fetch another result link
    another_xpath = '/html/body/div/p[1]/b/a'
    Name_Text = wait.until(EC.presence_of_element_located((By.XPATH, another_xpath)))
    Name_Text.click()

# Laying basic information in 'CSV' format by creating a file.
with open('candidate_list.csv', 'w') as file:
    file.write('Roll No.,Student Name,Total Marks,Percentage')

# Calling Function for entire Roll No. Range
school_code = int(input("Enter your CBSE School Code :- "))
roll_start = int(input("Enter First Roll number :- "))
roll_last = int(input("Enter last Roll number :- "))

# Initiating Chrome Browser automated window
driver = webdriver.Chrome(r'C:\driver\chromedriver.exe')    #Don't forget to set your webdriver location.
driver.get("https://cbseresults.nic.in/class12/Class12th21.htm")
wait = WebDriverWait(driver, 1000)

# Starting Script/Program For Loop.
print("Please Wait.... \nGenerating...")
for rollNo in range(roll_start, roll_last+1):
    fetch_detail(rollNo, school_code)

driver.quit()   # Closing the Chrome Window.

print("\n\n Done! Enjoy :) ")
