# Customer operations with OOP
# Perfect on use of lists # Unique ID checker

CUSTOMERS = []


class Customer:

    def __init__(self, customer_id: str, customer_name: str, customer_address: str):
        self.id = customer_id
        self.name = customer_name
        self.address = customer_address
        # actions to execute

        # Customer.CUSTOMERS.append(self)

    def __repr__(self):  # helps readability
        return f"{self.id}, {self.name},{self.address}"


# customer1 = Customer('1', 'Angela', 'Juja')
# customer2 = Customer('2', 'Guantai', 'Embu')

# print(Customer.CUSTOMERS)

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
        add_customers()
    elif selection == '2':
        find_customer()
    elif selection == '3':
        delete_customer()
    elif selection == '4':
        update_customer()
    elif selection == '5':
        view_customers()
    else:
        print('\nValue: {} did not match any menu choice'.format(selection))

        customer_display_menu()


def add_customers():
    key = open("customer_primary_key.txt", "r")
    prim_key = key.read()
    if prim_key == "":
        p_key = 1
        key = open("customer_primary_key.txt", "w")
        key.write(str(p_key))
    else:
        p_key = int(prim_key) + 1
        key = open("customer_primary_key.txt", "w")
        key.write(str(p_key))
    customer_id = str(p_key)
    customer_name = input('Enter full customer name: ')
    customer_address = input('Enter customer address: ')

    new_customer = Customer(customer_id, customer_name, customer_address)
    CUSTOMERS.append(new_customer)

    # add_another_customer = input('Do you want to add another customer? Enter y or n. ')
    #
    # if add_another_customer.lower == 'y':
    #     add_customers()
    #
    # elif add_another_customer.lower == 'n':
    with open('customer.txt', 'a') as product_file:
        for product in CUSTOMERS:
            # add the product to file
            product_file.write(str(product.id) + ' ' + product.name + ' ' + product.address + '\n')
        print('Customer added to file successfully.')


# add_customers()


def find_customer():
    """
    Find a specific customer and prints the customer
    """
    with open('customer.txt', "r+") as customerfile2:
        customer_id = input('Enter the customer ID to find: ')
        lines = customerfile2.readlines()  # loads data from the file to a list called lines
        for line in lines:
            line_stripped = line.strip()
            line_list = line_stripped.split(' ')
            if line_list[0] == customer_id:
                print('CustomerID: ', line_list[0])
                print('Customer Name: ', line_list[1])
                print('Customer Address: ', line_list[2])


# find_customer()


def delete_customer():  # deletes a particular customer
    with open('customer.txt', "r+") as customerfile3:
        lines = customerfile3.readlines()
        customerfile3.seek(0)
        customer_id = input('Enter the customer ID to delete: ')
        for line in lines:
            if not line.startswith(customer_id):
                customerfile3.write(line)
        customerfile3.truncate()


# delete_customer()

def update_customer():
    customer_id = input('Enter the customer ID to update: ')
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

def view_customers():  # view all customers on the list
    with open('customer.txt', "r") as customers:
        customers_contents = customers.read()
        print(customers_contents)


# view_customers()
if __name__ == '__main__':
    customer_display_menu()
