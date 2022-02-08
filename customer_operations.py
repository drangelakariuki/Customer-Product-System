# Customer operations with OOP
# Perfect on use of lists # Unique ID checker

CUSTOMERS = []


class Customer:

    def __init__(self, customer_id: str, customer_name: str, customer_address: str):
        # instance variables
        self.id = customer_id
        self.name = customer_name
        self.address = customer_address

    def __repr__(self):  # helps readability
        return f"{self.id}, {self.name},{self.address}"


def customer_display_menu(): # displays menu options for customer functions
    while True:
        selection = input(""" Welcome to the customer menu! Enter 0 to if you want to exit program:\n
                1. Add customer\n
                2. Update Customer Details\n
                3. Delete a Customer\n
                4. Find a Customer\n
                5. View all customers\n
                Enter your choice: """)
        if selection == '1':
            add_customers()
        elif selection == '2':
            update_customer()
        elif selection == '3':
            delete_customer()
        elif selection == '4':
            find_customer()
        elif selection == '5':
            view_customers()
        elif selection == '0':
            break
        else:
            print('\nValue: {} did not match any menu choice'.format(selection))


def add_customers(): # FUNCTION TO ADD CUSTOMER TO FILE
    def id_check():  # check uniqueness of id
        with open("customer.txt", "r") as customerfile: # open  customer file in read mode
            global customer_id
            customer_id = input('Assign a unique ID(Customer Phone Number): ')
            id_list = []
            lines = customerfile.readlines()  # loads data from the file to a list called lines
            for line in lines:
                line_stripped = line.strip()
                line_list = line_stripped.split(' ')
                id_list.append(line_list[0])
            if customer_id in id_list:
                print("The customer already exists. Enter a valid ID")
                id_check()

    id_check()

    customer_name = input('Enter full customer name: ')
    customer_address = input('Enter customer address: ')
    new_customer = Customer(customer_id, customer_name, customer_address)
    CUSTOMERS.append(new_customer)
    # write customer into the file
    with open('customer.txt', 'a+', newline='') as customer_file:
        for customer in CUSTOMERS:
            customer_file.write(customer.id + ' ' + customer.name + ' ' + customer.address + '\n')
        print('Customer added to file successfully.')


# add_customers()

def update_customer():
    def id_check():  # check uniqueness of id
        with open('customer.txt', 'r') as customerfile4:
            global customer_id
            customer_id = input('Enter the customer ID to update: ')
            id_list = []
            lines = customerfile4.readlines()  # loads data from the file to a list called lines
            for line in lines:
                line_stripped = line.strip()
                line_list = line_stripped.split(' ')
                id_list.append(line_list[0])
            if customer_id not in id_list:
                print("ID not in file. Re Enter ID?")
                id_check()

    id_check()
    with open('customer.txt', 'r+') as customerfile4:
        lines = customerfile4.readlines()
        customerfile4.seek(0)
        for line in lines:
            line_stripped = line.strip()
            line_split = line_stripped.split(' ')
            if line_split[0] == customer_id:
                print('Found Customer!', line_split[1])
                print(line_split)
            elif line_split[0] != customer_id:
                customerfile4.write(line)
        customerfile4.truncate()  # cut out the customer to be updated
        new_name = input('Enter new customer name : ')
        line_split[1] = new_name
        new_address = input('Enter new customer address: ')
        line_split[2] = new_address
        updated_customer = Customer(customer_id, new_name, new_address)
        CUSTOMERS.append(updated_customer)
        with open('customer.txt', 'a+') as customerfile4:
            for instance in CUSTOMERS:
                customerfile4.write(instance.id + ' ' + instance.name + ' ' + instance.address + '\n')
                print('Customer file updated successfully.')


# update_customer()


def delete_customer():  # deletes a particular customer
    def id_check():  # check uniqueness of id
        with open('customer.txt', "r") as customerfile3:
            global customer_id
            customer_id = input('Enter the customer ID to delete: ')
            id_list = []
            lines = customerfile3.readlines()  # loads data from the file to a list called lines
            for line in lines:
                line_stripped = line.strip()
                line_list = line_stripped.split(' ')
                id_list.append(line_list[0])
            if customer_id not in id_list:
                print("ID Not Found! Re Enter a valid ID")
                id_check()

    id_check()

    with open('customer.txt', "r+") as customerfile3:
        lines = customerfile3.readlines()
        customerfile3.seek(0)
        for line in lines:
            if not line.startswith(customer_id):
                customerfile3.write(line)
        customerfile3.truncate()


# delete_customer()

def find_customer():
    """
    Find a specific customer and prints the customer
    """
    with open('customer.txt', "r+") as customerfile2:
        customer_id = input('Enter the customer ID to find: ')
        lines = customerfile2.readlines()  # loads data from the file to a list called lines
        id_list = []
        for line in lines:
            line_stripped = line.strip()
            line_list = line_stripped.split(' ')
            if line_list[0] == customer_id:
                print('Customer Phone Number: ', line_list[0])
                print('Customer Name:         ', line_list[1])
                print('Customer Address:      ', line_list[2])


# find_customer()

def view_customers():  # view all customers on file
    with open('customer.txt', "r") as customers:
        customers_contents = customers.read()
        print(customers_contents)


# view_customers()
if __name__ == '__main__':
    customer_display_menu()
