print("программа выводит все символы введённых слов(с повторением)")

kolvo_strok = int(input("введите количество строк со словами:"))

spisok =[]

for i in range(kolvo_strok):
    a = input("введите слово: ")
    b = list(a)
    spisok.extend(b)

spisok.sort()
print("список всех букв с повторением:", end=" ")
print(*spisok, sep=", ")