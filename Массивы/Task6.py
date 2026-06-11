print("программа покажет полидром это или нет")

text = input("введите слово: ")
lista = list(text)

if lista == lista[::-1]:
    print(f'{text} это полидром')
else:
    print(f"{text} это не полидром")