import turtle

side = int(input())
turtle.penup()
turtle.shape('turtle')
turtle.pensize(5)
turtle.Screen().bgcolor('light blue')

for j in range(6):
        turtle.left(30)
        for i in range(2):
            turtle.forward(side-(side/4))
            turtle.pendown()
            turtle.forward(side/4 - (side/6))
            turtle.penup()
            turtle.forward(side/6)
            turtle.stamp()
            turtle.left(180)
            turtle.forward(side)
turtle.right(180)

turtle.done()