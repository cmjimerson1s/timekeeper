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
NAME_CHOICE = ''


def start_program():
    """
    Initilaizes the program requesting the employee user requires to view/edit"
    """
    while True:
        global NAME_CHOICE
        names = SHEET.get_worksheet(0)
        data = names.col_values(1)
        list = ", ".join(data)
        print('Please choose the employee whose working hours you wish to view.')
        print(f'Current employees are {list}.')
        print('Please note, your choice is case sensitive.')

        while True:
            NAME_CHOICE = input('Employee: ')
            if not NAME_CHOICE:
                print('Please enter valid name.')
            else:
                break
                
        
        if validate_employee_name(list, NAME_CHOICE):
            main_menu()
            break



def validate_employee_name(names, choice):
    """
    Validates that the chosen name by the user matches current employees
    """
    if choice in names:
        print("Correct")
        
    else:
        print('Wrong')
        return False
    
    return True



def main_menu():
    """
    Initializes the main menu for the user to choose what to do with selected employee
    """
    print('Please chose one of the following options\n')
    print(f"1. View {NAME_CHOICE}'s Hours\n")
    print(f"2. Edit {NAME_CHOICE}'s Hours\n")
    print(f"3. View {NAME_CHOICE}'s Salary\n")
    print("4. Return to Employee Select")



start_program()

# add_new_name()
# get_names()
# add_new_sheet()

# def add_new_sheet():
#     """
#     Adds new worksheet to spreadsheet
#     """
#     SHEET.add_worksheet(title = 'Frank', rows = 100, cols=20)


# def add_new_name():
#     NAMES.update('A4', 'Eddy')
