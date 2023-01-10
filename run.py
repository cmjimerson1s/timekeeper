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


def get_names():
    names = SHEET.get_worksheet(0)
    data = names.col_values(1)
    print(data)


def make_employee():
    SHEET.add_worksheet(title = 'Eddy', rows = 100, cols=20)



get_names()
make_employee()