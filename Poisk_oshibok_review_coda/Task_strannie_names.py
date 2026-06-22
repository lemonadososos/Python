s = input()

while len(s) < 10:         # меньше 10
    if len(s) % 4 == 0:    # кратна 4
        s = s + 'x'
    elif len(s) % 5 == 0:  #кратно 5
        s = s + 'y'
    else:
        s = 'z' + s       # символ z  должен быть слева
s = '@' + s               # символ @, а не &
print(s)