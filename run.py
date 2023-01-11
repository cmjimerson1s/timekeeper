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
SHEET = GSPREAD_CLIENT.open('timekeeper')

NAMES = SHEET.get_worksheet(0)


def start_program():
    """
    Initilaizes the program requesting the employee user requires to view/edit"
    """
    names = SHEET.get_worksheet(0)
    data = names.col_values(1)
    list = ", ".join(data)
    print('Please choose the employee whose working hours you wish to view.')
    print(f'Current employees are {list}.')
    print('Please note, your choice is case sensitive.')

    employee_choice = input('Employee: ')

    if employee_choice in data:
        print(employee_choice)
    else:
        print('Not valid employee, please try again')

def add_new_sheet():
    """
    Adds new worksheet to spreadsheet
    """
    SHEET.add_worksheet(title = 'Frank', rows = 100, cols=20)


def add_new_name():
    NAMES.update('A4', 'Eddy')




start_program()
# add_new_name()
# get_names()
# add_new_sheet()
