#	Main Menu: in the main() function

import add_new_record # Option 1 file name
import display_record # Option 2 file name
import search_record # Option 3 file name
import modify_record # Option 4 file name
import delete_record # Option 5 file name

# Constants for the menu choices
ADD_RECORD = 1
DISPLAY_RECORD = 2
SEARCH_RECORD = 3
MODIFY_RECORD = 4
DELETE_RECORD = 5
QUIT_SYSTEM = 886

# The choice variable controls the loop.
def main():

    # Hold the user's menu choice.
    choice = 0

    #display the menu.
    while choice != QUIT_SYSTEM:
        display_menu()
        choice = int(input("What is your option (1-5/886) ?\n"))

        if choice == ADD_RECORD:
            print("Please add record.")
            add_new_record.option_1()

        elif choice == DISPLAY_RECORD:
            print("Please display record.")
            display_record.option_2()
            
        elif choice == SEARCH_RECORD:
            print("Please search record.")
            search_record.option_3()

        elif choice == MODIFY_RECORD:
            print("Please modify record.")
            modify_record.option_4()

        elif choice == DELETE_RECORD:
            print("Please delete record.")
            delete_record.option_5()

        elif choice == QUIT_SYSTEM:
            print("Quit the system... bye!")

        else:
            print("Error: Wrong selection.")

# The display_menu function displays a menu.
def display_menu():

    print()
    print("***Welcome to HKSPACE Inventory Management and Record System 1920S1 ***\n")
    print("*** This system is developed by CCIT4020 Class No. CL02 Group No. ?? ***\n")
    print("--<Basic functions>--\n")
    print("1. Add New Item(s):\n")
    print("2. Display Item Record(s):\n")
    print("3. Search Item Information:\n")
    print("4. Modify Item Record(s):\n")
    print("5. Delete Item Record(s):\n")
    print("886. Quit System.\n")

main()
