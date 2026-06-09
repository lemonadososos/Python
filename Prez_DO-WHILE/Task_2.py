proizvedenie = 1

while True:
    num = int(input("введите число для умножения на общее произведение(вначале 1): "))
    if num < 0:
        break
    proizvedenie *= num
    print(proizvedenie)