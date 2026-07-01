def  is_valid_password(password):
    password = password.split(':')
    password_int = []
    for i in range(len(password)):
        password_int.append(int(password[i]))
    if password_int[0] != int(str(password_int[0])[::-1]):
        return False
    elif password_int[0] == int(str(password_int[0])[::-1]):
        return True
    if password_int[1] == 1:
        return False
    for i in range(2, password_int[1]):
            if password_int[1] % i == 0:
                return False
    else:
        return True
    if password_int[2] % 2 == 0:
        return False
    return True


print(is_valid_password('1221:101:22'))
print(is_valid_password('565:30:50'))
print(is_valid_password('112:7:9'))
print(is_valid_password('1221:101:22:22'))
