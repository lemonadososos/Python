num = int(input("введите число: "))

number3 = 0
last_num = 0
chet_num = 0
sum_num_bol_5 = 0
umn_num_7 = 1
sum_num_0_and_5 = 0
count_num = len(str(num))
digits = list(map(int, str(num)))
cifri = 0

while cifri < count_num  :
    if digits[cifri] == 3 :
        number3 += 1
    if digits[cifri] == digits[count_num - 1] :
        last_num += 1
    if digits[cifri]%2 == 0:
        chet_num += 1
    if digits[cifri] > 5:
        sum_num_bol_5 += 1
    if digits[cifri] > 7:
        umn_num_7 =  umn_num_7 * digits[cifri]
    if digits[cifri] == 0 or digits[cifri] == 5 :
        sum_num_0_and_5 += 1
    cifri = cifri + 1
else:
    print(f"количество цифр [3] в числе: {number3}")
    print(f"количество последних цифр в числе: {last_num}")
    print(f"количество чётных цифр в числе: {chet_num}")
    print(f"количество цифр больше 5 в числе: {sum_num_bol_5}")
    print(f"произведение цифр больше 7 в числе(минимум 1): {umn_num_7}")
    print(f"количество цифр [0] и [5] в числе: {sum_num_0_and_5}")