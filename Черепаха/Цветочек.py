import turtle


side = int(input())
turn = float(input())
kolvo = int(input())
turtle.speed(0)

for k in range(kolvo):
    if k >= 1:
        turtle.left(turn)
    for i in range(4):
        if i >= 1:
            turtle.forward(side)
            turtle.left(90)
            turtle.left(90)
            turtle.forward(side)
            if i >= 2:
                turtle.left(90)
                if i >= 3:
                    turtle.right(90)
        for j in range(4):
            turtle.forward(side)
            turtle.left(90)


turtle.done()
