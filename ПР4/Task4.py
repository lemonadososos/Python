print("программа делит мандарины между школьника и показывает сколько осталось неподелённых")

kolvo_shkolnikov = int(input("Количество школьников: "))
kolvo_mandarinov = int(input("Количество мандаринов: "))

skolnik = kolvo_mandarinov // kolvo_shkolnikov
korzina = kolvo_mandarinov % kolvo_shkolnikov

print(f" Каждому школьнику достаётся {skolnik} мандаринов")
print(f" В корзине осталось {korzina} мандаринов")