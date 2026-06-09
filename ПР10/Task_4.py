print("Программа считает сумму цен на товары пока не будет введено 0(это будет озгачать остановку)")

all_price = 0

while True:
    price = int(input("введите сумму товара: "))
    if price == 0:
        break
    if price < 0:
        print("Ошибка цены")
        continue
    all_price += price

if all_price > 1000:
    all_price -= (all_price * 0.1)

print(f"полная цена = {all_price} руб.")