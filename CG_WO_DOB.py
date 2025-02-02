from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from datetime import datetime, timedelta

# Path to ChromeDriver
chrome_driver_path = "C:/Users/Himu/Desktop/PY Projects/chromedriver-win64/chromedriver.exe"

# Set up Selenium WebDriver
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

driver.get("https://erp.uttarauniversity.edu.bd/online-result")
wait = WebDriverWait(driver, 0)  # Increased timeout to 20 seconds

# Student ID to test
student_id = "2233161049"

# Start searching from December 31, 2005, to December 31, 2000
start_date = datetime(2005, 12, 31)
end_date = datetime(2000, 12, 31)

found = False  # Flag to stop looping once found

current_date = start_date

while current_date >= end_date and not found:
    dob = current_date.strftime("%Y-%m-%d")  # Format date as YYYY-MM-DD
    print(f"Trying DOB: {dob}")

    # Input Student ID
    id_input = wait.until(EC.presence_of_element_located((By.NAME, "sid")))
    id_input.clear()
    id_input.send_keys(student_id)

    # Input Date of Birth using JavaScript
    dob_input = driver.find_element(By.NAME, "dob")
    driver.execute_script("arguments[0].value = arguments[1];", dob_input, dob)

    # Select Academic Year
    try:
        academic_year_div = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='col-md-3'][3]")))
        academic_year_dropdown = academic_year_div.find_element(By.XPATH, ".//span[@class='select2-selection select2-selection--single']")
        academic_year_dropdown.click()
        for _ in range(3):  # Press Down 3 times
            academic_year_dropdown.send_keys(Keys.ARROW_DOWN)
        academic_year_dropdown.send_keys(Keys.ENTER)
        # print("Selected 2024 as Academic Year.")
    except Exception as e:
        print(f"Error selecting Academic Year: {e}")

    # Select Semester
    try:
        semester_div = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='col-md-3'][4]")))
        semester_dropdown = semester_div.find_element(By.XPATH, ".//span[@class='select2-selection select2-selection--single']")
        semester_dropdown.click()
        for _ in range(3):  # Press Down 3 times
            semester_dropdown.send_keys(Keys.ARROW_DOWN)
        semester_dropdown.send_keys(Keys.ENTER)
        # print("Selected Fall as Semester.")
    except Exception as e:
        print(f"Error selecting Semester: {e}")

    # Click Search Button
    search_button = driver.find_element(By.CLASS_NAME, "btn-primary")
    search_button.click()

    # Wait for results to load
    try:
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "table-bordered")))
        cgpa_element = driver.find_element(By.XPATH, "//td[contains(text(), 'Semester GPA')]/following-sibling::td")
        cgpa = cgpa_element.text
        print(f"✅ Student ID: {student_id}, CGPA: {cgpa}, DOB: {dob} Semester: Fall-24")
        found = True  # Stop loop if CGPA is found
    except:
        print(f"❌ No result for DOB: {dob}")
        current_date -= timedelta(days=1)  # Move to the previous day

# Close the browser
driver.quit()
