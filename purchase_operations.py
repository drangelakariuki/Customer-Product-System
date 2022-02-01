import os
import customer_operations
import product_operations

purchases = open('purchases.txt', 'x')
purchases.close()


def purchase_operations():
    pass



if __name__ == '__main__':
    product_display_menu()
    pass
    # ask admin if they want to do something else
    do_more = input('Would you like to do anything else? Type yes or no. ')

    if do_more.lower() == 'yes':
        product_display_menu()
    elif do_more.lower() == 'no':
        print('Welcome again!')

        pass