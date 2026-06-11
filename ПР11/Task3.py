kolvo = 0
a = 1
b = 1
c = 1
d = 1

for e in range(1,151):
    print(e)
    for a in range(1,151):
        if e ** 5 == a ** 5 + b ** 5 + c ** 5 + d ** 5:
            print(f"{e}^5 = {a}^5 + {b}^5 + {c}^5 + {d}^5")
            kolvo += 1
