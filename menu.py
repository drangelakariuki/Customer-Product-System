import datetime
import os
from customer_operations import customer_display_menu
from product_operations import product_display_menu
from purchase_operations import product_operations, purchase_operations


def menu_selection():
    valid_selection = ('1', '2', '3')
    message = "Welcome to the main menu! Please press enter to continue."
    loop = 'yes'
    while True and loop == 'yes':
        selection = input("\nPlease select from the following menu.(Type exit to exit the program)\n"
                          "Enter 1 to conduct customer operations\n"
                          "Enter 2 to conduct product operations\n"
                          "Enter 3 to conduct purchases\n"
                          "\nEnter your choice: ")
        if selection.lower() == 'exit':
            break
        else:
            if selection in valid_selection:
                loop = 'no'

            else:
                print('\nValue: {} did not match any menu choice'.format(selection))
                loop = 'yes'
    return selection


def selection_calls():
    selection = menu_selection()
    if selection == '1':
        customer_display_menu()

    elif selection == '2':
        product_display_menu()

    elif selection == '3':
        purchase_operations()


if __name__ == '__main__':
    selection_calls()
    # ask admin if they want to do something else
    do_more = input('Would you like to do anything else? Type yes or no. ')
    if do_more.lower() == 'no':
        print('Welcome again!')
    if do_more.lower() == 'yes':
        selection_calls()





