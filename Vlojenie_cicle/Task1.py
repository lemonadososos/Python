print("Шахматное поле")

flag = True

for i in range(1,9):
    if flag == True:
        flag = False
    else:
        flag = True
    for j in range(1,9):
        if flag == True:
            print("B",end=" ")
            flag = False
            continue
        if flag == False:
            print("W",end=" ")
            flag = True
            continue
    print()