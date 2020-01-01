from lib.producttype import ProductType
from lib.product import Product
from lib.orders import Orders

class Parser:
    def __init__(self, categories_file):
        self.__loadCategories(categories_file)

    def __loadCategories(self, categories_file):
        self.categories = {}

        with open(categories_file) as file:
            for line in file:
                splitted_line = line.split(';')
                product_name = splitted_line[0]
                product_type = ProductType.toProductType(splitted_line[1])
                self.categories[product_name] = product_type
    
    def parse(self, input_file):
        # 1 imported box of chocolates at 10.00
        orders = Orders()

        with open(input_file) as file:
            for line in file:
                splitted_line = line.split(" ")

                product_imported = 'imported' in line
                if product_imported:
                    splitted_line.remove('imported')
                    
                product_quantity = int(splitted_line[0])
                product_price = float(splitted_line[-1])

                product_name = ''.join([s + ' ' for s in splitted_line[1:-2]])[:-1]
                product_type = self.categories[product_name]

                orders.add(Product(product_name, product_type, product_price), product_quantity, product_imported)
        
        return orders
                


