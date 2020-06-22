import random, sys

magic_number = random.randint(1,9)
print(f"magic_number: {magic_number}")
if input("ha nem akarsz játszani, írd N: ") in "ennek":
    print("nem akarsz játszani")
    sys.exit(1)
else:
    print("ha ki akarsz szállni, írj valami nem számot")
    while True:
        c = input("mit tippelsz?: ")
        try:
            c_num = int(c)
        except:
            print("nem számot adtál, ezért kilépek")
            sys.exit(1)
        if c_num == magic_number:
            print(f"eltaláltad: {magic_number}")
            sys.exit(0)
        elif abs(c_num-magic_number) == 1:
            print("távolság: 1")
        else:
            print("nem találtad el, ", end='')


