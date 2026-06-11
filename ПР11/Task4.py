num = int(input("введите число: "))

number3 = 0
last_num = 0
chet_num = 0
umn_num_7 = 1
count_num = len(str(num))
digits = list(map(int, str(num)))
cifri = 0

while True :
    if digits[cifri] == 3 :
        number3 += 1
    if digits[cifri] == digits[count_num - 1] :
        last_num += 1
    if digits[cifri]%2 == 0:
        chet_num += 1
    if digits[cifri] > 7:
        umn_num_7 =  umn_num_7 * digits[cifri]
    cifri = cifri + 1
    if cifri >= len(str(num)) :
        break

print(f"количество цифр [3] в числе: {number3}")
print(f"количество последних цифр в числе: {last_num}")
print(f"количество чётных цифр в числе: {chet_num}")
print(f"произведение цифр больше 7 в числе(минимум 1): {umn_num_7}")