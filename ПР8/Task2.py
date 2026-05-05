print("программа, которая считывает последовательность из 10 целых чисел и определяет, является ли каждое из них чётным.")
print("введите числа")

Proverka = 0

for i in range(1, 11):
    num = int(input(f"{i}:"))
    if num % 2 == 0:
        Proverka +=1
    elif num % 2 == 1:
        Proverka -=1

if Proverka == 10:
    print("Yes")
else:
    print("No")