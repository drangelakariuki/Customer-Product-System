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
        global cust_id
        cust_id = input('Enter the customer ID: ')
        with open('customer.txt', 'r') as customerfile:
            lines = customerfile.readlines()
            for line in lines:
                line_stripped = line.strip()
                line_list = line_stripped.split(' ')

                if line_list[0] == cust_id:
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
                line_split = line.split(' ')
                if line_split[0] == product_id:
                    product.append(line_split[1])
            print(product)
            product1 = product[0]  # the product list
            product_amount = int(line_split[2])
            product_price = float(line_split[3])
            print('Product to be sold: ', product1)
            print('Doses in stock:', str(product_amount))
            print('Product Price:', product_price)

        amount = int(input('Enter number of doses you would like to sell: '))
        if amount < 1:
            print("ERROR")
            check_product()
        elif amount > product_amount:
            print(f"The {amount} is more than what is available which is {product_amount}.")
            check_product()

        else:
            total_price = amount * product_price
            # create a purchases list
            purchases.append([cust_id, customer[0], product_id, product1, amount, product_price, total_price])
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
            total_purchases += purchases[0][6]
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
                print(f"{purchases[0][3]}")
                print(f'{purchases[0][4]} {space} {purchases[0][5]} {space}{purchases[0][6]}')
                print()
            print('Amount Tendered:    ', cash)
            print('Total Purchases:    ', total_purchases)
            print('The balance is:    ', balance)
            print()
            print('Welcome Again')

            with open('purchases.txt', 'a+') as purchasesfile:
                purchasesfile.write(cust_id + ' ' + customer[0] + ' ' + product_id + ' ' + purchases[0][3] + ' ' + str(
                    purchases[0][4]) + ' ' + str(purchases[0][5]) + ' ' + str(total_purchases))

                print('purchases added')

    checking_out()

    def update_records():
        for purchase in purchases:
            update_id = purchases[0][2]
            quantity = purchases[0][4]

            # product_id = input('Enter the product ID to update: ')
            with open('products.txt', 'r+') as productfile2:
                lines = productfile2.readlines()
                productfile2.seek(0)
                for line in lines:
                    line_stripped = line.strip()
                    line_split = line_stripped.split(' ')
                    if line_split[0] == update_id:
                        print('Found product!', line_split[1])
                        print(line_split)
                    elif line_split[0] != product_id:
                        productfile2.write(line)
                productfile2.truncate()  # cut out the product to be updated
                new_quantity = int(line_split[2]) - int(quantity)
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
