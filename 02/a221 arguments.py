def multiply(*args):
    a = 1
    for i in args:
        a *= i
    print(a)

b = [1,2,3,4]
multiply(*b)