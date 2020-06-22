student_att = {"anna": 95,"bob":44, "adam":27}

for i in student_att:
    print(f"neve: {i}, magassága: {student_att[i]}")

for nev, magas in student_att.items():
    print(f"{nev}: {magas}")

att_values = student_att.values()
print(att_values)
atlag = sum(att_values) / len(att_values)
print(f"{atlag:.2f}")