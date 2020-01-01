from lib.orders import Orders
from lib.product import Product
from lib.producttype import ProductType
from lib.parser import Parser
import argparse

#TODO: Add testing on the pre-requisites:
# 1 - Taxes of 10% on goods except for food, books and medical products which is 0%
# 2 - Taxes of 5% on ALL imported products
# 3 - Approssimate the tax value to the nearest 0.05

parser = argparse.ArgumentParser(description='Compute taxes.')
parser.add_argument('--categories', dest='categories', default='',
                    help='File containing all the products and their category.')
parser.add_argument('--input', dest='input', default='',
                    help='File containing all the ordered products.')

args = parser.parse_args()
categories_file = args.categories
input_file = args.input


if input_file != '' and categories_file != '':
    parser = Parser(categories_file)
    orders = parser.parse(input_file)
    orders.printProducts()

else:
    orders = Orders()
    orders.add(Product('book', ProductType.Books, 12.49), 2, False)
    orders.add(Product('music CD', ProductType.Goods, 14.99), 1, False)
    orders.add(Product('chocolate bar', ProductType.Food, 0.85), 1, False)
    orders.printProducts()

    orders.clean()
    orders.add(Product('box of chocolates', ProductType.Food, 10.00), 1, True)
    orders.add(Product('bottle of perfume', ProductType.Goods, 47.50), 1, True)
    orders.printProducts()

    orders.clean()
    orders.add(Product('bottle of perfume', ProductType.Goods, 27.99), 1, True)
    orders.add(Product('bottle of perfume', ProductType.Goods, 18.99), 1, False)
    orders.add(Product('packet of headache pills', ProductType.Medicals, 9.75), 1, False)
    orders.add(Product('box of chocolates', ProductType.Food, 11.25), 3, True)
    orders.printProducts()