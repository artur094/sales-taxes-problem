from lib.producttype import ProductType

class Product:
    def __init__(self, product_name, product_type, product_price):
        self.__name = product_name
        self.__type = product_type
        self.__price = product_price
    
    def getName(self):
        return self.__name

    def getType(self):
        return self.__type

    def getPrice(self):
        return self.__price
    
    def __repr__(self):
        return f"Product([{self.__name}, {self.__type}, {self.__price}])"

    def __str__(self):
        return f"Name: {self.__name}, Type: {self.__type}, Price: {self.__price}"