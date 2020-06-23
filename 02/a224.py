class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Hello, én vagyok {self.name} és {self.age} éves vagyok."

    def __repr__(self):
        return f"<Person({self.name}, {self.age})>"

bob = Person("bob", 19)
print(bob)
