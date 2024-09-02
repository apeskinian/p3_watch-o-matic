# Importing libraries and apis.
import gspread
from google.oauth2.service_account import Credentials
from prettytable import PrettyTable
import os
import time
import getpass
import math

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

# Colours for text highlighting.
ERROR_COLOUR = '\033[31m'  # Red
CHOICE_COLOUR = '\033[32m'  # Green
CHECK_COLOUR = '\033[33m'  # Yellow
CLEAR = '\033[39m'  # Clear


# Defining the watch class.
class Watch:
    """
    A watch object which is passed when adding a new watch to either the
    current collection or the wishlist.
    """
    def __init__(self, make, model, movement, sheet):
        self.make = make
        self.model = model
        self.movement = movement
        self.sheet = sheet

    def add_to_sheet(self):
        print(f'Adding watch to {self.sheet}...\n')
        worksheet = SHEET.worksheet(self.sheet)
        worksheet.append_row([self.make, self.model, self.movement])
        print(
            f'New watch successfully added to {self.sheet}. '
            f'Loading {self.sheet}...\n'
        )
        view_selection(self.sheet)


# Functions for app.
def clear():
    """
    Clears the terminal to keep a clean asthetic.
    """
    os.system("cls" if os.name == "nt" else "clear")


def validate(user_input, check, request):
    """
    Checks if users choice is within valid menu options.
    Highlights erroneous inputs in red.
    Invalid inputs raise an error and throws an exception.
    Repeats until valid input is given.
    """
    try:
        if user_input.lower() == '':
            raise ValueError(
                f'no input was given. {request}'
            )
        elif user_input.lower() not in check:
            raise ValueError(
                f'{ERROR_COLOUR}{user_input}{CLEAR} entered. {request}'
            )
    except ValueError as e:
        print(f'\nInvalid input: {e}.\n')
        return False
    clear()
    return True


def start_over():
    """
    Options given to user when they do not confirm addition of new watch data.
    They can repeat the addition process, return to the menu or quit.
    All inputs are validated.
    """
    print('Watch addition cancelled. Would you like to:\n')
    time.sleep(0.2)
    print('1 - Try to add the watch again.')
    time.sleep(0.2)
    print('2 - Go back to the main menu.')
    time.sleep(0.2)
    print('3 - Quit the Watch-o-Matic.\n')
    time.sleep(0.2)
    while True:
        start_over_check = input(
            f'Please enter {CHOICE_COLOUR}1{CLEAR}, '
            f'{CHOICE_COLOUR}2{CLEAR} or '
            f'{CHOICE_COLOUR}3{CLEAR}:\n'
        )
        requested = 'Please enter 1, 2 or 3'
        if validate(start_over_check, ['1', '2', '3'], requested):
            break

    match start_over_check:
        case '1':
            add_watch()
        case '2':
            menu()
        case '3':
            print(
                'Thank you for using Watch-o-Matic. The app will now close...'
            )
        case _:
            # This should never happen
            print('I have a bad feeling about this...')


def get_watch_detail(detail, is_movement):
    """
    Get user inputs for adding a new watch which includes:
    1 - Make of watch (string input validated by user)
    2 - Model of watch (string input validated by user)
    3 - Movement of watch (options with input validated by app)
    """
    # If the detail is for the movement show the options available.
    if is_movement:
        print('Please select the movement:\n')
        time.sleep(0.2)
        print('1 - Quartz')
        time.sleep(0.2)
        print('2 - Manual')
        time.sleep(0.2)
        print('3 - Automatic\n')
        time.sleep(0.2)
        while True:
            movement_choice = input(
                f'Please enter {CHOICE_COLOUR}1{CLEAR}, '
                f'{CHOICE_COLOUR}2{CLEAR} or {CHOICE_COLOUR}3{CLEAR}\n'
            )
            requested = 'Please enter 1, 2 or 3'
            if validate(movement_choice, ['1', '2', '3'], requested):
                if movement_choice == '1':
                    return 'Quartz'
                elif movement_choice == '2':
                    return 'Manual'
                elif movement_choice == '3':
                    return 'Automatic'
    # If the detail is not movement, prompt user for text input.
    else:
        while True:
            watch_detail = input(f'Please enter the {detail} of the watch:\n')
            while True:
                # Get user to validate their own input, double check empties.
                if watch_detail == '':
                    user_confirm = input(
                        f'\nYou did not enter anything for the {detail}, '
                        f'is this correct? ({CHOICE_COLOUR}y{CLEAR}/'
                        f'{CHOICE_COLOUR}n{CLEAR}):\n'
                    )
                else:
                    user_confirm = input(
                        f'\nYou entered {CHECK_COLOUR}{watch_detail}{CLEAR}, '
                        f'is this correct? ({CHOICE_COLOUR}y{CLEAR}/'
                        f'{CHOICE_COLOUR}n{CLEAR}):\n'
                    )
                requested = 'Please enter y or n'
                if validate(user_confirm, ['y', 'n'], requested):
                    if user_confirm.lower() == 'y':
                        return watch_detail
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
    time.sleep(0.2)
    print('1 - Collection')
    time.sleep(0.2)
    print('2 - Wishlist\n')
    time.sleep(0.2)

    while True:
        list_selection = input(
            f'Please enter {CHOICE_COLOUR}1{CLEAR} or '
            f'{CHOICE_COLOUR}2{CLEAR}:\n'
        )
        requested = 'Please enter 1 or 2'
        if validate(list_selection, ['1', '2'], requested):
            break

    if list_selection == '1':
        print('Adding watch to current Collection:\n')
        sheet_to_update = 'collection'
    else:
        print('Adding watch to wishlist:\n')
        sheet_to_update = 'wishlist'

    # Create new watch object
    new_watch = Watch(
        get_watch_detail('make', False),
        get_watch_detail('model', False),
        get_watch_detail('movement', True),
        sheet_to_update
    )

    # Get total length of entered characters for warning if over 70
    total_length = (
        len(new_watch.make)+len(new_watch.model)+len(new_watch.movement)
    )

    # Presenting the proposed watch addition to the user.
    print(
        f'Watch-o-Matic will add the following to your {new_watch.sheet}:\n')
    print(f'Make:     {CHECK_COLOUR}{new_watch.make}{CLEAR}')
    print(f'Model:    {CHECK_COLOUR}{new_watch.model}{CLEAR}')
    print(f'Movement: {CHECK_COLOUR}{new_watch.movement}{CLEAR}\n')

    # Asking user for confirmation to add new watch to selected list.
    while True:
        if int(total_length) > 70:
            print(
                f'{ERROR_COLOUR}WARNING!\n\n'
                'Total character amount for these watch details\n'
                'will produce a glitch when viewing the table.\n\n'
                f'Data will be saved correctly to the sytem.{CLEAR}\n'
            )
        final_confirm = input(
            f'Enter {CHOICE_COLOUR}y{CLEAR} to accept or '
            f'{CHOICE_COLOUR}n{CLEAR} to cancel:\n'
        )
        requested = 'Please enter y to accept or n to cancel'
        # If users accepts, new watch data is saved to the google sheet.
        if validate(final_confirm, ['y', 'n'], requested):
            if final_confirm.lower() == 'y':
                new_watch.add_to_sheet()
                break
            # User does not accept so is given options.
            elif final_confirm.lower() == 'n':
                start_over()
                break


