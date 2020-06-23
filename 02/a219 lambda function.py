szorzas = lambda a,b: a*b
print(szorzas(2,3))

aa = (lambda a,b: a*b)(3,4)
print(aa)

# itt a külső függvény
def doub(a):
    return 2*a

#list comprehension + külső függvény
sequence = [1,2,3,4,5]
doubled = [doub(x) for x in sequence]
print(doubled)

# map +  külső függvény
doubled2 = list(map(doub,sequence))
print(doubled2)

# list comprehension + lambda
doubled = [(lambda x: 2*x)(x) for x in sequence]
print(doubled)

# map + lambda
doubled = map(lambda x: 2*x, sequence)
print(doubled)
