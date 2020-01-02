from lib.orders import Orders
from lib.product import Product
from lib.producttype import ProductType
from lib.taxescalculator import TaxesCalculator
from lib.parser import Parser

def test_product():
    product = Product('test', ProductType.Goods, 10.00)

    assert product.getName() == 'test'
    assert product.getType() == ProductType.Goods
    assert product.getPrice() == 10.00

def test_product_type():
    assert ProductType.toProductType('booksss') == ProductType.Books
    assert ProductType.toProductType('boosss') == ProductType.Goods
    assert ProductType.toProductType('Books') == ProductType.Books
    assert ProductType.toProductType('BoOk') == ProductType.Books

    assert ProductType.toProductType('food') == ProductType.Food
    assert ProductType.toProductType('foods') == ProductType.Food
    assert ProductType.toProductType('FoOd') == ProductType.Food
    assert ProductType.toProductType('ffoods') == ProductType.Food

    assert ProductType.toProductType('medical products') == ProductType.Medicals
    assert ProductType.toProductType('medical') == ProductType.Medicals
    assert ProductType.toProductType('medicals') == ProductType.Medicals
    assert ProductType.toProductType('medicine') == ProductType.Goods

    assert ProductType.toProductType('test') == ProductType.Goods
    assert ProductType.toProductType('') == ProductType.Goods
    assert ProductType.toProductType('goods') == ProductType.Goods
    assert ProductType.toProductType('medic4ls') == ProductType.Goods

def test_orders_insert():
    orders = Orders()

    orders.add(Product('book', ProductType.Books, 12.49), 2, False)
    assert len(orders.getOrders()) == 1

    orders.add(Product('music CD', ProductType.Goods, 14.99), 1, False)
    assert len(orders.getOrders()) == 2

    orders.add(Product('chocolate bar', ProductType.Food, 0.85), 1, False)
    assert len(orders.getOrders()) == 3

    orders.clean()
    assert orders.getOrders() == []
    assert len(orders.getOrders()) == 0

def test_orders_price():
    orders = Orders()
    orders.add(Product('book', ProductType.Books, 12.49), 2, False)
    orders.add(Product('music CD', ProductType.Goods, 14.99), 1, False)
    orders.add(Product('chocolate bar', ProductType.Food, 0.85), 1, False)
    
    assert orders.getTaxes() == 1.50
    assert orders.getPrice() == 42.32

    orders.clean()
    orders.add(Product('box of chocolates', ProductType.Food, 10.00), 1, True)
    orders.add(Product('bottle of perfume', ProductType.Goods, 47.50), 1, True)
    
    assert orders.getTaxes() == 7.65
    assert orders.getPrice() == 65.15

    orders.clean()
    orders.add(Product('bottle of perfume', ProductType.Goods, 27.99), 1, True)
    orders.add(Product('bottle of perfume', ProductType.Goods, 18.99), 1, False)
    orders.add(Product('packet of headache pills', ProductType.Medicals, 9.75), 1, False)
    orders.add(Product('box of chocolates', ProductType.Food, 11.25), 3, True)
    
    assert orders.getTaxes() == 7.90
    assert orders.getPrice() == 98.38

def test_taxes_calculator_round():
    assert TaxesCalculator.round(0.0) == 0.0
    assert TaxesCalculator.round(0.001) == 0.05
    assert TaxesCalculator.round(0.04) == 0.05
    assert TaxesCalculator.round(0.055) == 0.1
    assert TaxesCalculator.round(0.075) == 0.1
    assert TaxesCalculator.round(0.085) == 0.1

def test_taxes_calculator_type():
    assert TaxesCalculator.getTaxesFromProductType(Product("test", ProductType.Goods, 1.9)) == 0.1
    assert TaxesCalculator.getTaxesFromProductType(Product("test", ProductType.Food, 1.9)) == 0
    assert TaxesCalculator.getTaxesFromProductType(Product("test", ProductType.Books, 1.9)) == 0
    assert TaxesCalculator.getTaxesFromProductType(Product("test", ProductType.Medicals, 1.9)) == 0
    

def test_taxes_calculator_taxes():
    prod1 = Product('book', ProductType.Books, 27.99)
    assert TaxesCalculator.getImportTaxes(prod1, 1, False) == 0
    assert TaxesCalculator.getImportTaxes(prod1, 10, False) == 0
    assert TaxesCalculator.getImportTaxes(prod1, 1, True) == 1.40
    assert TaxesCalculator.getImportTaxes(prod1, 10, True) == 14.00

    assert TaxesCalculator.getProductTaxes(prod1, 1) == 0
    assert TaxesCalculator.getProductTaxes(prod1, 10) == 0

    assert TaxesCalculator.getTaxes(prod1, 1, False) == 0
    assert TaxesCalculator.getTaxes(prod1, 10, False) == 0
    assert TaxesCalculator.getTaxes(prod1, 1, True) == 1.40
    assert TaxesCalculator.getTaxes(prod1, 10, True) == 14.00

    assert TaxesCalculator.getPrice(prod1, 1, False) == 27.99
    assert TaxesCalculator.getPrice(prod1, 10, False) == 279.9
    assert TaxesCalculator.getPrice(prod1, 1, True) == 29.39
    assert TaxesCalculator.getPrice(prod1, 10, True) == 293.9

    prod2 = Product('bottle of perfume', ProductType.Goods, 18.99)
    assert TaxesCalculator.getImportTaxes(prod2, 1, False) == 0
    assert TaxesCalculator.getImportTaxes(prod2, 10, False) == 0
    assert TaxesCalculator.getImportTaxes(prod2, 1, True) == 0.95
    assert TaxesCalculator.getImportTaxes(prod2, 10, True) == 9.5

    assert TaxesCalculator.getProductTaxes(prod2, 1) == 1.9
    assert TaxesCalculator.getProductTaxes(prod2, 10) == 19.0

    assert TaxesCalculator.getTaxes(prod2, 1, False) == 1.9
    assert TaxesCalculator.getTaxes(prod2, 10, False) == 19.0
    assert TaxesCalculator.getTaxes(prod2, 1, True) == 2.85
    assert TaxesCalculator.getTaxes(prod2, 10, True) == 28.5

    assert TaxesCalculator.getPrice(prod2, 1, False) == 20.89
    assert TaxesCalculator.getPrice(prod2, 10, False) == 208.9
    assert TaxesCalculator.getPrice(prod2, 1, True) == 21.84
    assert TaxesCalculator.getPrice(prod2, 10, True) == 218.4