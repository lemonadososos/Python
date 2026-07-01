import math


def calculate_rectangle_area(width, height):
    """
    Считает площадь прямоугольника

    Args:
        width(int): Ширина прямоугольника
        height(int): Высота прямоугольника
    Returns:
        int: Площадь прямоугольника
    """
    return width * height

def  calculate_circle_area(radius):
    """
    Считает площадь круга

    Args:
        radius(int): радиус круга

    Returns:
        float: площадь круга
    """
    return math.pi * radius * radius

w = int(input("Ширина прямоугольника: "))
h = int(input("Высота прямоугольника: "))

print(f"Площадь прямоугольника = {calculate_rectangle_area(w, h)}")

r = int(input("Радиус круга: "))

print(f"Площадь круга = {calculate_circle_area(r):.3f}")