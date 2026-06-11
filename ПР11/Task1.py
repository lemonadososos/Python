mes30 = 0
mes31 = 0
mes28 = 0

for j in range(1,8):
     if j % 2 == 1:
        mes31 += 1
     elif j == 2:
        mes28 += 1
     else:
         mes30 += 1
for j in range(8,13):
     if j % 2 == 0:
        mes31 += 1
     else:
        mes30 += 1
print(f"{mes31}месяцев по 31 день")
print(f"{mes30}месяцев по 30 дней")
print(f"{mes28}месяцев по 28 дней")

