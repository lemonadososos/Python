import random

print("программа меняет местами 1-е число и наименьшее в спсике. все числа в списке случайны(от 1 до 100)")

numbers = [random.randint(1,100),
           random.randint(1,100),
           random.randint(1,100),
           random.randint(1,100),
           random.randint(1,100),]
min_list = min(numbers)
first_list = numbers[0]
print(numbers)

numbers[0] = min_list
for i in range(1, len(numbers)):
    if numbers[i] == min_list:
        numbers[i] = first_list
print(numbers)