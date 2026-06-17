print("""Добро пожаловать в лабиринт!
Начало вашего пути это ⭐, а конец - 🎉.
Управляйте своим персонажем вводя [WASD].
После каждого ввода буквы нажимайте [Enter]

""")


labirint = "⬛⬛⭐⬛⬛🎉⬛⬜⬜⬜⬜⬛🔷⬛🪙⬜🧌⬜⬛⬜⬛⬛🪙🔷⬜"

if len(labirint) != 25:
    print("неправильное число элементов лабиринта")
    exit()
labirint_stok = []
for a in range(0,25):
    labirint_stok.append(labirint[a])

index_start = labirint.index("⭐")
row_start = index_start // 5
column_start = index_start % 5
print(f"Вход находится на {row_start+1} строке и {column_start+1} столбце")
distance =  abs(row_start - 2) + abs(1 - column_start)
print(f"""Растояние между началом и выходом: {distance} [без учёта стен]

""")

character = 2
character_index = "⭐"
back_step = "⬜"
money = 0
money_index = "🪙"
HP = 100
HP_index = "🩶"
damage = 0
damage_index = "🖤"
finish = False

while True:
    if finish == True:
        break
    step_value = False
    print("ваше здоровье: ", end="")
    print(HP_index*(HP//10),damage_index*(damage//10))
    print()
    for i in range(0,25,5):
        print(*labirint_stok[i: i+5])

    while step_value == False:
        step = input("введите куда хотите пойти: ")
        if step == "S":
            if labirint_stok[int(character)+5] == "⬛":
                print("нельзя пройти! Там стена")
                break
            if labirint_stok[int(character)+5] =="🪙":
                money += 1
                print("Поздравляю! Вы нашли монету🪙!")
            if labirint_stok[int(character)+5] =="🔷":
                HP -=10
                damage += 10
                print("О нет! Вы наткнулись на ловушку🔷!")
            if labirint_stok[int(character)+5] =="🧌":
                HP -=50
                damage += 50
                print("О нет! Вы наткнулись на монстра🧌! [-50 HP]")
            if labirint_stok[int(character) + 5] == "🎉":
                print("УРА! Вы прошли лабиринт!🎉")
                finish = True
                break
            labirint_stok[int(character)] = labirint_stok[int(character) + 5]
            character += 5
            labirint_stok[int(character)] = character_index
            labirint_stok[int(character)-5] = back_step
            step_value = True
        if step == "W":
            if labirint_stok[int(character)-5] == "⬛":
                print("нельзя пройти! Там стена")
                break
            if labirint_stok[int(character)-5] == "🪙":
                money += 1
                print("Поздравляю! Вы нашли монету🪙!")
            if labirint_stok[int(character)-5] =="🔷":
                HP -=10
                damage += 10
                print("О нет! Вы наткнулись на ловушку🔷!")
            if labirint_stok[int(character)-5] =="🧌":
                HP -=50
                damage += 50
                print("О нет! Вы наткнулись на монстра🧌! [-50 HP]")
            if labirint_stok[int(character) - 5] == "🎉":
                print("УРА! Вы прошли лабиринт!🎉")
                finish = True
                break
            labirint_stok[int(character)] = labirint_stok[int(character) - 5]
            character -= 5
            labirint_stok[int(character)] = character_index
            labirint_stok[int(character) + 5] = back_step
            step_value = True
        if step == "A":
            if labirint_stok[int(character)-1] == "⬛":
                print("нельзя пройти! Там стена")
                break
            if labirint_stok[int(character)-1] == "🪙":
                money += 1
                print("Поздравляю! Вы нашли монету🪙!")
            if labirint_stok[int(character)-1] =="🔷":
                HP -=10
                damage += 10
                print("О нет! Вы наткнулись на ловушку🔷!")
            if labirint_stok[int(character) -1] == "🧌":
                HP -= 50
                damage += 50
                print("О нет! Вы наткнулись на монстра🧌! [-50 HP]")
            if labirint_stok[int(character) -1] == "🎉":
                print("УРА! Вы прошли лабиринт!🎉")
                finish = True
                break
            labirint_stok[int(character)] = labirint_stok[int(character) - 1]
            character -= 1
            labirint_stok[int(character)] = character_index
            labirint_stok[int(character) + 1] = back_step
            step_value = True
        if step == "D":
            if labirint_stok[int(character)+1] == "⬛":
                print("нельзя пройти! Там стена")
                break
            if labirint_stok[int(character)+1] == "🪙":
                money += 1
                print("Поздравляю! Вы нашли монету🪙!")
            if labirint_stok[int(character)+1] =="🔷":
                HP -=10
                damage += 10
                print("О нет! Вы наткнулись на ловушку🔷!")
            if labirint_stok[int(character)+1] =="🧌":
                HP -=50
                damage += 50
                print("О нет! Вы наткнулись на монстра🧌! [-50 HP]")
            if labirint_stok[int(character) + 1] == "🎉":
                print("УРА! Вы прошли лабиринт!🎉")
                finish = True
                break
            labirint_stok[int(character)] = labirint_stok[int(character) + 1]
            character += 1
            labirint_stok[int(character)] = character_index
            labirint_stok[int(character) - 1] = back_step
            step_value = True

print(f"Вы собрали {money_index*money} монет")
print(f"Оставшееся здоровье:", end=" ")
print(HP_index*(HP//10),damage_index*(damage//10), end="")
print(f"{HP}%")
