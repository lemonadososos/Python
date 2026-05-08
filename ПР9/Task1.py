print("программа показывает ряд чисел до введённого исключая 5-9, 17-37, 78-87")

num = int(input("введите число:"))
chislo = 1

while chislo <= num:
    if (5 <= chislo <= 9) or (17 <= chislo <= 37) or (78 <= chislo <= 87):
        chislo += 1
        continue
    else:
        print(chislo)
        chislo += 1


