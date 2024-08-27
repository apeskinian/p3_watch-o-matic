#Importing libraries and apis.
import gspread
from google.oauth2.service_account import Credentials
from prettytable import PrettyTable

#Defining constants for accessing google sheet data.
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('watch-o-matic')

def get_choice():
    """
    Get menu choice from user and check for valid response, if invalid throw an exception and repeat until valid response is given.
    """
    while True:
        print('1 - View your current collection')
        print('2 - View your current wishlist')
        print('3 - Add a watch to the collection or wishlist')
        print('4 - Remove a watch from the collection or wishlist\n')
        choice = input('What would you like do to? (press 1,2,3 or 4 and press Enter):\n')

        if validate_choice(choice):
            break

    return choice

def validate_choice(user_input):
    """
    Checks if users choice is within valid menu options
    """
    try:
        if int(user_input) not in range(1,5):
            raise ValueError(f"Please enter either 1, 2, 3 or 4. You entered {user_input}")
    except ValueError as e:
        print(f"Invalid choice: {e}, please try again.\n")
        return False
    
    return True

def view_selection(sheet_choice,collection):

    watches = SHEET.worksheet(sheet_choice)

    watch_data = watches.get_all_values()
    watch_titles = watch_data[0]

    watch_table = PrettyTable(watch_titles)
    for row in range(1,len(watch_data)):
        watch_table.add_row(watch_data[row])

    print(f'Here are the current watches in your {collection}:\n')
    print(watch_table)

def main():
    """
    Run all program functions
    """
    menu_chosen = get_choice()
    if menu_chosen == '1':
        view_selection('owned','collection')
    elif menu_chosen == '2':
        view_selection('wishlist','wishlist')
    else:
        print(menu_chosen)

print('Welcome to the Watch-o-Matic! Your helpful watch collection manager. What would you like to do? Please enter one of the options below:\n')
main()


#watches = SHEET.worksheet('owned')

#ownedWatches = watches.get_all_values()
#ownedTitles = ownedWatches[0]

#ownedTable = PrettyTable(ownedTitles)
#for row in range(1,len(ownedWatches)):
#    ownedTable.add_row(ownedWatches[row])

#print('Here are the current watches in your collection:\n')
#print(ownedTable)