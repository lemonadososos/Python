PASSWORD = 4590

while True:
    attempt = int(input("введите пароль: "))
    if attempt != PASSWORD:
        print("Ошибка. Попробуйте ещё раз")
    if attempt == PASSWORD:
        print("Доступ разрешён")
        break