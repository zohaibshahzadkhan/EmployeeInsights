import pandas as pd
import gspread
from tabulate import tabulate
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('employee_data')

def analyze_data(employees_data_frame):
    """
    Analyze the survey data and return the results.

    Args:
        employees_data_frame (DataFrame): DataFrame containing the survey data.

    Returns:
        dict: Analysis results.
    """

    # Validate input data
    if not validate_input_data(employees_data_frame):
      print("Input data validation failed. Exiting program.")
      return
    
    try:
        
        # Drop rows with NaN values
        employees_data_frame.dropna(subset=['Age', 'Salary'], inplace=True)

        # Analysis results
        analysis_results = {
            'Number of employees under 30 years': len(employees_data_frame[employees_data_frame['Age'] < 30]),
            'Number of employees over 30 years': len(employees_data_frame[employees_data_frame['Age'] > 30]),
            'Number of employees with salary under 20000': len(employees_data_frame[employees_data_frame['Salary'] < 20000]),
            'Number of employees with salary over 20000': len(employees_data_frame[employees_data_frame['Salary'] > 20000]),
            'The youngest age among all employees': f"{employees_data_frame['Age'].min()} years",
            'The oldest age among all employees': f"{employees_data_frame['Age'].max()} years",
            'Name of the oldest employee': employees_data_frame.sort_values(by='Age', ascending=False).iloc[0]['Name'],
            'Name of the youngest employee': employees_data_frame.sort_values(by='Age', ascending=True).iloc[0]['Name'],
            'Number of employees above age 30 with salary under 20000': len(employees_data_frame[(employees_data_frame['Age'] > 30) & (employees_data_frame['Salary'] < 20000)]),
            'Total number of employees surveyed': len(employees_data_frame)

        }
        return analysis_results
    except Exception as e:
        print(f"An error occurred during data analysis: {str(e)}")
        return None

def validate_input_data(employees_data_frame):
    """
    Validate the input data before analysis.

    Args:
        employees_data_frame (DataFrame): DataFrame containing the survey data.

    Returns:
        bool: True if validation succeeds, False otherwise.
    """
    # Check if expected columns are present
    expected_columns = ['Name', 'Age', 'Salary']
    if not all(col in employees_data_frame.columns for col in expected_columns):
        print("Error: Missing expected columns in input data.")
        return False
    
    # Validate 'Age' and 'Salary' columns
    try:
        employees_data_frame['Age'] = pd.to_numeric(employees_data_frame['Age'], errors='raise')
        employees_data_frame['Salary'] = pd.to_numeric(employees_data_frame['Salary'], errors='raise')
    except ValueError:
        print("Error: 'Age' and 'Salary' columns must contain numerical data.")
        return False
    
    # Check for missing or invalid values
    if employees_data_frame.isnull().values.any():
        print("Error: Input data contains missing values.")
        return False
    
    return True

def display_results(analysis_results):
    """
    Display the analysis results in a table format.

    Args:
        analysis_results (dict): Analysis results.
    """
    try:
        headers = ["Analysis", "Result"]
        rows = [[key, value] for key, value in analysis_results.items()]
        print(tabulate(rows, headers=headers, tablefmt="grid"))
    except Exception as e:
        print(f"An error occurred while displaying results: {str(e)}")

def save_summary_to_sheet(summary, sheet_name, worksheet_name):
    """
    Save the summary to a Google Sheet.

    Args:
        summary (dict): Summary to be saved.
        sheet_name (str): Name of the Google Sheet.
        worksheet_name (str): Name of the worksheet to which the summary will be saved.
    """
    try:
        print("Saving results to employees_summary Google worksheet")
        # Open the Google Sheet
        sheet = GSPREAD_CLIENT.open(sheet_name)

        # Select the worksheet
        worksheet = sheet.worksheet(worksheet_name)

        # Clear existing content
        worksheet.clear()

        # Convert the summary to a list of lists
        rows = [["Analysis", "Result"]] + [[key, value] for key, value in summary.items()]

        # Resize worksheet
        worksheet.resize(rows=len(rows), cols=2)

        # Update the worksheet with the summary data
        cell_list = worksheet.range(f"A1:B{len(rows)}")
        for cell in cell_list:
            cell.value = rows[cell.row - 1][cell.col - 1]
        worksheet.update_cells(cell_list)

        print("Summary saved to Google Sheet successfully.")
    except Exception as e:
        print(f"An error occurred while saving the summary to Google Sheet: {str(e)}")

def main():
    """
    Run all program functions
    """
    employees = SHEET.worksheet('employees')
    employees_data = employees.get_all_values()

    try:
        # Convert employees_data to DataFrame
        employees_data_frame = pd.DataFrame(employees_data[1:], columns=employees_data[0])
 
        # Analyze data
        analysis_results = analyze_data(employees_data_frame)

        if analysis_results is None:
            print("Analysis could not be performed due to missing or invalid data.")
            return
        
        # Display analysis results
        display_results(analysis_results)

        # Save summary to Google Sheet
        save_summary_to_sheet(analysis_results, "employee_data", "employees_summary")


    except Exception as e:
        print(f"An error occurred: {str(e)}")

print("Welcome to Employee Insight Survey Analyzer")
main()