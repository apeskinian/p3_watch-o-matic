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
    print('What would you like do to?\n')
    print('1 - View your current collection')
    print('2 - View your current wishlist')
    print('3 - Add a watch to the collection or wishlist\n')
    while True: 
        choice = input(
            'Please enter \033[32m1\033[0m,'
            ' \033[32m2\033[0m,' 
            'or \033[32m3\033[0m:\n'
        )
        requested = 'Please enter 1, 2, or 3'
        if validate(choice, ['1','2','3'], requested):
            break

    return choice


def menu():
    """
    Calls correct function depending on users choice from menu.
    """
    menu_chosen = get_choice()
    if menu_chosen == '1':
        view_selection('collection')
    elif menu_chosen == '2':
        view_selection('wishlist')
    else:
        add_watch()


def continue_app():
    """
    See if the user wants to go back to the menu to do something else and
    validate response. If invalid throw an exception and repeat until valid
    response is given. 
    """
    while True:
        continue_check = input(
            'Would you like to do anything else? ' 
            '(\033[32my\033[0m/\033[32mn\033[0m):\n'
        )
        requested = 'Please enter y or n'
        if validate(continue_check, ['y','n'], requested):
            break

    if continue_check.lower() == 'y':
        menu()
    elif continue_check.lower() == 'n':
        print('Thank you for using Watch-o-Matic. The app will now close...')

def view_selection(sheet_choice):
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

    print(f'Here are the current watches in your {sheet_choice}:\n')
    print(watch_table.get_string(sortby="Make"),'\n')

    continue_app()

def get_watch_detail(detail, is_movement):
    """
    Get user inputs for adding a new watch which includes:
    1 - Make of watch (string input validated by user)
    2 - Model of watch (string input validated by user)
    3 - Movement of watch (options with input validated by app)
    """
    if is_movement:
        print('Please select the movement:\n')
        print('1 - Quartz')
        print('2 - Manual')
        print('3 - Automatic\n')
        while True:
            movement_choice = input(
                'Please enter \033[32m1\033[0m, '
                '\033[32m2\033[0m or \033[32m3\033[0m\n'
            )
            requested = 'Please enter 1, 2 or 3'
            if validate(movement_choice, ['1','2','3'], requested):
                if movement_choice == '1':
                    return 'Quartz'
                elif movement_choice == '2':
                    return 'Manual'
                elif movement_choice == '3':
                    return 'Automatic'
    else:
        while True:
            watch_detail = input(f'Please enter the {detail} of the watch:\n')
            while True:
                user_confirm = input(
                    f'\nYou entered \033[33m{watch_detail.title()}\033[0m, '
                    'is this correct?: (\033[32my\033[0m/\033[32mn\033[0m)'
                )
                requested = 'Please enter y or n'
                if validate(user_confirm, ['y','n'], requested):
                    if user_confirm.lower() == 'y':
                        return watch_detail.title()
                    elif user_confirm.lower() == 'n':
                        break


def add_watch():
    """
    Adds a watch to either the collection or wishlist.
    User is asked which list to add to first with validation.
    Then watch details are retrieved from get_watch function calls.
    Returned watch details are then presented to user for confirmation.
    """
    # Getting list to update
    print('Please choose which list to add to:\n')
    print('1 - Collection')
    print('2 - Wishlist\n')

    while True:
        list_selection = input(
            'Please enter \033[32m1\033[0m or \033[32m2\033[0m:\n'
        )
        requested = 'Please enter 1 or 2'
        if validate(list_selection, ['1','2'], requested):
            break
    
    if list_selection == '1':
        print('Adding watch to current Collection:\n')
        sheet_to_update = 'collection'
    else:
        print('Adding watch to wishlist:\n')
        sheet_to_update = 'wishlist'

    # Getting watch details
    watch_make = get_watch_detail('make', False)
    watch_model = get_watch_detail('model', False)
    watch_movement = get_watch_detail('movement', True)

    print(
        f'Watch-o-Matic will add the following to your {sheet_to_update}:\n')
    print(f'Make:     \033[33m{watch_make}\033[0m')
    print(f'Model:    \033[33m{watch_model}\033[0m')
    print(f'Movement: \033[33m{watch_movement}\033[0m\n')
    
    while True:
        final_confirm = input(
            'Enter \033[32my\033[0m to accept or \033[32mn\033[0m to cancel:\n'
        )
        requested = 'Please enter y to accept or n to cancel'
        if validate(final_confirm, ['y','n'], requested):
            if final_confirm.lower() == 'y':
                push_data_to_sheet(
                    watch_make,
                    watch_model,
                    watch_movement,
                    sheet_to_update
                )
                break
            elif final_confirm.lower() == 'n':
                start_over()
                break
                

def start_over():
    print('Watch addition cancelled. Would you like to:\n')
    print('1 - Try to add the watch again.')
    print('2 - Go back to the main menu.')
    print('3 - Quit the Watch-o-Matic.\n')
    while True:
        start_over_check = input(
            'Please enter \033[32m1\033[0m, '
            '\033[32m2\033[0m or '
            '\033[32m3\033[0m:\n'
        )
        requested = 'Please enter 1, 2 or 3'
        if validate(start_over_check, ['1','2','3'], requested):
            break

    if start_over_check == '1':
        add_watch()
    elif start_over_check == '2':
        menu()
    elif start_over_check == '3':
        print('Thank you for using Watch-o-Matic. The app will now close...')


def push_data_to_sheet(make, model, movement, sheet):
    print(f'Adding watch to {sheet}...\n')
    data = [make, model, movement]
    worksheet = SHEET.worksheet(sheet)
    worksheet.append_row(data)
    print(f'New watch successfully added to {sheet}. Loading {sheet}...\n')
    view_selection(sheet)


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
