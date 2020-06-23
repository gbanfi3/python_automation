class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return "Hello, én vagyok " + self.name + ", és " + age + " éves vagyok."

bob = Person("bob", 19)
print(bob)