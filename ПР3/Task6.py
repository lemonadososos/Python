name = input("Ваше имя: ")
age = int(input("Ваш возраст: "))
subjects_str = input("Ваши любимые предметы(через запятую): ")

subjects_list = subjects_str.split(",")

student = {"name": name,
           "age": age,
           "subjects": subjects_list}


print("="*30)
print("АНКЕТА СТУДЕНТА")
print("="*30)

print(f" Имя: {student['name']} ")
print(f" Возраст: {student['age']} ")
print(f" Любимые предметы: {student['subjects']} ")