class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        aa= f"Hello, én vagyok {self.name} és {self.age} éves vagyok."
        return aa

bob = Person("bob", 19)
print(bob)