print("числа от a до b")

a = int(input())
b = int(input())

print(a)
while (b > a):
    a +=1
    for i in range(1, b + 1):
        for j in range(1, b + 1):
            if i % j == 0:
                print(a, end=" ")