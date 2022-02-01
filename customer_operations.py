# handling customer functions
import os

customer_file = open('customer.txt', 'a')


def customer_display_menu():
    print("Welcome to the customer operations menu! Please press enter to continue.")
    print(
        " \n"
        "        1. View all customers\n"
        "        2. Find Customer\n"
        "        3. Add new customer\n"
        "        4. Update customer details\n"
        "        5. Delete Customer")
    selection = input('Enter the choice: ')
    if selection == '1':
        view_customers()
    elif selection == '2':
        find_customer()
    elif selection == '3':
        new_customer()
    elif selection == '4':
        update_customer()
    elif selection == '5':
        delete_customer()
    else:
        print('\nValue: {} did not match any menu choice'.format(selection))

        customer_display_menu()


def view_customers():
    with open('customer.txt', "r") as customers:
        customers_contents = customers.read()
        print(customers_contents)


def new_customer():  # adding new customer and creating a unique ID.
    key = open("primary_key.txt", "r")
    prim_key = key.read()
    if prim_key == "":
        p_key = 1
        key = open("primary_key.txt", "w")
        key.write(str(p_key))
    else:
        p_key = int(prim_key) + 1
        key = open("primary_key.txt", "w")
        key.write(str(p_key))
    with open('customer.txt', "a") as customer_file1:
        customer_name = input("Enter the customer's name: ")
        customer_address = input("Enter the customer's address: ")
        customer_file.write(str(p_key) + ' ' + customer_name + ' ' + customer_address + '\n')

    print('New Customer added!')


def find_customer():
    with open('customer.txt', "r+") as customerfile2:
        lines = customerfile2.readlines()
        customer_id = input('Enter the customer ID to find: ')
        for line in lines:
            line_stripped = line.strip()
            line_list = line_stripped.split(' ')
            if line_list[0] == customer_id:
                print('CustomerID: ', line_list[0])
                print('Customer Name: ', line_list[1])
                print('Customer Address: ', line_list[2])


def update_customer():
    with open('customer.txt', "r+") as customerfile4:
        lines = customerfile4.readlines()
        customerfile4.seek(0)
        customer_id = input('Enter the customer ID to update: ')
        for line in lines:
            if not line.startswith(customer_id):
                customerfile4.write(line)
        customerfile4.truncate()
        customer_name = input("Enter the customer's name: ")
        customer_address = input("Enter the customer's address: ")
        customerfile4.write(customer_id + ' ' + customer_name + ' ' + customer_address + '\n')


def delete_customer():
    with open('customer.txt', "r+") as customerfile3:
        lines = customerfile3.readlines()
        customerfile3.seek(0)
        customer_id = input('Enter the customer ID to delete: ')
        for line in lines:
            if not line.startswith(customer_id):
                customerfile3.write(line)
        customerfile3.truncate()


# delete_customer()


if __name__ == '__main__':
    customer_display_menu()
    # ask admin if they want to do something else
    do_more = input('Would you like to do anything else? Type yes or no. ')
    if do_more.lower() == 'no':
        print('Welcome again!')
    if do_more.lower() == 'yes':
        customer_display_menu()
