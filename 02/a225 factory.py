class Book:
    TYPES = ("hardcover", "paperback")

    def __init__(self, name, booktype, weight):
        self.name = name
        self.booktype = booktype
        self.weight = weight

    def __repr__(self):
        return f"<Book {self.name}, {self.booktype}, {self.weight}g>"

    @classmethod
    def hardcover(cls, name, weight):
        return Book(name, Book.TYPES[0], weight + 100)

    @classmethod
    def paperback(cls, name, weight):
        return Book(name, Book.TYPES[1], weight)

konyv1 = Book('aa', "hardcover", 222)
konyv2 = Book('bb', "paperback", 333)

# print(Book.TYPES)
print(konyv1.name)
print(konyv1)

konyv3 = Book.hardcover("kemény", 444)
print(konyv3)

konyv4 = Book.paperback("papír", 555)