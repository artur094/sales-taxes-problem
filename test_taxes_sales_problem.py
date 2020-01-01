from lib.orders import Orders
from lib.product import Product
from lib.producttype import ProductType
from lib.parser import Parser

def test_product():
    product = Product('test', ProductType.Goods, 10.00)

    assert product.getName() == 'test'
    assert product.getType() == ProductType.Goods
    assert product.getPrice() == 10.00

def test_product_type():
    assert ProductType.toProductType('booksss') == ProductType.Books