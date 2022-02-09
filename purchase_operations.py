from customer_operations import *
from product_operations import *

customer = []
product = []
purchases = []
def purchase_display_menu():
    print('Welcome to purchases!')
    while True:
        selection = input('''
        1. Conduct Purchase
        2. Find a Purchase
        Enter your choice(Enter O to exit): ''')
        if selection == '1':
            purchase()
        elif selection == '2':
            find_purchase()
        elif selection == '0':
            break
        else:
            print('\nValue: {} did not match any menu choice'.format(selection))
            purchase_display_menu()


def purchase():
    def check_customer():
        global customer_id
        customer_id = input('Enter the customer ID: ')
        with open('customer.txt', 'r') as customerfile:
            lines = customerfile.readlines()
            for line in lines:
                line_stripped = line.strip()
                line_list = line_stripped.split(' ')
                if line_list[0] == customer_id:
                    customer.append(line_list[1])
                    print(customer)

    check_customer()

    def check_product():
        global product_id
        product_id = input('Enter the unique product ID: ')
        with open('products.txt', 'r') as product_file1:
            lines = product_file1.readlines()
            for line in lines:
                line_stripped = line.strip()
                line_split = line_stripped.split(' ')
                if line_split[0] == product_id:
                    name = line_split[1]
                    global doses
                    doses = int(line_split[2])
                    price = float(line_split[3])
                    product = line_split
                    print(product)
                    print('Product to be sold: ', name)
                    print('Doses in stock:', doses)
                    print('Product Price:', price)
        global amount
        amount = int(input('Enter number of doses you would like to sell: '))
        if amount < 1:
            print("ERROR")
            check_product()
        elif amount > doses:
            print(f"The {amount} is more than what is available which is {doses}.")
            check_product()

        else:
            total_price = amount * price
            # create a purchases list
            purchases.append([customer_id, customer[0], product_id, name, amount, price, total_price])
            print(purchases)

            another_purchase = input("""
                                        Enter 1 to conduct another purchase
                                        Enter 2 to checkout.
                                        Enter choice: """)
            if another_purchase == '1':
                check_product()

            if another_purchase == '2':
                print('Proceed to checkout')

    check_product()

    def checking_out():
        total_purchases = 0
        for purchase in purchases:
            print(purchase)
            total_purchases += purchase[6]
        print(total_purchases)

        cash = int(input('Enter amount of money customer has given: '))
        if cash < total_purchases:
            print(f"Insufficient funds. The total amount is {total_purchases}")
            option = input('Enter 1 to enter a different amount or 2 to exit: ')
            if option == '1':
                checking_out()
            elif option == '2':
                exit

        else:
            # print the receipt
            balance = cash - total_purchases

            print('    ' + 'ANGELA PHARMACY' + '   ')
            print()
            print('    ' + 'Purchase Receipt' + '   ')
            print('  ' + customer[0])
            print()
            space = ' '
            for purchase in purchases:
                print(f"{purchase[3]}")
                print(f'{purchase[4]} {space} {purchase[5]} {space}{purchase[6]}')
                print()
            print('Amount Tendered:    ', cash)
            print('Total Purchases:    ', total_purchases)
            print('The balance is:    ', balance)
            print()
            print('Welcome Again')

        with open('purchases.txt', 'a+') as purchasesfile:
            purchasesfile.write(customer_id + ' ' + customer[0] + ' ' + product_id + ' ' + purchase[3] + ' ' + str(
                purchase[4]) + ' ' + str(purchase[5]) + ' ' + str(purchase[6]) + '\n')

            print('purchases added')

    checking_out()

    def update_records():
        for purchase in purchases:
            print(purchase)
            update_id = purchase[2]  # product_id
            quantity = purchase[4]  # amount bought
            # product_id = input('Enter the product ID to update: ')
            with open('products.txt', 'r+') as productfile2:
                lines = productfile2.readlines()
                print(lines)
                productfile2.seek(0)
                for line in lines:
                    # print(line)
                    line_stripped = line.strip()
                    line_split = line_stripped.split(' ')
                    if line_split[0] == update_id:
                        print(line_split)
                        print('Found product!', line_split[1])
                        quantity1 = line_split[2]
                        new_quantity = int(quantity1) - int(quantity)  # what's left
                        print(new_quantity)
                    elif line_split[0] != update_id:
                        productfile2.write(line)
                productfile2.truncate()  # cut out the product to be updated
                new_product = [update_id, line_split[1], str(new_quantity), str(line_split[3])]
                print(new_product)
        with open('products.txt', 'a+') as productfile2:
            productfile2.write(
                update_id + ' ' + line_split[1] + ' ' + str(new_quantity) + ' ' + str(line_split[3]) + '\n')
        print('inventory updated successfully.')

    update_records()


# purchase()


def find_purchase():
    option = input('''
                            1. Search by Customer ID
                            2. Search by Product ID
                            Enter your choice: ''')
    if option == '1':
        customer_id = input('Enter the unique Customer ID: ')
        with open('purchases.txt', 'r') as purchasefile1:
            lines = purchasefile1.readlines()
            for line in lines:
                line_stripped = line.strip()
                line_split = line_stripped.split(' ')
                print(line_split)
                if line_split[0] == customer_id:
                    print('Customer Name:', line_split[1])
                    print('Product name:', line_split[3])
                    print('Product quantity:', line_split[4])
                    print('Product price:', line_split[5])
                    print('Total Amount Spent:', line_split[6])

    if option == '2':
        product_id = input('Enter the unique product ID: ')
        with open('purchases.txt', 'r') as purchasefile1:
            lines = purchasefile1.readlines()
            for line in lines:
                line_stripped = line.strip()
                line_split = line_stripped.split(' ')
                print(line_split)
                if line_split[2] == product_id:
                    print('Customer Name:', line_split[1])
                    print('Product name:', line_split[3])
                    print('Quantity Purchased:', line_split[4])
                    print('Product price:', line_split[5])
                    print('Total Amount Spent:', line_split[6])

# find_purchase()

if __name__ == '__main__':
    purchase_display_menu()
