from lib.order import Order
from lib.product import Product
from lib.category import Category
from lib.parser import Parser
import argparse

# 1 - Taxes of 10% on goods except for food, books and medical products which is 0%
# 2 - Taxes of 5% on ALL imported products
# 3 - Approssimate the tax value to the nearest 0.05

# Parse input parameters
parser = argparse.ArgumentParser(description='Compute taxes.')
parser.add_argument('--categories', dest='categories', default='',
                    help='File containing all the products and their category. The file is formatted as CSV using \';\' as separator and it has 2 columns: product name - category.')
parser.add_argument('--input', dest='input', default='',
                    help='File containing all the ordered products.')

args = parser.parse_args()
categories_file = args.categories
input_file = args.input


# If input file is defined, then parse it to retrieve all the products in the basket
# Otherwise, use hard coded test cases.
if input_file != '':
    parser = Parser(categories_file)
    orders = parser.parse(input_file)
    orders.printProducts()

else:
    order = Order()
    order.add(Product('book', Category.Books, 12.49), 2, False)
    order.add(Product('music CD', Category.Goods, 14.99), 1, False)
    order.add(Product('chocolate bar', Category.Food, 0.85), 1, False)
    order.printProducts()
    
    order.clean() # Remove previous products
    order.add(Product('box of chocolates', Category.Food, 10.00), 1, True)
    order.add(Product('bottle of perfume', Category.Goods, 47.50), 1, True)
    order.printProducts()

    order.clean() # Remove previous products
    order.add(Product('bottle of perfume', Category.Goods, 27.99), 1, True)
    order.add(Product('bottle of perfume', Category.Goods, 18.99), 1, False)
    order.add(Product('packet of headache pills', Category.Medicals, 9.75), 1, False)
    order.add(Product('box of chocolates', Category.Food, 11.25), 3, True)
    order.printProducts()