# Importing libraries and apis.
import gspread
from google.oauth2.service_account import Credentials
from prettytable import PrettyTable
import os
import time

# Defining constants for accessing google sheet data.
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('watch-o-matic')


def clear():
    """
    Clear function to clean-up the terminal so things don't get messy.
    """
    os.system("cls" if os.name == "nt" else "clear")


def validate(user_input, check, request):
    """
    Checks if users choice is within valid menu options.
    """
    try:
        if user_input.lower() not in check:
            raise ValueError(
                f"\033[31m{user_input}\033[0m entered. {request}"
            )
    except ValueError as e:
        print(f"\nInvalid choice: {e}.\n")
        return False
    clear()
    return True


def get_choice():
    """
    Get menu choice from user and check for valid response,
    if invalid throw an exception and repeat until valid response is given.
    """
    print('Please enter one of the options below:\n')
    print('1 - View your current collection')
    print('2 - View your current wishlist')
    print('3 - Add a watch to the collection or wishlist\n')
    while True: 
        choice = input(
            'What would you like do to? (press 1,2, or 3 and press Enter):\n'
        )
        requested = 'Please enter either 1, 2, or 3'
        if validate(choice, ['1','2','3'], requested):
            break

    return choice


def menu():
    """
    Calls correct function depending on users choice from menu.
    """
    menu_chosen = get_choice()
    if menu_chosen == '1':
        view_selection('owned','collection')
    elif menu_chosen == '2':
        view_selection('wishlist','wishlist')
    else:
        print('Add a watch has been chosen')


def continue_app():
    """
    See if the user wants to go back to the menu to do something else and
    validate response. If invalid throw an exception and repeat until valid
    response is given. 
    """
    while True:
        continue_check = input('Would you like to do anything else? (y/n):\n')
        requested = 'Please enter y or n'
        if validate(continue_check, ['y','n'], requested):
            break

    if continue_check.lower() == 'y':
        menu()
    else:
        print('Thank you for using Watch-o-Matic. The app will now close...')
        time.sleep(3)

def view_selection(sheet_choice,collection):
    """
    Displays either current watch collection or wishlist
    in table format using PrettyTable library.
    """
    watches = SHEET.worksheet(sheet_choice)

    watch_data = watches.get_all_values()
    watch_titles = watch_data[0]

    watch_table = PrettyTable(watch_titles)
    for row in range(1,len(watch_data)):
        watch_table.add_row(watch_data[row])

    print(f'Here are the current watches in your {collection}:\n')
    print(watch_table,'\n')

    continue_app()


def main():
    """
    Run all program functions
    """
    clear()
    print(
        'Welcome to the Watch-o-Matic! '
        'Your helpful watch collection manager.\n'
        )
    menu()


main()
