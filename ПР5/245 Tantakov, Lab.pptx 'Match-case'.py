print("Вы запустили программу определение сезона! \n")

month = int(input("Введите номер месяца (от 1 до 12): "))

jan = ("Номер месяца: 1 \n"
       "Введённый месяц: январь\n"
       "Соответствующий emoji: ❄️\n")

feb = "Введённый месяц: февраль"

march = "Введённый месяц: март"
april = "Введённый месяц: апрель"
may = "Введённый месяц: май"
june = "Введённый месяц: июнь"
july = "Введённый месяц: июль"
august = "Введённый месяц: август"
september = "Введённый месяц: сентябрь"
oct = "Введённый месяц: октябрь"
nov = "Введённый месяц: ноябрь"
dec = "Введённый месяц: декабрь"

match month:
    case 1:
        print(jan)
    case 2:
        print(feb)
    case 3:
        print(march)
    case 4:
        print(april)
    case 5:
        print(may)
    case 6:
        print(june)
    case 7:
        print(july)
    case 8:
        print(august)
    case 9:
        print(september)
    case 10:
        print(oct)
    case 11:
        print(nov)
    case 12:
        print(dec)

    case _:
        print("Вы ввели неверный номер месяца! Пожалуйста, введите число от 1 до 12\n")

input("Нажмите Enter, чтобы закрыть программу...")


