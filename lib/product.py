class Product:
    '''
        Define a product with a name, category and price.
    '''
    def __init__(self, product_name, product_category, product_price):
        self.__name = product_name
        self.__category = product_category
        self.__price = product_price
    
    def getName(self):
        return self.__name

    def getCategory(self):
        return self.__category

    def getPrice(self):
        return self.__price
    
    def __repr__(self):
        return f"Product([{self.__name}, {self.__category}, {self.__price}])"

    def __str__(self):
        return f"Name: {self.__name}, Type: {self.__category}, Price: {self.__price}"