grades = (22,45,1,74,29)
sum1 = 0
hany = len(grades)
for i in range(hany):
    sum1 += grades[i]
print(f"átlag= {sum1/hany}")

sum2 = sum(grades)
print(f"átlag= {sum2/hany}")

