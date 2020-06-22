import sys
user_age = input("hány éves vagy?: ")
try:
    age = int(user_age)
except:
    print("nem jó: {}".format(ValueError))
    sys.exit(1)
print(f"ennyi hónapos vagyok: {age*12}")