# Employee Insight Survey Analyzer

Welcome to the Employee Insight Survey Analyzer! This Python application is designed to empower employers with the tools they need to conduct insightful surveys based on their existing employee data. With Employee Insight Survey Analyzer, employers can seamlessly analyze their employee data stored in Google Sheets, gain valuable insights, and generate comprehensive summaries.

Employee Insight Survey Analyzer is a python terminal program, which runs in the CI mock terminal on Heroku.
<br>

Click here to use the program here: [Employee Insight Survey Analyzer](https://employee-insights-b63786ebfbf5.herokuapp.com/)

<br>

![Program Screen](assets/media/main_image.png)

# Introduction
Managing your workforce as an employer is crucial to making well-informed decisions and cultivating a happy workplace. Employers may easily extract valuable insights from their current data pool by using the Employee Insight Survey Analyzer, which offers an intuitive interface for employee data analysis.

## How to Use

Upon running the program, you'll be presented with a main menu offering the following options:

1. **Generate Summary from Employee Google Sheet**: Retrieve survey data from the Google Sheet, analyze it, display summary in console and save the summary to a separate worksheet.
  
2. **Add New Employee to Employee Google Sheet**: Add new employee data to the Google Sheet.
  
3. **View Existing Employee Data from Employee Google Sheet**: View existing employee data stored in the Google Sheet.

To use the program, follow these steps:

1. **Using Program Options**:
   - **Generate Summary from Employee Google Sheet**:
     - Select option 1 from the main menu.
      ![options screen](assets/media/guide/option1_01.png)
     - The program will retrieve survey data from the Google Sheet named `employee_data`.
     - It will then perform analysis on the data, including counts of employees based on age and salary ranges, identifying the youngest and oldest employees, etc.
     - After analysis, the program will display the results in a tabular format.
    ![summary display](assets/media/guide/option1_02.png)
     - Finally, it will save the summary data to a separate worksheet named `employee_summary` within the same Google Sheet for future reference.
    ![summary](assets/media/guide/option1_04.png)

   - **Add New Employee to Employee Google Sheet**:
     - Choose option 2 from the main menu.
     ![options screen](assets/media/guide/option2_01.png)
     - Follow the prompts to enter the details of the new employee, including their name, age, and salary.
     - The program will validate the input to ensure correctness and completeness.
    ![validation image](assets/media/guide/option2_02.png)
     - Once validated, the new employee data will be added to the Google Sheet named `employee_data`.
    ![employee data](assets/media/guide/option2_03.png)

   - **View Existing Employee Data from Employee Google Sheet**:
     - Opt for option 3 from the main menu.
     - The program will retrieve existing employee data from the Google Sheet named `employee_data`.
     - It will display the data in a tabular format, showing the names, ages, and salaries of all employees currently stored in the sheet.
      ![employee data](assets/media/guide/option3_01.png)

### Flowchart


![Flowchart Image](assets/media/flow_chart.png)

## User Story

| Story Number | User Story                                                                                     | Description                                                                                                                                                                 |
|--------------|-----------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1            | As a user, I want to be able to analyze employee survey data stored in a Google Sheet         | So I can gain insights into employee demographics and trends.                                                                                                               |
| 2            | As a user, I want to add new employee data to the Google Sheet easily                          | So I can keep the employee database up-to-date.                                                                                                                              |
| 3            | As a user, I want to view existing employee data from the Google Sheet in a clear format       | So I can quickly understand the composition of our workforce.                                                                                                                |
| 4            | As a user, I want the program to validate input data for new employees                         | So I can ensure that accurate information is added to the employee database.                                                                                                 |
| 5            | As a user, I want the program to perform various analyses on the employee survey data          | Such as identifying the youngest and oldest employees, to help me understand the workforce distribution.                                                                     |
| 6            | As a user, I want the program to generate comprehensive summaries based on the survey data     | So I can present key findings to management and stakeholders.                                                                                                                |
| 7            | As a user, I want the program to be easy to use and navigate                                   | So that users with varying technical skills can utilize it effectively.                                                                                                       |
| 8            | As a user, I want the program to save analysis summaries to a separate worksheet within Google Sheet | So that historical data can be maintained for future reference.                                                                                                            |

## Features

The Employee Insight Survey Analyzer is designed to provide efficient analysis of survey data from employees stored in a Google Sheet. Here's a deeper look at its key features:

### 1. Data Analysis
   - **Comprehensive Analysis**: Utilizing the Pandas library, the application performs comprehensive analysis on employee data, including age and salary distributions. This allows employers to gain valuable insights into the demographics of their workforce and identify any salary trends.

### 2. Google Sheets Integration
   - **Seamless Data Retrieval**: Through the use of the `gspread` library and Google Sheets API, the application seamlessly retrieves survey data from the designated Google Sheet named `employee_data`. This integration ensures that the latest employee data is used for analysis.
   - **Adding New Employees**: Employers can easily add new employee data to the Google Sheet directly from the application. This ensures that the database remains up-to-date without the need for manual data entry.

### 3. User-Friendly Interface
   - **Intuitive Navigation**: The application provides a simple and intuitive menu-driven interface, allowing users to easily select and execute various options such as generating summaries, adding new employees, or viewing existing data.
   - **Error Handling**: Robust error handling mechanisms are implemented to validate input data. In case of any errors, informative error messages are displayed to guide users on how to rectify them, ensuring data accuracy and integrity.

### 4. Summary Saving
   - **Data Preservation**: Upon analysis, the application saves comprehensive summaries to a separate worksheet named `employee_summary` within the Google Sheet. This allows employers to maintain historical data and refer back to previous analysis results for future reference and comparison.
  
## Future Features

### 1. Export to CSV

- **Data Export**: Add functionality to export analysis results to CSV format.

### 2. Filtering Options

- **Segmented Analysis**: Provide filtering options for analysis results, allowing users to focus on specific area.


### 3. Feedback Mechanism

- **User Input Gathering**: Incorporate a feedback mechanism to gather user input and suggestions for further improvements to the application.

## Technologies and Libraries Used

The Employee Insight Survey Analyzer is built using the following technologies and libraries:

- **Python**: The core programming language used for development.
- **Google Sheets API**: Used to interact with Google Sheets for data retrieval and storage.
- **gspread**: Python library for accessing Google Sheets.
- **Pandas**: Data manipulation and analysis library used for processing survey data.
- **tabulate**: Python library for formatting tabular data for display.
- **google-auth**: Library for authenticating with Google services.
  
## Tools and Programs Used

During the development of this application, the following programs have been used:

- **Visual Studio Code**: Integrated Development Environment (IDE) used for writing and debugging code.
- **Lucid**: Tool used for creating diagrams and visual representations of system architecture.
- **Heroku**: Cloud platform used for deployment and hosting of the application.
- **Git**: Version control system used for tracking changes to the codebase.
- **GitHub**: Web-based hosting service for version control and collaboration.
- **Google Spreadsheet**: Online spreadsheet tool used for storing and managing survey data.
- **CI Python Linter**: Continuous integration tool used for Python linting and code quality checks.
  
## Data Modeling with Google Sheets

### Overview

In the Survey Analyzer application, Google Sheets is utilized as the primary data storage and management tool for employee survey data. The data modeling approach involves structuring the Google Sheets document to efficiently store and organize employee information.

### Schema Design

The Google Sheets document follows a tabular structure, with each row representing a unique employee record and each column representing different attributes of the employee data, such as name, age, and salary. The schema design ensures consistency and uniformity in the data format, facilitating easy retrieval and analysis.

### Worksheet Organization

The Google Sheets document consists of multiple worksheets, each serving a specific purpose in the data management process. For example:

- **Employees Worksheet**: This worksheet contains the main dataset of employee survey responses, including attributes such as name, age, and salary.
- **Summary Worksheet**: This worksheet is dedicated to storing analysis results and summary data generated by the Survey Analyzer application. It includes columns for different analysis metrics and their corresponding results.

### Data Manipulation

The Survey Analyzer application interacts with the Google Sheets document through the Google Sheets API, enabling seamless data manipulation and analysis. The application can read, write, and update data in the Google Sheets document, allowing for real-time synchronization and collaboration.

## Employee Data in Employees Worksheet

Below is an example of how employee survey data may be structured in the Google Sheets document:

| Name   | Age | Salary |
|--------|-----|--------|
| John   | 35  | 50000  |
| Alice  | 28  | 45000  |
| Bob    | 42  | 60000  |
| Emily  | 31  | 48000  |
| Sarah  | 26  | 42000  |

## Summary Data in Employees Summary Worksheet

Below is a representation of the summary data stored in the Summary Worksheet:

| Analysis                                          | Result |
|---------------------------------------------------|--------|
| Number of employees under 30 years               | 1      |
| Number of employees over 30 years                | 1      |
| Number of employees with salary under 20000      | 2      |
| Number of employees with salary over 20000       | 1      |
| The youngest age among all employees             | 18 years |
| The oldest age among all employees               | 50 years |
| Name of the oldest employee                      | John   |
| Name of the youngest employee                    | Ali    |
| Number of employees above age 30 with salary under 20000 | 1      |
| Total number of employees surveyed              | 3      |

This structured format allows for easy retrieval and analysis of summary data generated by the Survey Analyzer application.



## Testing

### Validator Testing

The Code Institute Python Linter confirms that the code is error-free.

![employee data](assets/media/linter.png)

## Manual Testing for Survey Analyzer

### Option 1: Generate Summary from Employee Google Sheet

| Test | Description | Expected Outcome | Result |
|------|-------------|------------------|--------|
| 1    | Valid Data | Ensure the Google Sheet contains valid employee data | Program successfully retrieves employee data, analyzes the data and Save summary to Google Sheet |
| 2    | Missing Columns | Remove one or more expected columns from the input data | Program detects missing columns and displays an error message |
| 3    | Non-Numeric Age | Enter non-numeric values for the 'Age' column | Program detects non-numeric values and displays an error message |
| 4    | Non-Numeric Salary | Enter non-numeric values for the 'Salary' column | Program detects non-numeric values and displays an error message |
| 5    | Missing Values | Introduce missing values in the input data | Program detects missing values and displays an error message |
| 6    | Analysis - Age Distribution | Analyze the data and check age distribution results | Program accurately calculates the age distribution |
| 7    | Analysis - Salary Distribution | Analyze the data and check salary distribution results | Program accurately calculates the salary distribution |
| 8    | Analysis - Youngest Employee | Verify the name of the youngest employee | Program correctly identifies the youngest employee |
| 9    | Analysis - Oldest Employee | Verify the name of the oldest employee | Program correctly identifies the oldest employee |
| 10   | Analysis - Employees under 30 with Salary < 20000 | Verify the count of employees under 30 with salary less than 20000 | Program accurately counts the employees meeting the criteria |
| 11   | Analysis - Total Employees Surveyed | Check the total count of employees surveyed | Program accurately counts the total number of employees |

### Option 2: Add New Employee to Employee Google Sheet

| Test | Description | Expected Outcome | Result |
|------|-------------|------------------|--------|
| 1    | Valid Data | Add a new employee with valid data | Program successfully adds the new employee to the Google Sheet |
| 2    | Invalid Data | Attempt to add a new employee with invalid data | Program detects invalid data and displays an error message |
| 3    | Google Sheet Update | Verify that the Google Sheet is updated after adding a new employee | Google Sheet reflects the addition of the new employee |

### Option 3: View Existing Employee Data from Employee Google Sheet

| Test | Description | Expected Outcome | Result |
|------|-------------|------------------|--------|
| 1    | Valid Data | Ensure the Google Sheet contains valid employee data | Program successfully retrieves and displays the existing employee data |

## Deployment

### Cloning & Forking
#### Fork
1. On GitHub.com, navigate to the [zohaibshahzadkhan/EmployeeInsights](https://github.com/zohaibshahzadkhan/EmployeeInsights) repository.
2. In the top-right corner of the page, click Fork.
3. By default, forks are named the same as their parent repositories. You can change the name of the fork to distinguish it further.
4. Add a description to your fork.
5. Click Create fork.

#### Clone
1. Above the list of files click the button that says 'Code'.
2. Copy the URL for the repository.
3. Open Terminal. Change the directory to the location where you want the cloned directory.
4. Type git clone, and then paste the URL
5. Press Enter.

### Local Deployment
1. Sign up to [Gitpod](https://gitpod.io/)
2. Download the Gitpod browser extension.
3. On GitHub.com, navigate to the [zohaibshahzadkhan/EmployeeInsights](https://github.com/zohaibshahzadkhan/EmployeeInsights) repository.
4. Above the list of files click the button that says 'Gitpod'.
5. Once open you will need to install the libraries, you can do this by typing "pip3 install -r requirements.txt" into the terminal
   
## Remote Deployment

The program can be deployed to Heroku. Follow these steps after forking/cloning the repository:

1. Create a new app on Heroku.
2. Choose a name for your app.
3. Go to the settings tab.
4. Scroll down to Config Vars and click on "Reveal Config Vars".
5. Add `CREDS` as the key and paste the content of the Google API creds file into the value field.
6. Add another config named `PORT` with the value `8000`.
7. Set the buildpacks to Python and Node.js in that order.
8. Link your Heroku app to your repository.
9. Click on Deploy.
10. Once deployed, the page will provide the URL to access the application.
11. The live link can be found here: [Employee Insight Survey Analyzer](https://employee-insights-b63786ebfbf5.herokuapp.com/)
    
## Credits and Acknowledgements

Code instutie for the deployment terminal - 
https://codeinstitute.net/


### Libraries and Tools

The Survey Analyzer application utilizes several libraries and tools to facilitate its functionality. I would like to extend our gratitude to the developers and contributors of the following:

- **Pandas**: Used for data manipulation and analysis.
- **gspread**: Utilized for accessing and modifying Google Sheets.
- **tabulate**: Employed for displaying data in a tabular format.
- **Google Sheets API**: Integrated for interaction with Google Sheets.
- **Google OAuth2 Library**: Enabled authentication for accessing Google Sheets.
- **Visual Studio Code**: The integrated development environment used for writing and testing the code.
- **Heroku**: Utilized for deploying the application to a remote server.
- **Git and GitHub**: Used for version control and collaboration during the development process.
- **Excel**: Used for manual testing and verification of data integrity.
- **Lucidchart**: Utilized for visualizing data models and workflows.
  
### Special Thanks

Special thanks to the Code Institute for providing guidance and resources that have helped in the development of this project. Additionally, I would like to express our appreciation to the Open Source community for their continuous support and contributions to the development ecosystem.






