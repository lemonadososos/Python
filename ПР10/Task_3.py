print("Программа выбирает самое большое число из введённых. Если ввести 0, то программа остановится и выведет число")

max_num = 0

while True:
    num = int(input("введите число: "))
    if num > max_num:
        max_num = num
    if num == 0:
        break

print(f"{max_num} - наибольшее число")