print("делит путь к файлу на отдельные элементы")

put_faila = input("введите путь файла")
parts = put_faila.split('\\')

for i in range(len(parts)):
    a = parts[i]
    print(a)