print("Знакочередующаяся сумма")

num = int(input("введите число до которого будет идти вычисление:  "))
summa = 1

for i in range(2,num+1):
    if i % 2 == 0:
        summa = summa - i
    else:
        summa = summa + i

print(f"1-2+3-4+5...+(-1)^(n+1)*{num}={summa}")