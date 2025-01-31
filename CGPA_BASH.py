from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

# Path to ChromeDriver
chrome_driver_path = "C:/Users/Himu/Desktop/PY Projects/chromedriver-win64/chromedriver.exe"

# Excel file location and name
file_path = "C:/Users/Himu/Desktop/PY Projects/hack.xlsx"  # Path to your Excel file
df = pd.read_excel(file_path)

# Set up Selenium WebDriver with ChromeDriver path using Service
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

driver.get("https://erp.uttarauniversity.edu.bd/online-result")
wait = WebDriverWait(driver, 20)  # Increased timeout to 20 seconds

# Flag to ensure Academic Year and Semester are selected only once
is_first_iteration = True

for index, row in df.iterrows():
    student_id = str(row["Student ID"])
    dob = row["Date of Birth"].strftime("%Y-%m-%d")  # Format date to YYYY-MM-DD

    # Input Student ID
    id_input = wait.until(EC.presence_of_element_located((By.NAME, "sid")))
    id_input.clear()
    id_input.send_keys(student_id)

    # Input Date of Birth using JavaScript for full date value
    dob_input = driver.find_element(By.NAME, "dob")
    driver.execute_script("arguments[0].value = arguments[1];", dob_input, dob)  # Set the date directly

    # Select Academic Year and Semester only the first time
    if is_first_iteration:
        try:
            # Academic Year dropdown (third col-md-3 div)
            academic_year_div = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='col-md-3'][3]")))
            academic_year_dropdown = academic_year_div.find_element(By.XPATH, ".//span[@class='select2-selection select2-selection--single' and @aria-expanded='false']")
            academic_year_dropdown.click()  # Click to expand the dropdown
            # print("Dropdown expanded for Academic Year.")
            
            # Simulate pressing the down arrow key 3 times to reveal the options
            for _ in range(3):
                academic_year_dropdown.send_keys(Keys.ARROW_DOWN)
            # print("Pressed down arrow 3 times for Academic Year.")
            
            # After pressing the down key 3 times, hit Enter to select 2024
            academic_year_dropdown.send_keys(Keys.ENTER)
            print("Selected 2024 as Academic Year.")
        except Exception as e:
            print(f"Error selecting Academic Year: {e}")

        try:
            # Semester dropdown (fourth col-md-3 div)
            semester_div = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='col-md-3'][4]")))
            semester_dropdown = semester_div.find_element(By.XPATH, ".//span[@class='select2-selection select2-selection--single' and @aria-expanded='false']")
            semester_dropdown.click()  # Click to expand the dropdown
            # print("Dropdown expanded for Semester.")
            
            # Simulate pressing the down arrow key 3 times to reveal the options
            for _ in range(3):
                semester_dropdown.send_keys(Keys.ARROW_DOWN)
            # print("Pressed down arrow 3 times for Semester.")
            
            # After pressing the down key 3 times, hit Enter to select Fall
            semester_dropdown.send_keys(Keys.ENTER)
            print("Selected Fall as Semester.")
        except Exception as e:
            print(f"Error selecting Semester: {e}")

        # Set the flag to False after selecting for the first time
        is_first_iteration = False

    # Click Search Button
    search_button = driver.find_element(By.CLASS_NAME, "btn-primary")
    search_button.click()

    # Wait for results to load
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "table-bordered")))

    # Extract CGPA
    try:
        cgpa_element = driver.find_element(By.XPATH, "//td[contains(text(), 'Semester GPA')]/following-sibling::td")
        cgpa = cgpa_element.text
    except:
        cgpa = "Not Found"

    # Save CGPA in DataFrame
    df.at[index, "CGPA"] = float(cgpa) if cgpa != "Not Found" else None
    print(f"Student ID: {student_id}, CGPA: {cgpa}")

# Save updated DataFrame back to Excel
df.to_excel(file_path, index=False)

# Close the browser
driver.quit()
