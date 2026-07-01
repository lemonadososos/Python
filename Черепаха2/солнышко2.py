import turtle

side = int(input())
turn = int(input())
turtle.shape()

for i in range(turn//2):
        turtle.right(360/turn)
        turtle.dot(10)
        for j in range(2):
            turtle.forward(side)
            turtle.stamp()
            turtle.left(180)
            turtle.forward(side)





turtle.done()