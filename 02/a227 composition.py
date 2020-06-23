class Book:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"könyv {self.name}"

class Bookshelf:
    def __init__(self, *books):
        self.books = []
        self.books.append(books)

    def __repr__(self):
        return f"gyüjtemény, melyben {len(self.books)} van"

    def addbook(self, ujkonyv):
        self.books.append(ujkonyv)

konyv1 = Book("harrypotter1")
konyv2 = Book("harrypotter2")
gyujtemeny = Bookshelf(konyv1, konyv2)
print(gyujtemeny)