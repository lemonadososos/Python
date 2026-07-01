print(" Программа округляет действительное число в большую и в меньшую сторону и складывает вышедшие числа")

import math

num = float(input("введите число"))

minnum_plus_maxnum = math.ceil(num) + math.floor(num)
print(minnum_plus_maxnum)