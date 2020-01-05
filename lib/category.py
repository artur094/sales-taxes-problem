import enum

class Category(enum.Enum):
    '''
        Defines the categories handled in this project. Goods have a 10% of tax to include in the final price,
        while the other categories are free of taxes.
    '''
    Goods = 0
    Books = 1
    Food = 2
    Medicals = 3
    
    @staticmethod
    def toCategory(label):
        '''
            Convert the label into a category.
            If it contains the word 'book', then it's considered as Book
            If it contains the word 'food', then it's considered as Food
            If it contains the word 'medical', then it's considered as Medical Product
        '''
        if 'book' in label.lower():
            return Category.Books
        if 'food' in label.lower():
            return Category.Food
        if 'medical' in label.lower():
            return Category.Medicals
        return Category.Goods