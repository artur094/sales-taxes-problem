from lib.order import Order
from lib.product import Product
from lib.category import Category
from lib.taxescalculator import TaxesCalculator

def test_product():
    # Test the product class
    product = Product('test', Category.Goods, 10.00)

    assert product.getName() == 'test'
    assert product.getCategory() == Category.Goods
    assert product.getPrice() == 10.00

def test_category():
    # Test the category parser.
    assert Category.toCategory('booksss') == Category.Books
    assert Category.toCategory('boosss') == Category.Goods
    assert Category.toCategory('Books') == Category.Books
    assert Category.toCategory('BoOk') == Category.Books

    assert Category.toCategory('food') == Category.Food
    assert Category.toCategory('foods') == Category.Food
    assert Category.toCategory('FoOd') == Category.Food
    assert Category.toCategory('ffoods') == Category.Food

    assert Category.toCategory('medical products') == Category.Medicals
    assert Category.toCategory('medical') == Category.Medicals
    assert Category.toCategory('medicals') == Category.Medicals
    assert Category.toCategory('medicine') == Category.Goods

    assert Category.toCategory('test') == Category.Goods
    assert Category.toCategory('') == Category.Goods
    assert Category.toCategory('goods') == Category.Goods
    assert Category.toCategory('medic4ls') == Category.Goods

def test_orders_insert():
    # Test the insertion and deletion of products for an order.
    order = Order()

    order.add(Product('book', Category.Books, 12.49), 2, False)
    assert len(order.getOrder()) == 1

    order.add(Product('music CD', Category.Goods, 14.99), 1, False)
    assert len(order.getOrder()) == 2

    order.add(Product('chocolate bar', Category.Food, 0.85), 1, False)
    assert len(order.getOrder()) == 3

    order.clean()
    assert order.getOrder() == []
    assert len(order.getOrder()) == 0

def test_orders_price():
    # Test the price computation of the orders.
    order = Order()
    order.add(Product('book', Category.Books, 12.49), 2, False)
    order.add(Product('music CD', Category.Goods, 14.99), 1, False)
    order.add(Product('chocolate bar', Category.Food, 0.85), 1, False)
    
    assert order.getTaxes() == 1.50
    assert order.getPrice() == 42.32

    order.clean()
    order.add(Product('box of chocolates', Category.Food, 10.00), 1, True)
    order.add(Product('bottle of perfume', Category.Goods, 47.50), 1, True)
    
    assert order.getTaxes() == 7.65
    assert order.getPrice() == 65.15

    order.clean()
    order.add(Product('bottle of perfume', Category.Goods, 27.99), 1, True)
    order.add(Product('bottle of perfume', Category.Goods, 18.99), 1, False)
    order.add(Product('packet of headache pills', Category.Medicals, 9.75), 1, False)
    order.add(Product('box of chocolates', Category.Food, 11.25), 3, True)
    
    assert order.getTaxes() == 7.90
    assert order.getPrice() == 98.38

def test_taxes_calculator_round():
    # Test the round up function to the nearest 0.05
    assert TaxesCalculator.round(0.0) == 0.0
    assert TaxesCalculator.round(0.001) == 0.05
    assert TaxesCalculator.round(0.04) == 0.05
    assert TaxesCalculator.round(0.055) == 0.1
    assert TaxesCalculator.round(0.075) == 0.1
    assert TaxesCalculator.round(0.085) == 0.1

def test_taxes_calculator_category():
    # Test the taxes for each category
    assert TaxesCalculator.getTaxesFromCategory(Product("test", Category.Goods, 1.9)) == 0.1
    assert TaxesCalculator.getTaxesFromCategory(Product("test", Category.Food, 1.9)) == 0
    assert TaxesCalculator.getTaxesFromCategory(Product("test", Category.Books, 1.9)) == 0
    assert TaxesCalculator.getTaxesFromCategory(Product("test", Category.Medicals, 1.9)) == 0
    

def test_taxes_calculator_taxes():
    # Test the taxes and price computation
    prod1 = Product('book', Category.Books, 27.99)
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

    prod2 = Product('bottle of perfume', Category.Goods, 18.99)
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