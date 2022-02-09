import os

PRODUCTS = []


class Product:

    def __init__(self, product_id, product_name, product_quantity, product_price):
        # assign to self object
        self.id = product_id
        self.name = product_name
        self.amount = product_quantity
        self.price = product_price
        # actions to execute
        # Product.products.append(self)

    def __repr__(self):
        return f'(\'{self.id}\', {self.name}, {self.amount}, {self.price})'


def product_display_menu():
    print("Welcome to the customer operations menu! Please press enter to continue.")
    while True:
        selection = input(
            " \n"
            "        1. Add new product\n"
            "        2. Update product details\n"
            "        3. Delete product\n"
            "        4. Find Product\n"
            "        5. View all products\n"
            "        Enter your choice(Enter O to exit): ")
        if selection == '1':
            add_product()
        elif selection == '2':
            update_product()
        elif selection == '3':
            delete_product()
        elif selection == '4':
            find_product()
        elif selection == '5':
            view_products()
        elif selection == '0':
            break
        else:
            print('\nValue: {} did not match any menu choice'.format(selection))


def add_product():
    def id_check():  # check uniqueness of  Product ID
        with open("products.txt", "r") as product_file:  # open  product file in read mode
            global product_id
            product_id = input('Assign a unique Product ID(or Scan Barcode): ')
            id_list = []
            lines = product_file.readlines()  # loads data from the file to a list called lines
            for line in lines:
                line_stripped = line.strip()
                line_list = line_stripped.split(' ')
                id_list.append(line_list[0])
            if product_id in id_list:
                print("The product already exists. Enter a valid unique ID")
                id_check()

    id_check()
    product_name = input('Enter the product name: ')
    product_quantity = int(input('Enter the quantity of product: '))
    product_price = float(input('Enter the price of the product: '))
    new_product = Product(product_id, product_name, product_quantity, product_price)
    print(new_product)
    PRODUCTS.append(new_product)
    # print(Product.products)
    with open('products.txt', 'a+') as product_file:
        product_file.write(product_id + ' ' + product_name + ' ' + str(product_quantity) + ' ' + str(product_price) + '\n')
        # for product in PRODUCTS:  # add the product to file
        #     product_file.write(
        #         product.id + ' ' + product.name + ' ' + str(product.amount) + ' ' + str(product.price) + '\n')
        print('Product added successfully.')


# add_product()


def update_product():
    """
    Reads in the product ID and edits the product attributes
    """
    print('Update product details')

    def id_check():  # check uniqueness of  Product ID
        with open("products.txt", "r") as productfile2:  # open  product file in read mode
            global product_id
            product_id = input('Enter ID to update: ')
            id_list = []
            lines = productfile2.readlines()  # loads data from the file to a list called lines
            for line in lines:
                line_stripped = line.strip()
                line_list = line_stripped.split(' ')
                id_list.append(line_list[0])
            if product_id not in id_list:
                print("Enter valid ID")
                id_check()

    id_check()
    with open('products.txt', 'r+') as productfile2:
        lines = productfile2.readlines()
        productfile2.seek(0)
        for line in lines:
            line_stripped = line.strip()
            line_split = line_stripped.split(' ')
            if line_split[0] == product_id:
                print('Found product!', line_split[1])
                print(line_split) # the product in a line (just checking)
            elif line_split[0] != product_id:
                productfile2.write(line)
        productfile2.truncate()  # cut out the product to be updated
        new_name = input('Enter new name: ') # in case you want to change the name
        line_split[1] = new_name
        new_amount = input('Enter new amount: ')
        line_split[2] = new_amount
        new_price = input('Enter new price: ')
        line_split[3] = new_price
        updated_product = Product(product_id, new_name, new_amount, new_price)
        PRODUCTS.append(updated_product)
        with open('products.txt', 'a+') as productfile2:
            for instance in PRODUCTS:
                productfile2.write(
                    instance.id + ' ' + instance.name + ' ' + str(instance.amount) + ' ' + str(instance.price) + '\n')
            print('Product file updated successfully.')


# update_product()


def delete_product():
    def id_check():  # check uniqueness of  Product ID
        with open("products.txt", "r") as productfile3:  # open  product file in read mode
            global product_id
            product_id = input('Enter ID to delete: ')
            id_list = []
            lines = productfile3.readlines()  # loads data from the file to a list called lines
            for line in lines:
                line_stripped = line.strip()
                line_list = line_stripped.split(' ')
                id_list.append(line_list[0])
            if product_id not in id_list:
                print("Enter valid ID")
                id_check()

    id_check()
    with open('products.txt', "r+") as productfile3:
        lines = productfile3.readlines()
        productfile3.seek(0)
        for line in lines:
            if not line.startswith(product_id):
                productfile3.write(line)
        productfile3.truncate()
        print('Product deleted successfully.')


# delete_product()

def find_product():
    """
    Finding a particular product
    """
    product_id = input('Enter the unique product ID: ')
    with open('products.txt', 'r') as product_file1:
        lines = product_file1.readlines()
        for line in lines:
            line_stripped = line.strip()
            line_split = line.split(' ')
            if line_split[0] == product_id:
                print('Product Id:', line_split[0])
                print('Product name:', line_split[1])
                print('Product quantity:', line_split[2])
                print('Product price:', line_split[3])


# find_product()

def view_products():
    with open('products.txt', "r") as products1:
        products_contents = products1.read()
        print(products_contents)


# view_products()


if __name__ == '__main__':
    product_display_menu()
