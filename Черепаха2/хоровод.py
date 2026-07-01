import turtle

side = int(input())
turtle.penup()
turtle.shape('turtle')

for j in range(5):
        turtle.left(36)
        for i in range(2):
            turtle.forward(side)
            turtle.stamp()
            turtle.left(180)
            turtle.forward(side)
turtle.right(180)




turtle.done()