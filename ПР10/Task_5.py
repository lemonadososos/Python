print("Меню банкомата")

print("""1. Узнать баланс
2. Снять 100 руб
3. Положить 100 руб
4. Выход
""")

balance = 1000

while True:
    select_num = int(input("выберите действие:"))
    if select_num == 1:
        print(f"ваш баланс: {balance}")
    elif select_num == 2:
        if balance >= 100:
            balance -= 100
            print("Снято")
        else:
            print("Недостаточно средств")
    elif select_num == 3:
        balance += 100
        print("Внесено")
    elif select_num == 4:
        break
    else:
        print("Неверная команда")


