def multiply(*args):
    a = 1
    for i in args:
        a *= i
    return a

# multiply(4,5,6)
#
# b = [1,2,3,4]
# multiply(b)

def add(*par):
    a = 0
    for i in par:
        a += i
    return a

print(add(5,6,7,8))
aa = (5,6,7,8)
print(add(*aa))

# def add2(x,y):
#     return x+y
#
# par = {'x':2, 'y':3}
# print(add2(**par))

def apply(*para, operator):
    if operator == '*':
        return multiply(*para)
    elif operator == '+':
        return add(*para)
    else:
        return 'nincs ilyen művelet'

print(apply(2,3,4,5,operator='*'))
print(apply(2,3,4,5,operator='+'))
print(apply(2,3,4,5,operator='>'))
