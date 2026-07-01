import math

x_gr = int(input("введите x в градусах: "))

x_rad = math.radians(x_gr)
trg = math.sin(x_rad) + math.cos(x_rad) + math.cos(x_gr)**2
print(trg)