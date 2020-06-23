# def divide(a,b):
#     if b == 0:
#         raise ValueError
#     return a/b
#
# def calculate(*pars, operator):
#     return operator(*pars)
#
# c = calculate(2,0, operator=divide)
# print(c)
import typing
from operator import itemgetter

# from builtins import function

friends = [
    {'name': "aa bb", 'age': 22},
    {'name': "aa cc", 'age': 55},
    {'name': "ff bb", 'age': 22},
    {'name': "xx ee", 'age': 33},
    {'name': "ff mm", 'age': 22}
]


def search(sequence: typing.List, expected: str, finder):
    for i in sequence:
        if finder(i) == expected:
            return i
    raise RuntimeError(f"nem találtam meg őt: {expected}")


def get_name(a):
    return a['name']
a = search(friends, "ff bb", get_name)

a = search(friends, "ff bb", itemgetter("name"))

a = search(friends, "ff bb", lambda a: a["name"])


print(a)
