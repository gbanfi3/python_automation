student_att = {"anna": 95,"bob":44, "adam":27}

for i in student_att:
    print(f"neve: {i}, magassága: {student_att[i]}")

for nev, magas in student_att.items():
    print(f"{nev}: {magas}")