group_1 = {'Иван', 'Мария', 'Петр', 'Сергей', 'Анна'}
group_2 = {'Мария', 'Анна', 'Дмитрий', 'Елена', 'Сергей'}

all_group_students = group_1.intersection(group_2)
print("Студенты в обоих группах:", end=" ")
print(*all_group_students, sep=", ")

just_group1 = group_1.difference(group_2)
print("Студенты только в первой группе:", end=" ")
print(*just_group1, sep=", ")

just_group2 = group_2.difference(group_1)
print("Студенты только во втрой группе:", end=" ")
print(*just_group2, sep=", ")

all_students = group_1.union(group_2)
print("Студенты хотя бы в одной группе:", end=" ")
print(*all_students, sep=", ")

just_one_group_stundents = group_1.symmetric_difference(group_2)
print("Студенты тоько в одной группе:", end=" ")
print(*just_one_group_stundents, sep=", ")
