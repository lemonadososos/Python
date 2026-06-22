n = int(input())
max_digit = n % 10
while n > 10 :       #при делении всегда будет больше нуля
    digit = n % 10
    if digit % 3 == 0:
        if digit > max_digit:   # нам нужно чтобы было наибольше, а не наименьшее
            max_digit = digit   #поменял местами чтобы получить максимальное кратное 3
    n = n // 10     #
if max_digit == 0:
    print('NO')
else:
    print(max_digit)