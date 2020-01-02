from lib.producttype import ProductType
from lib.product import Product
import math

class TaxesCalculator:
    @staticmethod
    def getTaxesFromProductType(product):
        if product.getType() == ProductType.Goods:
            return 0.1
        return 0

    @staticmethod
    def getImportTaxes(product, quantity, imported):
        if not imported:
            return 0.0

        price = product.getPrice()
        taxes = price * 0.05
        return round(TaxesCalculator.round(taxes) * quantity, 2)

    @staticmethod
    def getProductTaxes(product, quantity):
        price = product.getPrice()
        taxes = price * TaxesCalculator.getTaxesFromProductType(product)
        return round(TaxesCalculator.round(taxes) * quantity, 2)

    @staticmethod
    def getTaxes(product, quantity, imported):
        import_taxes = TaxesCalculator.getImportTaxes(product, quantity, imported)
        product_taxes = TaxesCalculator.getProductTaxes(product, quantity)

        return round(import_taxes + product_taxes, 2)

    @staticmethod
    def getPrice(product, quantity, imported):
        price = product.getPrice() * quantity
        taxes = TaxesCalculator.getTaxes(product, quantity, imported)

        return round(price + taxes, 2)

    @staticmethod
    def round(taxes):
        return round(math.ceil((taxes*100.0)/5.0) * (5.0/100.0), 2)