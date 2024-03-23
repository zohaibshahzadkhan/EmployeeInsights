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

def main():
    """
    Run all program functions
    """
    employees = SHEET.worksheet('employees')
    employees_data = employees.get_all_values()

    try:
        # Convert employees_data to DataFrame
        employee_data_frame = pd.DataFrame(employees_data[1:], columns=employees_data[0])
        print(employee_data_frame)

    except Exception as e:
        print(f"An error occurred: {str(e)}")

print("Welcome to Employee Insight Survey Analyzer")
main()