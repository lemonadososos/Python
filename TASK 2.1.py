import math

print("высчитывание самого короткого пути c округлением до 2 цифр после запятой")


def dist (x1,y1,x2,y2):
    distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    return distance

x1,y1 = map(float,input("Введите координаты первой точки (x y): ").split())
x2,y2 = map(float,input("Введите координаты второй точки (x y): ").split())

print(f"Расстояние между точками: {dist(x1, y1, x2, y2):.2f} единиц")
