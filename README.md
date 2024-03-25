# Employee Insight Survey Analyzer

Welcome to the Employee Insight Survey Analyzer! This Python application is designed to empower employers with the tools they need to conduct insightful surveys based on their existing employee data. With Employee Insight Survey Analyzer, employers can seamlessly analyze their employee data stored in Google Sheets, gain valuable insights, and generate comprehensive summaries.

Employee Insight Survey Analyzer is a python terminal program, which runs in the CI mock terminal on Heroku.
<br>

Click here to use the program here: [Employee Insight Survey Analyzer](https://employee-insights-b63786ebfbf5.herokuapp.com/)

<br>

![Program Screen](assets/media/main_image.png)

# Introduction
Comprehending your workforce as an employer is crucial to making well-informed decisions and cultivating a happy workplace. Employers may easily extract valuable insights from their current data pool by using the Employee Insight Survey Analyzer, which offers an intuitive interface for employee data analysis.

# Employee Insight Survey Analyzer

Welcome to the Employee Insight Survey Analyzer! This Python application is designed to help employers analyze survey data from their employees stored in a Google Sheet. The program offers various options to analyze data, add new employee information, and view existing employee data.

## How to Use

Upon running the program, you'll be presented with a main menu offering the following options:

1. **Generate Summary from Employee Google Sheet**: Retrieve survey data from the Google Sheet, analyze it, display summary in console and save the summary to a separate worksheet.
  
2. **Add New Employee to Employee Google Sheet**: Add new employee data to the Google Sheet.
  
3. **View Existing Employee Data from Employee Google Sheet**: View existing employee data stored in the Google Sheet.

4. **Exit**: Exit the program.

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

<br>

![Flowchart Image](assets/media/flow_chart.png)