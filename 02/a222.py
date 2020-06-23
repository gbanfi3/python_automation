def named(**kwargs):
    print(kwargs)
named(name="bob", age=23)

def named2(name, age):
    print(name, age)

details = {'name': "bob", 'age': 33}
named2(**details)

valami = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

def printnicely(**alma):
    print(alma)
    for a,b in alma.items():
        print(f"{a}: {b}")
printnicely(**valami)
