def get_days(month):
    if month <= 7:
        if month != 2:
            if month % 2 == 0:
                return 30
            else:
                return 31
        else :
            return 28
    else:
        if month % 2 == 0:
            return 31
        else:
            return 30


print(get_days(1))
print(get_days(2))
print(get_days(9))
