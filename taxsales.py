import enum

class Groups(enum.Enum):
    Goods = 0
    Books = 1
    Food = 2
    Medicals = 3

    def __init__(self, group):
        self.group = group

    def tax(self):
        if self.group == Groups.Goods.value:
            return 0.1
        return 0

class Order:
    def __init__(self, name, group, price, quantity, imported):
        self.name = name
        self.group = Groups(group)
        self.price = price
        self.quantity = quantity
        self.imported = imported

    def importTax(self):
        price = self.price * self.quantity
        import_tax = 0
        if self.imported:
            import_tax = 0.05 * price
        return import_tax
        
    def standardTax(self):
        price = self.price * self.quantity
        tax = self.group.tax() * price

        return tax

    def tax(self):
        tax = self.importTax() + self.standardTax()
        return round(5 * round((tax*100)/5) / 100, 2)
    
    def finalPrice(self):
        return round(self.price * self.quantity + self.tax(), 2)

def printOrders(orders):
    totsum = 0.0
    tottax = 0.0

    for order in orders:
        totsum += order.finalPrice()
        tottax += order.tax()

        imported = ""
        if order.imported:
            imported = " imported"

        print(f'{order.quantity}{imported} {order.name}: {order.finalPrice()}')
    print(f'Sales Taxes: {tottax}')
    print(f'Total: {totsum}')
    print("\n")

order1 = Order('book', Groups.Books, 12.49, 2, False)
order2 = Order('music CD', Groups.Goods, 14.99, 1, False)
order3 = Order('chocolate bar', Groups.Food, 0.85, 1, False)
orders = [order1, order2, order3]
printOrders(orders)

order1 = Order('box of chocolates', Groups.Food, 10.00, 1, True)
order2 = Order('bottle of perfume', Groups.Goods, 47.50, 1, True)
orders = [order1, order2]
printOrders(orders)

order1 = Order('bottle of perfume', Groups.Goods, 27.99, 1, True)
order2 = Order('bottle of perfume', Groups.Goods, 18.99, 1, False)
order3 = Order('packet of headache pills', Groups.Medicals, 9.75, 1, False)
order4 = Order('box of chocolates', Groups.Food, 11.25, 3, True)
orders = [order1, order2, order3, order4]
printOrders(orders)