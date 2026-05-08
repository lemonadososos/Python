print("программа считает очередь между играми Александрой и Левоном. Александра должна быть раньше")

ochered_aleksandra =0
ochered_levon = 0
ochered= 1

while True:
    name = input(f"введите имя участника {ochered}: ")
    if name == "Александра":
        ochered_aleksandra = ochered
    if name == "Левон":
        ochered_levon = ochered
    if name == "стоп":
        break
    ochered += 1

if ochered_aleksandra > ochered_levon:
    print("ошибка")
else:
    print(f"очередь между играми Александрой и Левоном = {ochered_levon - ochered_aleksandra-1}")