def continue_app():
    """
    See if the user wants to go back to the menu to do something else.
    Response is sent for validation.
    """
    while True:
        continue_check = input(
            'Would you like to do anything else? '
            f'({CHOICE_COLOUR}y{CLEAR}/{CHOICE_COLOUR}n{CLEAR}):\n'
        )
        requested = 'Please enter y or n'
        if validate(continue_check, ['y', 'n'], requested):
            break

    if continue_check.lower() == 'y':
        menu()
    elif continue_check.lower() == 'n':
        print('Thank you for using Watch-o-Matic. The app will now close...')


def show_table(table, pages, sheet):
    """
    Display the requested table in pages depending on how many watches there
    are. Pages are split every 10 entries with page numbers shown and a
    prompt to press enter to continue.
    getpass is used so that any other key entries are not seen.
    """
    # Set table min column widths
    table._min_width = {'Make': 30, 'Model': 30, 'Movement': 10}
    table._max_width = {'Make': 30, 'Model': 30, 'Movement': 10}

    # Set initial page view variables
    page_count = 0
    start_row = 0
    end_row = 10

    # Loop through table data showing one page of 10 at a time
    while page_count < pages:
        print(f'Here are the current watches in your {sheet}:\n')
        print(
            table.get_string(start=start_row, end=end_row, sortby="Make"), '\n'
        )
        page_count += 1
        start_row = page_count * 10
        end_row = start_row + 10
        if pages != 1:
            print(f'Page {page_count}/{pages}\n')
        if page_count == pages:
            break
        next_page = getpass.getpass('Press ENTER to continue...\n')
        clear()


def view_selection(sheet_choice):
    """
    Prepares the table to be shown by accessing the corresponding google
    sheet and adding the data to a PrettyTable object. The number of pages
    required is calculated and then all data is passed to show_table function
    to display the table correctly.
    """
    # Access google sheet and feed into PrettyTable.
    watches = SHEET.worksheet(sheet_choice)
    watch_data = watches.get_all_values()
    watch_titles = watch_data[0]
    watch_table = PrettyTable(watch_titles)
    for row in range(1, len(watch_data)):
        watch_table.add_row(watch_data[row])

    # Work out number pages needed.
    num_pages = math.ceil((len(watch_data)-1)/10)

    # Send table data with page info and sheet choice to display.
    show_table(watch_table, num_pages, sheet_choice)

    # Ask user if they want to continue after last page is shown.
    continue_app()


def get_choice():
    """
    Get menu choice from user and calls for validation.
    """
    print('What would you like do to?\n')
    time.sleep(0.2)
    print('1 - View your current collection')
    time.sleep(0.2)
    print('2 - View your current wishlist')
    time.sleep(0.2)
    print('3 - Add a watch to the collection or wishlist\n')
    time.sleep(0.2)
    while True:
        choice = input(
            f'Please enter {CHOICE_COLOUR}1{CLEAR}, '
            f'{CHOICE_COLOUR}2{CLEAR}, '
            f'or {CHOICE_COLOUR}3{CLEAR}:\n'
        )
        requested = 'Please enter 1, 2, or 3'
        if validate(choice, ['1', '2', '3'], requested):
            break

    return choice


def menu():
    """
    Calls correct function depending on users choice from menu.
    """
    match get_choice():
        case '1':
            view_selection('collection')
        case '2':
            view_selection('wishlist')
        case '3':
            add_watch()
        case _:
            # This should never happen
            print('I have a bad feeling about this...')


def main():
    """
    Welcomes user to the app and loads the main menu.
    """
    clear()
    print(
        'Welcome to the Watch-o-Matic! '
        'Your helpful watch collection manager.\n'
        )
    menu()


if __name__ == "__main__":
    clear()
    main()
