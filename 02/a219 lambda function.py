szorzas = lambda a,b: a*b
print(szorzas(2,3))

aa = (lambda a,b: a*b)(3,4)
print(aa)

#list comprehension
def doub(a):
    return 2*a

sequence = [1,2,3,4,5]
doubled = [doub(x) for x in sequence]
print(doubled)

# még jobb
doubled2 = list(map(doub,sequence))
print(doubled2)

# újabb

doubled = [(lambda x: 2*x)(x) for x in sequence]
print(doubled)

