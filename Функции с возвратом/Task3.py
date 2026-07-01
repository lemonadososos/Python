def get_middle_point(x1, y1, x2, y2):
   x12 = (x1 + x2)/2
   y12 = (y1 + y2)/2
   return x12, y12


print(*get_middle_point(0, 0, 10, 0))
print(*get_middle_point(1, 5, 8, 3))
