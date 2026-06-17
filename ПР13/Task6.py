numbers = [1, 2, 3]
print(numbers)

numbers.insert(1, 17)
print(numbers)

numbers.extend([4, 5, 6])
print(numbers)

del numbers[0]
print(numbers)

numbers.extend(numbers)
print(numbers)

numbers.insert(3, 25)
print(numbers)


