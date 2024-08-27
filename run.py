# Importing libraries and apis.
import gspread
from google.oauth2.service_account import Credentials
from prettytable import PrettyTable
import os

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


def get_choice():
    """
    Get menu choice from user and check for valid response,
    if invalid throw an exception and repeat until valid response is given.
    """
    clear()
    while True:
        print(
        'Welcome to the Watch-o-Matic! '
        'Your helpful watch collection manager.\n'
        )
        print('Please enter one of the options below:\n')
        print('1 - View your current collection')
        print('2 - View your current wishlist')
        print('3 - Add a watch to the collection or wishlist\n')
        choice = input(
            'What would you like do to? (press 1,2, or 3 and press Enter):\n'
        )

        if validate_choice(choice):
            break

    return choice


def validate_choice(user_input):
    """
    Checks if users choice is within valid menu options.
    """
    try:
        if int(user_input) not in range(1,4):
            raise ValueError(
                f"Please enter either 1, 2, or 3. You entered {user_input}"
            )
        clear()
    except ValueError as e:
        print(f"Invalid choice: {e}, please try again.\n")
        clear()
        return False

    return True


def validate_continue(yes_or_no):
    """
    Checks for y or n value for continue question.
    """
    try:
        if (yes_or_no).lower() != 'y' or 'n':
            raise ValueError(
                f"Please enter either y or n. You entered {user_input}"
            )
        clear()
    except ValueError as e:
        print(f"Invalid choice: {e}, please try again.\n")
        clear()
        return False

    return True


def menu():
    menu_chosen = get_choice()
    if menu_chosen == '1':
        view_selection('owned','collection')
    elif menu_chosen == '2':
        view_selection('wishlist','wishlist')
    else:
        print('Add a watch has been chosen')


def view_selection(sheet_choice,collection):

    watches = SHEET.worksheet(sheet_choice)

    watch_data = watches.get_all_values()
    watch_titles = watch_data[0]

    watch_table = PrettyTable(watch_titles)
    for row in range(1,len(watch_data)):
        watch_table.add_row(watch_data[row])

    print(f'Here are the current watches in your {collection}:\n')
    print(watch_table,'\n')

    # Check for another action
    continue_check = input('Would you like to do anything else? (y/n):\n')
    if continue_check == 'y':
        menu()


def main():
    """
    Run all program functions
    """
    clear()
    menu()


main()
