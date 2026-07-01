def is_prime(number):
    if number == 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    else:
        return True


print(is_prime(1))
print(is_prime(10))
print(is_prime(17))
