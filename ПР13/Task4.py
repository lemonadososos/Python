a = input("введите IP-адрес: ")

IP = a.split(".")

if len(IP) != 4:
    print("Некоректный IP")
    exit()
for i in range(len(IP)):
    IP[i] = int(IP[i])
    if IP[i] > 255 or IP[i] < 0:
        print("Некоректный IP")
        exit()

print(*IP,sep=".", end=" ")
print(" - корректный IP")