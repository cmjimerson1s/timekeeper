import gspread
from google.oauth2.service_account import Credentials
import pandas as pd

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
    while True:
        names = SHEET.get_worksheet(0)
        data = names.col_values(1)
        list = ", ".join(data)
        print('Please choose the employee whose working hours you wish to view.')
        print(f'Current employees are {list}.')
        print('Please note, your choice is case sensitive.')

        while True:
            # This validates the input, ensureing inability to enter a blank input
            name_choice = input('Employee: ')
            if not name_choice:
                print('Please enter valid name.')
            else:
                break
            
        if validate_employee_name(list, name_choice):
            main_menu(name_choice)
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


def validate_menu_num(menu, choice):
    """
    Validates that the chosen menu number by the user matches current menu
    """
    if choice in menu:
        print("Correct")    
    else:
        print('Wrong')
        return False
    return True


def main_menu(name_choice):
    """
    Initializes the main menu for the user to choose what to do with selected employee
    """
    while True:
        menu_options = ['1', '2', '3', '4']
        print('Please chose one of the following options\n')
        print(f"1. View {name_choice}'s Hours\n")
        print(f"2. Edit {name_choice}'s Hours\n")
        print(f"3. Calculate {name_choice}'s Current Monthly Salary\n")
        print("4. Return to Employee Select\n")
        
        while True:
                # This validates the input, ensureing inability to enter a blank input
                main_menu_choice = input("Menu Number: ")
                if not main_menu_choice:
                    print('Please enter valid menu number.')
                else:
                    break

        if validate_menu_num(menu_options, main_menu_choice):
            menu_one(name_choice, main_menu_choice)
            break


def menu_one(name_choice, menu_choice):
    """
    Collects and displays all of the current time keeping data for selected employee
    """
    while True:
        print(f"Menu 1: Currently viewing {name_choice}'s Hours \n")
        names = SHEET.get_worksheet(0)
        data = names.col_values(1)
        x = data.index(name_choice)
        hours = SHEET.get_worksheet(x)
        info = pd.DataFrame(hours.get_all_records())
        print(info)

        while True:
            main_menu_return = input('Press Enter to return to Main Menu:')
            if not main_menu_return:
                main_menu(name_choice)
            else:
                print('If done, please press enter to return to main menu.')










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
