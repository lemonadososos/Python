numb = input("введите числа черезх пробел: ")

snumb = numb.split()
para = 0

for i in range(len(snumb)):
    for j in range(i+1, len(snumb)):
        if snumb[i] == snumb[j]:
            para += 1
print(f"{para} пар чисел")