import turtle

side = int(input())
turn = int(input())

for j in range(3):
        turtle.left(turn)
        for i in range(4):
            turtle.forward(side)
            turtle.left(90)





turtle.done()