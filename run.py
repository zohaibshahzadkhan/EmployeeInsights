import pandas as pd
import gspread
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
    try:
        # Convert 'Age' and 'Salary' columns to numeric
        employees_data_frame['Age'] = pd.to_numeric(employees_data_frame['Age'], errors='coerce')
        employees_data_frame['Salary'] = pd.to_numeric(employees_data_frame['Salary'], errors='coerce')

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
        print(analysis_results)
        
        if analysis_results is None:
            print("Analysis could not be performed due to missing or invalid data.")
            return

    except Exception as e:
        print(f"An error occurred: {str(e)}")

print("Welcome to Employee Insight Survey Analyzer")
main()