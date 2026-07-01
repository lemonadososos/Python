def is_prime(number):
    if number == 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    else:
        return True

def get_next_prime(number):
    prime = number + 1
    while not is_prime(prime):
        prime += 1
    return prime




print(get_next_prime(6))
print(get_next_prime(7))
print(get_next_prime(14))
