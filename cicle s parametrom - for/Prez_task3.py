m,n = map(int,input("введите 2 числа(m n):").split())

if m > n:
    for i in range(n,m+1):
        print(i)
else:
    for i in range(n,m-1,-1):
        print(i)
