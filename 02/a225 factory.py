class Book:
    TYPES = ("hardcover", "paperback")

    def __init__(self, name, booktype, weight):
        self.name = name
        self.booktype = booktype
        self.weight = weight


konyv1 = Book('aa', "hardcover", 222)
konyv2 = Book('bb', "paperback", 333)

print(Book.TYPES)