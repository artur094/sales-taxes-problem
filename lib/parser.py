from lib.category import Category
from lib.product import Product
from lib.order import Order

class Parser:
    '''
    Parses the input file and categories file.
    The categories file is a CSV file formatted using ';'. The CSV has 2 columns: product name; category
    If the category contains one of these words: 'book', 'food' or 'medical', then the product is free of taxes.

    The input file which contains the products is formatted in the following way:
    <numerical quantity> <imported/empty> <product name> at <price>

    The parser retrieves the product names from the input file and matches them with the categories from the categories file.
    In this way, it is possible to use all possible product names if they are mapped in the categories file (if not, they will be considered as generic goods)
    '''

    def __init__(self, categories_file):
        self.__loadCategories(categories_file)

    def __loadCategories(self, categories_file):
        '''
            Parses the file to retrieve the mapping product name - category
        '''
        self.categories = {}

        with open(categories_file) as file:
            for line in file:
                splitted_line = line.split(';')
                product_name = splitted_line[0]
                product_category = Category.toCategory(splitted_line[1])
                self.categories[product_name] = product_category
    
    def parse(self, input_file):
        '''
            Parse the input file to retrieve all the products in the basket.
            Each line of the file corresponds to a product type.
        '''
        # 1 imported box of chocolates at 10.00
        order = Order()

        with open(input_file) as file:
            for line in file:
                splitted_line = line.split(" ")

                product_imported = 'imported' in line
                if product_imported:
                    splitted_line.remove('imported')
                    
                product_quantity = int(splitted_line[0])
                product_price = float(splitted_line[-1])

                product_name = ''.join([s + ' ' for s in splitted_line[1:-2]])[:-1]
                product_category = self.categories.get(product_name, Category.Goods)

                order.add(Product(product_name, product_category, product_price), product_quantity, product_imported)
        
        return order
                


