print(" программа переводит минуты в часы и минуты")

minutes = int(input("Ввдеите количество минут: "))

hours = minutes // 60
ost_minutes = minutes - hours * 60

print(f"{minutes} мин - это {hours} час {ost_minutes} минут.")