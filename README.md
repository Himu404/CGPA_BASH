# CGPA Scraping Script

This Python script automates the process of scraping CGPA information from **Uttara University Online Result Portal**. It uses **Selenium** for web automation to interact with the website, submits the **Student ID** and **Date of Birth**, selects the **Academic Year** and **Semester**, and extracts the CGPA of each student. The data is then saved back into the same Excel file from which it was read.

## Prerequisites

Before running the script, make sure you have the following installed:

- **Python 3.12+**
- **Selenium** library
- **Pandas** library
- **ChromeDriver** (compatible with your version of Google Chrome)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Himu404/CGPA_BASH.git
   cd CGPA_BASH

## How It Works

### Script Overview

1. **Reading Input**: The script reads the **Student ID** and **Date of Birth** from an Excel file.
2. **Interacting with the Website**: The script uses **Selenium** to open the **Uttara University Online Result Portal** and enter the data in the form fields.
3. **Dropdown Handling**: 
   - **Academic Year** and **Semester** dropdowns are selected by simulating clicks and keypresses. The script selects **2024** as the **Academic Year** and **Fall** as the **Semester** for the first time.
   - After selecting the dropdown options, the form is submitted to fetch the CGPA.
4. **Saving Data**: The script extracts the **CGPA** for each student and saves it back into the same Excel file under the **CGPA** column.

### How Dropdowns Work

The script interacts with the dropdown buttons by simulating clicks and keyboard actions:

1. **Academic Year**:
   - The script first clicks on the Academic Year dropdown to expand the options.
   - It simulates pressing the **down arrow** key three times to scroll through the dropdown options.
   - After selecting the desired option (2024), the script submits the form.

2. **Semester**:
   - Similarly, the **Semester** dropdown is clicked and the down arrow is pressed to select the desired semester (**Fall**).

### Form Fields and Interaction:

The form consists of the following fields:

1. **Student ID**: The script types the Student ID into the input field.
2. **Date of Birth**: The script enters the student's date of birth in the required format.
3. **Academic Year**: The script selects **2024**.
4. **Semester**: The script selects **Fall**.
5. **Search Button**: After all data is entered, the script clicks the search button to retrieve the CGPA.

### Output:

- After submitting the form, the script waits for the results and extracts the **CGPA**. 
- The **CGPA** is then saved in the **CGPA** column of the Excel file for the corresponding student.

## Example Excel Format

The Excel file (`hack.xlsx`) must have the following structure to be read by the script:

| Student ID | Date of Birth |
|------------|---------------|
| 2233083547 | 2001-01-01    |
| 2233081548 | 2001-02-01    |
| 2233081464 | 2001-03-01    |
| ...        | ...           |

- **Student ID**: This column should contain the unique ID for each student.
- **Date of Birth**: This column should contain the **Date of Birth** in the format `YYYY-MM-DD` for each student.

### Output Column:

After running the script, the Excel file will be updated with an additional column for **CGPA**:

| Student ID | Date of Birth | CGPA   |
|------------|---------------|--------|
| 2233083547 | 2001-01-01    | 3.11   |
| 2233081548 | 2001-02-01    | 3.45   |
| 2233081464 | 2001-03-01    | 2.98   |
| ...        | ...           | ...    |

- **CGPA**: The script will populate this column with the student's CGPA retrieved from the online portal.

