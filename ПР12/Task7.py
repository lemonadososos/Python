print("поиск числа из списка")

numbers = [10, 20, 30, 40, 50]
num = int(input("введите число: "))
flag = False

for i in range (len(numbers)):
    if numbers[i] == num:
        print(f"{num} находится в списке с индексом {i}")
        flag = True
        break
if not flag:
    print("Нет такого числа")
