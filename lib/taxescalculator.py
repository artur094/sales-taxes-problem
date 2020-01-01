from lib.producttype import ProductType
from lib.product import Product

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

        price = product.getPrice() * quantity
        taxes = price * 0.05
        return TaxesCalculator.round(taxes)

    @staticmethod
    def getProductTaxes(product, quantity):
        price = product.getPrice() * quantity
        taxes = price * TaxesCalculator.getTaxesFromProductType(product)
        return TaxesCalculator.round(taxes)

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
        taxes += 0.001
        return round(round(taxes*20) / 20, 2)