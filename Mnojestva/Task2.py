word1 = input("Введите первое слово: ")
word2 = input("Введите второе слово: ")

letters1 = set(word1)
letters2 = set(word2)

obshie_letters = letters1.intersection(letters2)
print("Общие буквы:", end=" ")
print(*obshie_letters, sep=", ")

just_letters1 = letters1.difference(letters2)
print("Буквы толко в первом слове:", end=" ")
print(*just_letters1, sep=", ")

just_letters2 = letters2.difference(letters1)
print("Буквы толко во втором слове:", end=" ")
print(*just_letters2, sep=", ")

