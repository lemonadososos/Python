print("Программа считает в каком купе находится место по выбранному номеру")


place_num = int(input("Введите номер своего места:"))   #номер места в вагоне

STEARS_PER_COMP = 4   #количество мест в купе

#вычисление
kupe_num = (place_num-1)//STEARS_PER_COMP+1
print("Место",place_num, "находится в купе", kupe_num)