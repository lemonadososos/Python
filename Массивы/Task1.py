prices = [100,50,200,150]

print(f'минимальная цена: {min(prices)}, максимальная цена: {max(prices)}')
print(f'средняя цена: {int(sum(prices)/len(prices))}')
print(*prices, sep=',')