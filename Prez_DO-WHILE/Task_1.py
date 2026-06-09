PASSWORD = "admin"
ATTEMPTS = 3

while True:
    attempt = input("введите пароль: ")
    if attempt != PASSWORD:
        ATTEMPTS += 1
        print("Неверный пароль")
        if ATTEMPTS == 3:
            break
    if attempt == PASSWORD:
        print("Доступ разрешён")
        break