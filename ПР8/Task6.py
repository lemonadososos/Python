import random

print("угадайте число от 1 до 10")

number = random.randint(1, 10)
num = 0

for popitka in range(1,4):
    num = int(input(f"попытка {popitka}: "))
    if num == number:
        print("поздравляю! вы угадали")
        break
    else:
        print("неправильное число")
        if popitka < 3:

            if num > number:
                print("число меньше")
            else:
                print("число больше")
        else:
            print("попытки кончились")