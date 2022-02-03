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
    print(
        " \n"
        "        1. View all products\n"
        "        2. Find product\n"
        "        3. Add new product\n"
        "        4. Update product details\n"
        "        5. Delete product")
    selection = input('Enter the choice: ')
    if selection == '1':
        view_products()
    elif selection == '2':
        find_product()
    elif selection == '3':
        add_product()
    elif selection == '4':
        update_product()
    elif selection == '5':
        delete_product()
    else:
        print('\nValue: {} did not match any menu choice'.format(selection))

        product_display_menu()


def view_products():
    with open('products.txt', "r") as products1:
        products_contents = products1.read()
        print(products_contents)

# view_products()

def add_product():
    """
    Adds new product"""
    print('Create new product')
    # create unique key
    key = open("product_primary_key.txt", "r")
    prim_key = key.read()
    if prim_key == "":
        p_key = 1
        key = open("product_primary_key.txt", "w")
        key.write(str(p_key))
    else:
        p_key = int(prim_key) + 1
        key = open("product_primary_key.txt", "w")
        key.write(str(p_key))
    # create new instance
    new_product_name = input('Enter the product name: ')
    new_product_quantity = int(input('Enter the quantity of product: '))
    new_product_price = float(input('Enter the price of the product: '))
    new_product = Product(p_key, new_product_name, new_product_quantity, new_product_price)
    print(new_product)
    PRODUCTS.append(new_product)
    # print(Product.products)
    with open('products.txt', 'a') as product_file:
        for product in PRODUCTS:
            # add the product to file
            product_file.write(str(product.id) + ' ' + product.name + ' ' + str(product.amount) + ' ' + str(product.price) + '\n')
        print('Product added successfully.')


# add_product()


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


def update_product():
    """
    Reads in the product ID and edits the product attributes
    """
    print('Update product details')
    update_list = []  # list with products not being updated

    product_id = input('Enter the product ID to update: ')
    with open('products.txt', 'r+') as productfile2:
        lines = productfile2.readlines()
        productfile2.seek(0)
        for line in lines:
            line_stripped = line.strip()
            line_split = line_stripped.split(' ')
            if line_split[0] == product_id:
                print('Found product!', line_split[1])
                print(line_split)
            elif line_split[0] != product_id:
                productfile2.write(line)
        productfile2.truncate() # cut out the product to be updated
        new_name = input('Enter new name: ')
        line_split[1] = new_name
        new_amount = input('Enter new amount: ')
        line_split[2] = new_amount
        new_price = input('Enter new price: ')
        line_split[3] = new_price
        print(line_split)
        updated_product = Product(product_id, new_name, new_amount, new_price)
        with open('products.txt', 'a+') as productfile2:

            for instance in Product.products:
                productfile2.write(
                    instance.id + ' ' + instance.name + ' ' + str(instance.amount) + ' ' + str(instance.price) + '\n')
                print('Product file updated successfully.')


# update_product()


def delete_product():
    with open('products.txt', "r+") as productfile3:
        lines = productfile3.readlines()
        productfile3.seek(0)
        product_id = input('Enter the product ID to delete: ')
        for line in lines:
            if not line.startswith(product_id):
                productfile3.write(line)
        productfile3.truncate()
        print('Product deleted successfully.')


# delete_product()


def load_products():
    pass


if __name__ == '__main__':
    product_display_menu()
    # ask admin if they want to do something else
    do_more = input('Would you like to do anything else? Type yes or no. ')

    if do_more.lower() == 'yes':
        product_display_menu()
    elif do_more.lower() == 'no':
        print('Welcome again!')