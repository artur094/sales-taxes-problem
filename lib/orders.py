from lib.producttype import ProductType
from lib.product import Product
from lib.taxescalculator import TaxesCalculator

class Orders:
    def __init__(self):
        self.__orders = []

    def add(self, product, quantity, imported):
        self.__orders.append({
            'product': product,
            'quantity': quantity,
            'imported': imported,
            'taxes': TaxesCalculator.getTaxes(product, quantity, imported),
            'price': TaxesCalculator.getPrice(product, quantity, imported)
        })
    
    def clean(self):
        self.__orders = []

    def getOrders(self):
        return self.__orders

    def getTaxes(self):
        taxes = 0
        for order in self.__orders:
            taxes += order.get('taxes', 0)
        return round(taxes, 2)
    
    def getPrice(self):
        price = 0
        for order in self.__orders:
            price += order.get('price', 0)
        return round(price, 2)

    def printProducts(self):
        for order in self.__orders:
            imported = ""
            if order['imported']:
                imported = " imported"

            print(f"{order['quantity']}{imported} {order['product'].getName()}: {order['price']}")
        print(f'Sales Taxes: {self.getTaxes()}')
        print(f'Total: {self.getPrice()}')
        print("\n")

    def __repr__(self):
        return str(self.orders)

    def __str__(self):
        return str(self.orders)