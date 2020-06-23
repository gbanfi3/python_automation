def multiply(*args):
    a = 1
    for i in args:
        a *= i
    return a

multiply(4,5,6)

b = [1,2,3,4]
multiply(b)

def add(*par):
    a = 0
    for i in par:
        a += i
    return a

par = {'x':2, 'y':3}
print(add(**par))

def apply(*para, operator):
    if operator == '*':
        return multiply(para)
    elif operator == '+':
        return add(para)
    else:
        print('nincs ilyen művelet')
