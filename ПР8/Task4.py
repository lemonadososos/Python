print("программу, которая предсказывает размер популяции организмов с 1‑го по n‑й день (включительно)")

m = int(input("введите стартовое количество организмов:  "))
p = int(input("введите процент повышения популяции в день"))
n = int(input("введите количество дней"))
procent= p/100
population = m

print(f"Популяция в 1 день = {population}")
for i in range(2,n+1):
    population = int(m * (1 + procent)**i-1)
    print(f"Популяция в {i} день = {population}")