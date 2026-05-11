print("Ведьмаку заплатите чеканой монетой")

price = int(input("введите количество крон, которые нужно заплвтить ведьмаку:  "))
coin = 0
coin_sum = 0

while price > 0:
    if price >= 25:
        coin = price//25
        coin_sum += coin
        price = price - coin * 25
    if price >= 10:
        coin = price//10
        coin_sum += coin
        price = price - coin * 10
    if price >= 5:
        coin = price//5
        coin_sum += coin
        price = price - coin * 5
    if price >= 1:
        coin = price//1
        coin_sum += coin
        price = price - coin * 1
print(f"минимальное количество монет(1, 5, 10 или 25 номинала): {coin_sum}")