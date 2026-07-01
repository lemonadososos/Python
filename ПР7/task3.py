
print("","‾"*45,"")
print(" ", " "*2,"Напиток 1 -    Кофе☕.   цена - 120 руб"," "," " )
print(" ", " "*2,"Напиток 2 -     Чай🍵.   цена -  80 руб"," "," " )
print(" ", " "*2,"Напиток 3 -     Сок🧃.   цена - 100 руб"," "," " )
print(" ", " "*2,"Напиток 4 -    Вода💧.   цена -  50 руб"," "," " )
print(" ", " "*2,"Напиток 5 - Лимонад🥤.   цена -  90 руб"," "," " )
print("","—"*45,"" )

order = input("Введите номер или название напитка: ")
quantity = int(input("Введите количество, сколько напитков вам нужно: "))
tea = 80
coffee = 120
juice = 100
water = 50
lemonade = 90
skidka_word = "STUDENT"
skidka = input("Введите скидку, если она у вас есть: ")
if skidka == skidka_word:

    match order:
        case "1"|"Кофе" | "☕":
            price=coffee * quantity
            discount = coffee * 0.2
            discount_quantity = discount * quantity
            discount_price = price - discount_quantity
            print("", "‾" * 45, "")
            print(" ", " " * 8, "☕КВИТАНЦИЯ ТОВАРА☕", " ", " ")
            print("", "‾" * 45, "")
            print("Товар: Кофе☕")
            print(f"Цена за порцию: {coffee} руб.")
            print(f"Количество: {quantity} порции")
            print(f"Сумма: {price} руб")
            print(" ")
            print(f"скидка 'STUDENT' (20%): -{discount_quantity} руб")
            print("=====================")
            print(f"К оплате {discount_price} руб.")
            print("=====================")
        case "2"|"Чай"|"🍵":
            price=tea * quantity
            discount = tea * 0.2
            discount_quantity = discount * quantity
            discount_price = price - discount_quantity
            print("", "‾" * 45, "")
            print(" ", " " * 8, "🍵КВИТАНЦИЯ ТОВАРА🍵", " ", " ")
            print("", "‾" * 45, "")
            print("Товар: Чай🍵")
            print(f"Цена за порцию: {tea} руб.")
            print(f"Количество: {quantity} порции")
            print(f"Сумма: {price} руб")
            print(" ")
            print(f"скидка 'STUDENT' (20%): -{discount_quantity} руб")
            print("=====================")
            print(f"К оплате {discount_price} руб.")
            print("=====================")
        case "3"|"Сок"|"🧃":
            price=juice * quantity
            discount = juice * 0.2
            discount_quantity = discount * quantity
            discount_price = price - discount_quantity
            print("", "‾" * 45, "")
            print(" ", " " * 8, "🧃КВИТАНЦИЯ ТОВАРА🧃", " ", " ")
            print("", "‾" * 45, "")
            print("Товар: Сок🧃")
            print(f"Цена за порцию: {juice} руб.")
            print(f"Количество: {quantity} порции")
            print(f"Сумма: {price} руб")
            print(" ")
            print(f"скидка 'STUDENT' (20%): -{discount_quantity} руб")
            print("=====================")
            print(f"К оплате {discount_price} руб.")
            print("=====================")
        case "4"|"Вода"|"💧":
            price=water * quantity
            discount = water * 0.2
            discount_quantity = discount * quantity
            discount_price = price - discount_quantity
            print("", "‾" * 45, "")
            print(" ", " " * 8, "💧КВИТАНЦИЯ ТОВАРА💧", " ", " ")
            print("", "‾" * 45, "")
            print("Товар: Вода💧")
            print(f"Цена за порцию: {water} руб.")
            print(f"Количество: {quantity} порции")
            print(f"Сумма: {price} руб")
            print(" ")
            print(f"скидка 'STUDENT' (20%): -{discount_quantity} руб")
            print("=====================")
            print(f"К оплате {discount_price} руб.")
            print("=====================")
        case "5"|"Лимонад"|"🥤":
            price=lemonade * quantity
            discount = lemonade * 0.2
            discount_quantity = discount * quantity
            discount_price = price - discount_quantity
            print("", "‾" * 45, "")
            print(" ", " " * 8, "🥤КВИТАНЦИЯ ТОВАРА🥤", " ", " ")
            print("", "‾" * 45, "")
            print("Товар: Лимонад🥤")
            print(f"Цена за порцию: {lemonade} руб.")
            print(f"Количество: {quantity} порции")
            print(f"Сумма: {price} руб")
            print(" ")
            print(f"скидка 'STUDENT' (20%): -{discount_quantity} руб")
            print("=====================")
            print(f"К оплате {discount_price} руб.")
            print("=====================")
        case _:
            print("Ошибка. Данного напитка нет в нашей базе")
else:
    match order:
        case "1" | "Кофе" | "☕":
            price = coffee * quantity
            print("", "‾" * 45, "")
            print(" ", " " * 8, "☕КВИТАНЦИЯ ТОВАРА☕", " ", " ")
            print("", "‾" * 45, "")
            print("Товар: Кофе☕")
            print(f"Цена за порцию: {coffee} руб.")
            print(f"Количество: {quantity} порции")
            print(f"Сумма: {price} руб")
            print("=====================")
            print(f"К оплате {price} руб.")
            print("=====================")
        case "2" | "Чай" | "🍵":
            price = tea * quantity
            print("", "‾" * 45, "")
            print(" ", " " * 8, "🍵КВИТАНЦИЯ ТОВАРА🍵", " ", " ")
            print("", "‾" * 45, "")
            print("Товар: Чай🍵")
            print(f"Цена за порцию: {tea} руб.")
            print(f"Количество: {quantity} порции")
            print(f"Сумма: {price} руб")
            print("=====================")
            print(f"К оплате {price} руб.")
            print("=====================")
        case "3" | "Сок" | "🧃":
            price = juice * quantity
            print("", "‾" * 45, "")
            print(" ", " " * 8, "🧃КВИТАНЦИЯ ТОВАРА🧃", " ", " ")
            print("", "‾" * 45, "")
            print("Товар: Сок🧃")
            print(f"Цена за порцию: {juice} руб.")
            print(f"Количество: {quantity} порции")
            print(f"Сумма: {price} руб")
            print("=====================")
            print(f"К оплате {price} руб.")
            print("=====================")
        case "4" | "Вода" | "💧":
            price = water * quantity
            print("", "‾" * 45, "")
            print(" ", " " * 8, "💧КВИТАНЦИЯ ТОВАРА💧", " ", " ")
            print("", "‾" * 45, "")
            print("Товар: Вода💧")
            print(f"Цена за порцию: {water} руб.")
            print(f"Количество: {quantity} порции")
            print(f"Сумма: {price} руб")
            print("=====================")
            print(f"К оплате {price} руб.")
            print("=====================")
        case "5" | "Лимонад" | "🥤":
            price = lemonade * quantity
            print("", "‾" * 45, "")
            print(" ", " " * 8, "🥤КВИТАНЦИЯ ТОВАРА🥤", " ", " ")
            print("", "‾" * 45, "")
            print("Товар: Лимонад🥤")
            print(f"Цена за порцию: {lemonade} руб.")
            print(f"Количество: {quantity} порции")
            print(f"Сумма: {price} руб")
            print("=====================")
            print(f"К оплате {price} руб.")
            print("=====================")
        case _:
            print("Ошибка. Данного напитка нет в нашей базе")