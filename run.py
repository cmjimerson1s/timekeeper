import gspread
from google.oauth2.service_account import Credentials
import pandas as pd
from datetime import datetime

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
            name_choice = input('Employee: \n')
            if not name_choice:
                print('Please enter valid name.')
            else:
                break
            
        if validate_employee_name(list, name_choice):
            main_menu(name_choice)
            break


def main_menu(name_choice):
    """
    Initializes the main menu for the user to choose what to do with selected employee
    """
    while True:
        menu_options = ['1', '2', '3', '4', '5']
        print('Main Menu \n')
        print('Please chose one of the following options\n')
        print(f"1. View {name_choice}'s Hours\n")
        print(f"2. Edit {name_choice}'s Hours\n")
        print(f"3. Add Entry to {name_choice}'s Hours\n")
        print(f"4. Calculate {name_choice}'s Current Monthly Salary\n")
        print("5. Return to Employee Select\n")
        
        while True:
            # This validates the input, ensureing inability to enter a blank input
            main_menu_choice = input("Menu Number: \n")
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
        record_set = hours.get_all_records()
        new_list = sorted(record_set, key=lambda d: d['Date'])
        info = pd.DataFrame(new_list)
        print(info)

        while True:
            # This provides the return to the main menu function, still passing the initial chosen employee name
            main_menu_return = input('Press Enter to return to Main Menu: \n')
            if not main_menu_return:
                main_menu(name_choice)
            else:
                print('If done, please press enter to return to main menu.')


def menu_two(name_choice):
    """
    Collects and displays all the current time keeping data for selected employee
    Allows user to select an existing data, clockin, and clockout to edit
    """
    while True:
        print(f"Menu 2: Currently viewing {name_choice}'s Hours\n")
        print("To return to main menu, enter 'Return'.")
        names = SHEET.get_worksheet(0)
        data = names.col_values(1)
        x = data.index(name_choice)
        hours = SHEET.get_worksheet(x)
        info = pd.DataFrame(hours.get_all_records())   
        list_length = hours.get_all_values()
        print(info)

        while True:
            # This validates the input, ensureing inability to enter a blank input
            string_edit_choice = str(input('What entry would you like to edit(Use number in far left column): \n'))
            if not string_edit_choice:
                print('Please enter valid menu number.')
            elif string_edit_choice == "Return":
                main_menu(name_choice)
            else:
                break

        if validate_menue_two_edit_choice(string_edit_choice, list_length):
            edit_choice = (int(string_edit_choice))+2
            display_choice = hours.row_values(edit_choice)
            print(display_choice)
            get_edit_row(edit_choice, hours, name_choice)




def menu_three(name_choice):
    names = SHEET.get_worksheet(0)
    data = names.col_values(1)
    x = data.index(name_choice)
    hours = SHEET.get_worksheet(x)

    print('Please enter the date, clock-in, and clock-out you would like to add. \n')
    add_new_hours(hours)
    

def menu_four(name_choice):
    monthly_total = []
    print('This is mene four')
    names = SHEET.get_worksheet(0)
    data = names.col_values(1)
    x = data.index(name_choice)
    hours = SHEET.get_worksheet(x)
    clockin_list = hours.col_values(2)
    clockin_list.pop(0)
    clockout_list = hours.col_values(3)
    clockout_list.pop(0)
    list_data = hour_combine(clockin_list, clockout_list)
    final_total = run_this(list_data, monthly_total)
    print(f"{name_choice}'s total hours are: {final_total}")


# Below this comment are the main functions called in the menus above
def menu_selector(name_choice, main_menu_choice):
    """
    Runs to direct user towards the apporiate menu of their selection
    """
    if main_menu_choice == "1":
        menu_one(name_choice)
    elif main_menu_choice == "2":
        menu_two(name_choice)
    elif main_menu_choice == "3":
        menu_three(name_choice)
    elif main_menu_choice == "4":
        menu_four(name_choice)
    elif main_menu_choice == "5":
        start_program()


