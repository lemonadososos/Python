for e in range(1,151):
    for a in range(1,151):
        for b in range(1, 151):
            for c in range(1, 151):
                for d in range(1,151):
                    if e ** 5 == a ** 5 + b ** 5 + c ** 5 + d ** 5:
                        print(f"{e}^5 = {a}^5 + {b}^5 + {c}^5 + {d}^5")
