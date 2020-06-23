import sys
users = [(0,"aa", "11"),(1,"bb", "22"),(2,"cc", "33"),(3,"dd", "44")]

for i in users:
    print(i)

user_mapping = { u[1]: u for u in users}
print(user_mapping)

input_username = input("mi a neved ?: ")
if not input_username in user_mapping.keys():
    print("nincs ilyen user")
    sys.exit(1)

input_pw = input("password?: ")

_, name, pw = user_mapping[input_username]
if input_pw == pw:
    print("ok")
else:
    print("nem OK")
