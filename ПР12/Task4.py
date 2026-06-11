marks = [5, 4, 3, 5, 2, 5, 4, 3, 5, 5]
print(marks)
length = len(marks)
mark5 = 0
mark2 = 0
for i in range(length):
    if marks[i] == 5:
        mark5 +=1
    if marks[i] == 2:
        mark2 +=1
print(f"количество цифр 5 в списке: {mark5}")
print(f"количество цифр 2 в списке: {mark2}")
