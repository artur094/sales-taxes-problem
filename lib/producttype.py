import enum

class ProductType(enum.Enum):
    Goods = 0
    Books = 1
    Food = 2
    Medicals = 3
    
    @staticmethod
    def toProductType(label):
        if 'book' in label.lower():
            return ProductType.Books
        if 'food' in label.lower():
            return ProductType.Food
        if 'medical' in label.lower():
            return ProductType.Medicals
        return ProductType.Goods