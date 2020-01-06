from lib.category import Category
import math

class TaxesCalculator:
    '''
        Handles the taxes calculations.
        It computes the taxes based on importation or category, or the sum of both taxes.
    '''
    @staticmethod
    def getTaxesFromCategory(product):
        '''
            Return the category tax percentage for the given product
        '''
        if product.getCategory() == Category.Goods:
            return 0.1
        return 0

    @staticmethod
    def getImportTaxes(product, quantity, imported):
        '''
            Return the amount of import taxes that must be added to the final price for the given product
        '''
        if not imported:
            return 0.0

        price = product.getPrice()
        taxes = price * 0.05
        return round(TaxesCalculator.round(taxes) * quantity, 2)

    @staticmethod
    def getProductTaxes(product, quantity):
        '''
            Return the amount of category taxes that must be added to the final price for the given product
        '''
        price = product.getPrice()
        taxes = price * TaxesCalculator.getTaxesFromCategory(product)
        return round(TaxesCalculator.round(taxes) * quantity, 2)

    @staticmethod
    def getTaxes(product, quantity, imported):
        '''
            Return the total taxes that must be added to the final price for the given product
        '''
        import_taxes = TaxesCalculator.getImportTaxes(product, quantity, imported)
        product_taxes = TaxesCalculator.getProductTaxes(product, quantity)

        return round(import_taxes + product_taxes, 2)

    @staticmethod
    def getPrice(product, quantity, imported):
        '''
            Return the final price for a given product
        '''
        price = product.getPrice() * quantity
        taxes = TaxesCalculator.getTaxes(product, quantity, imported)

        return round(price + taxes, 2)

    @staticmethod
    def round(taxes):
        '''
            Round up to the nearest 0.05
        '''
        # ceil -> round up to the highest integer ( math.ceil(0.1) = 1)
        # To round up to the second decimal, multiply by 100 before rounding up, then divide by 100 after the rounding to bring back the decimal part.
        # To round up to a multiple of 5, divide before rounding and after that, multiply the result by 5

        return round(math.ceil((taxes*100.0)/5.0) * (5.0/100.0), 2)