def get_edit_row(row_choice, sheet_choice, name_choice):
    """
    This collects the selected row to be edited by the user
    """
    row_updated = str(row_choice)
    new_date = str(input("Enter Date: \n"))
    new_clockin = str(input("Enter Clock-in: \n"))
    new_clockout = str(input("Enter Clock-out: \n"))

    update_cells_hours(new_date, new_clockin, new_clockout, row_updated, sheet_choice, name_choice)


def update_cells_hours(date, clockin, clockout, row, sheet, name_choice):
    """
    This function updates the individual cells of the row
    that as been selected to be edited by the user
    """
    sheet.update(f'A{row}', date)
    sheet.update(f'B{row}', clockin)
    sheet.update(f'C{row}', clockout)
    print("Updating date and hours...\n")
    print("Returning to Menu 2. Please wait...\n")
    menu_two(name_choice)


def add_new_hours(worksheet):
    """
    This asks the user to provide the new date, clock-in
    and clock-out that they wish to add to the selected users
    list
    """
    add_date = str(input('Date: \n'))
    if validate_date(add_date):
        add_clockin = str(input('Clock-in: \n'))
        add_clockout = str(input('Clock-out: \n'))
        addition_data = [add_date, add_clockin, add_clockout]

        worksheet.append_row(addition_data)


def hour_combine(clockin, clockout):
    """
    Combines the two collected lists from menu_four into one list
    """
    list_one = clockin
    list_two = clockout
    combo_list = []

    for first, second in zip(list_one, list_two):
        math_list = first + ',' + second
        combo_list.append(math_list)
    return combo_list


# Below this line is the subfunction, and all related functions, to calculate the monthly hours
def loop_split(combo_list, round, monthly_total):
    """
    This takes the list of combined clock-in and clock-outs and 
    splits them into the start and end time for the pair
    """
    list_sep = combo_list[round].split(',')
    start_sep = list_sep[0]
    end_sep = list_sep[1]

    return start_sep, end_sep, monthly_total


def time_transform(start, end, monthly_total):
    """
    This takes the clock-in and clock out strings 
    and converts the hours and minutes of each
    into intergers to be used for calculations later
    """
    start_sep = start.split(':')
    start_hour = int(start_sep[0])
    start_min = int(start_sep[1])
    end_sep = end.split(':')
    end_hour = int(end_sep[0])
    end_min = int(end_sep[1])

    return start_hour, start_min, end_hour, end_min, monthly_total

def time_calculation(start_hour, start_min, end_hour, end_min, monthly_total):
    """
    This takes the new intergers of the clockin/out
    times and calculates the total hours and minutes worked
    by first calculating the minutes, then the hours, and 
    finally converts the hours to minutes and then 
    total minutes back into hours as a decimal, ex: 1.75 etc
    """
    total_minuts = (end_min - start_min)
    if total_minuts < 0:
        total_minuts  = total_minuts * -1
    total_hours = end_hour - start_hour
    calc_comb = (total_hours * 60) + total_minuts
    calc_total = calc_comb / 60

    monthly_total.append(calc_total)


def run_this(list_data, monthly_total):
    """
    This is the subfunction that runs a loop through the
    collected and combined hours list (clock-in and clock-out) 
    to calculate the total hours worked for the month.
    """
    rotation = -1
    for pair in list_data:
        rotation += 1
        res_one, res_two, res_three = loop_split(list_data, rotation, monthly_total)
        res_four, res_five, res_six, res_seven, res_eight = time_transform(res_one, res_two, res_three)
        time_calculation(res_four, res_five, res_six, res_seven, res_eight)    
    final_total = (sum(monthly_total))

    return final_total


# Below this comment sits all the validation 
# functions for the above menu functions
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

def validate_menue_two_edit_choice(edit_choice, list_of_hours):
    choice_check = (int(edit_choice) + 1)
    if choice_check < len(list_of_hours):
        print("Valid entry")
    else:
        print("Invalid entry. Try again.")
        return False
    return True

def validate_date(date):
    try:
        dateObject = datetime.strptime(date, '%Y-%m-%d')
        return True
    except ValueError:
        return False











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
