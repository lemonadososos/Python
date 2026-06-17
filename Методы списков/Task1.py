prices_str = '100 50 200 150 75 300'

prices = prices_str.split()
print(prices)

for i in range (len(prices)):
    prices[i] = int(prices[i])
print(prices)

prices.sort()
max_price = prices.pop()
print(max_price)
print(prices)

prices.append((max_price)//2)
print(prices)

prices.sort()
print(prices)

print(*prices, sep=', ')

print(f'средняя цена {sum(prices) // len(prices)}')