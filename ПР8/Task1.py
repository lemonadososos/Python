print("программа показывает таблицу умножения на заданное число (от 1 до 10)")

number = int(input("введите число от 1 до 10:  "))
otvet = 0

if number > 10 or number < 1:
    print("введено число вне диапазона")
else:
    for i in range(1,11):
        otvet = number*i
        print(f"{number} x {i} = {otvet}")