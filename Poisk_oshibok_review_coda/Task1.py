n = int(input())  #было просто n = input(). Это была бы строка, которая в дальнейшем выдаст ошибки
product = 1 # было product = n % 10, это изменение нужно чтобы однозначные числа не изменялись и ответ был корректным
while n > 0:  # было while n >= 10: ,
    digit = n % 10
    product = product * digit
    n //= 10
print(product)