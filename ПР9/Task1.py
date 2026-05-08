print("программа показывает ряд чисел до введённого исключая 5-9, 17-37, 78-87")

num = int(input("введите число:"))
chislo = 1

while chislo <= num:
    if chislo < 5 or chislo > 9 or chislo < 17 or chislo > 37 or chislo < 78 or chislo > 87:
        print(chislo)
        chislo += 1
    else:
        chislo += 1
