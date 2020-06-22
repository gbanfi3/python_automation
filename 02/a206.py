friends = {'bob', 'rolf', 'anne'}
abroad = {'bob', 'anne', 'mary'}

local_friends = friends.difference(abroad)
print(local_friends)

all_friends = friends.union(abroad)
print(all_friends)

intersection_friends = friends.intersection(abroad)
print(intersection_friends)