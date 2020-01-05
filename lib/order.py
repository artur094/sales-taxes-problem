from lib.taxescalculator import TaxesCalculator

class Order:
    '''
        Handles a basket full of products. It is possible to add products, remove all of them, compute the
        total amount of taxes and the total price, taxes included, that the customer has to pay.
    '''
    def __init__(self):
        self.__order = []

    def add(self, product, quantity, imported):
        self.__order.append({
            'product': product,
            'quantity': quantity,
            'imported': imported,
            'taxes': TaxesCalculator.getTaxes(product, quantity, imported),
            'price': TaxesCalculator.getPrice(product, quantity, imported)
        })
    
    def clean(self):
        '''
            Delete all stored products
        '''
        self.__order = []

    def getOrder(self):
        return self.__order

    def getTaxes(self):
        '''
            Return the total sum of taxes to pay
        '''
        taxes = 0
        for order in self.__order:
            taxes += order.get('taxes', 0)
        return round(taxes, 2)
    
    def getPrice(self):
        '''
            Return the total price, taxes included, to pay
        '''
        price = 0
        for order in self.__order:
            price += order.get('price', 0)
        return round(price, 2)

    def printProducts(self):
        '''
            Print in a nice way each product with the final price, the total taxes and price to pay.
        '''
        for order in self.__order:
            imported = ""
            if order['imported']:
                imported = " imported"

            print(f"{order['quantity']}{imported} {order['product'].getName()}: {order['price']}")
        print(f'Sales Taxes: {self.getTaxes()}')
        print(f'Total: {self.getPrice()}')
        print("\n")

    def __repr__(self):
        return str(self.__order)

    def __str__(self):
        return str(self.__order)