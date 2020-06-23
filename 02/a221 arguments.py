def multiply(*args):
    a = 1
    for i in args:
        a *= i
    print(a)

multiply(4,5,6)

b = [1,2,3,4]
multiply(b)

def add(x,y):
    return x+y

par = {'x':2, 'y':3}
print(add(**par))

