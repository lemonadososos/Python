import math

print("высчитывание самого короткого пути c округлением до 2 цифр после запятой")

x1,y1 = map(float,input("Введите координаты первой точки (x y): ").split())
x2,y2 = map(float,input("Введите координаты второй точки (x y): ").split())

distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)
print(f"Расстояние между точками: {distance:.2f} единиц")