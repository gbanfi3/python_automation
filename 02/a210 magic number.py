import random, sys

magic_number = random.randint(1,9)
if input("akarsz játszani? (yes/bármi más): ").lower() != yes:
    sys.exit(1)
else:
    print("ha ki akarsz szállni, írj valami nem számot")
    while True:
        c = input("mit tippelsz?: ")
        try:
            c_num = int(c)
        except:
            print("kilépek")
            sys.exit(1)
        if c_num == magic_number:
            print(f"eltaláltad: {magic_number}")
        if abs(c_num,magic_number) == 1:
            print("távolság: 1")
        print("nem találtad el")

