import turtle

side = int(input())
turtle.speed(5)

for i in range(6):
    turtle.left(120)
    for j in range(7):
        turtle.forward(side)
        turtle.right(60)
turtle.done()