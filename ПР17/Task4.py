def is_password_good(password):

    has_lower = False
    has_digit = False
    has_upper = False

    if len(password) < 8:
        return False
    elif len(password) > 8 :
        for i in password:
            if i.islower() :
                has_lower = True
            if i.isdigit():
                has_digit = True
            if i.isupper():
                has_upper = True
        return has_lower and has_digit and has_upper

print(is_password_good('aabbCC11OP'))
print(is_password_good('abC1pu'))
