class Book:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"könyv {self.name}"

class Bookshelf:
    def __init__(self, *bookss):
        self.books = []
        for i in bookss:
            self.books.append(i)
        print(self)

    def __repr__(self):
        return f"gyüjtemény, melyben {len(self.books)} könyv van"

    def addbook(self, ujkonyv):
        self.books.append(ujkonyv)

konyv1 = Book("harrypotter1")
konyv2 = Book("harrypotter2")
konyv3 = Book("harrypotter3")
gyujtemeny = Bookshelf(konyv1, konyv2)
gyujtemeny.addbook(konyv3)
print(gyujtemeny)