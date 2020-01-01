from lib.producttype import ProductType
from lib.product import Product
from lib.taxescalculator import TaxesCalculator

class Orders:
    def __init__(self):
        self.orders = []

    def add(self, product, quantity, imported):
        self.orders.append({
            'product': product,
            'quantity': quantity,
            'imported': imported,
            'taxes': TaxesCalculator.getTaxes(product, quantity, imported),
            'price': TaxesCalculator.getPrice(product, quantity, imported)
        })
    
    def clean(self):
        self.orders = []

    def taxes(self):
        taxes = 0
        for order in self.orders:
            taxes += order.get('taxes', 0)
        return taxes
    
    def price(self):
        price = 0
        for order in self.orders:
            price += order.get('price', 0)
        return price

    def printProducts(self):
        for order in self.orders:
            imported = ""
            if order['imported']:
                imported = " imported"

            print(f"{order['quantity']}{imported} {order['product'].getName()}: {order['price']}")
        print(f'Sales Taxes: {self.taxes()}')
        print(f'Total: {self.price()}')
        print("\n")

    def __repr__(self):
        return str(self.orders)

    def __str__(self):
        return str(self.orders)