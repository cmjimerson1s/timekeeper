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
        print('Main Menu \n')
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
            menu_selector(name_choice, main_menu_choice)
            break


def menu_one(name_choice):
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
            # This provides the return to the main menu function, still passing the initial chosen employee name
            main_menu_return = input('Press Enter to return to Main Menu:')
            if not main_menu_return:
                main_menu(name_choice)
            else:
                print('If done, please press enter to return to main menu.')


def menu_two(name_choice):
    """
    Collects and displays all the current time keeping data for selected employee
    Allows user to select an existing data, clockin, and clockout to edit
    """
    print(f"Menu 2: Currently viewing {name_choice}'s Hours\n")
    names = SHEET.get_worksheet(0)
    data = names.col_values(1)
    x = data.index(name_choice)
    hours = SHEET.get_worksheet(x)
    info = pd.DataFrame(hours.get_all_records())
    print(info)
    edit_choice = (int(input('What entry would you like to edit(Use number in far left column): '))) + 2

    if edit_choice == 3:
        display_choice = hours.row_values(edit_choice)
        print(display_choice)
        get_edit_row(edit_choice, hours)


    
def menu_selector(name_choice, main_menu_choice):
    """
    Runs to direct user towards the apporiate menu of their selection
    """
    if main_menu_choice == "1":
        menu_one(name_choice)
    else:
        menu_two(name_choice)

def get_edit_row(row_choice, sheet_choice):
    row_updated = str(row_choice)
    
    new_date = str(input("Enter Date: "))
    new_clockin = str(input("Enter Clock-in: "))
    new_clockout = str(input("Enter Clock-out: "))

    sheet_choice.update(f'A{row_updated}', new_clockout)


# def update_cells_hours(date, clockin, clockou, row, sheet):
#     sheet.update(f'A{row_updated}





start_program()

# class TimeEdit:

#     def __init__(self, date, clockin, clockout):
#         self.date = date
#         self.clockin = clockin
#         self.clockout = clockout

# new_date = input("Enter new date: ")
# new_clockin = input("Enter new clock-in: ")
# new_clockout = input("Enter new clock-out: ")
























































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
