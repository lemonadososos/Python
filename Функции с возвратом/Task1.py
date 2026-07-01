print("Программа переводит километры в мили")

def convert_to_miles(kilometers):
    miles = round(kilometers * 0.62137, 4)
    return miles

print(convert_to_miles(1))
print(convert_to_miles(5))
print(convert_to_miles(10))
