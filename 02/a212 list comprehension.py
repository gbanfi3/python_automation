friends = ['Rolf', 'Samantha', 'Sam', 'Jen', 'Sauab']
aa = []
for f in friends:
    if f.startswith("S"):
        aa.append(f)
print(aa)

bb = [f for f in friends if f.startswith("S")]
print(bb)

print('friends: ', id(friends))

