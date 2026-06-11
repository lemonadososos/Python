print("все нечётны числа от 1 до n")

n = int(input("введите число:"))
nechet_chislo = [1, ]

for i in range(3,n+1):
    if i % 2 == 1:
        nechet_chislo.append(i)
print(nechet_chislo)