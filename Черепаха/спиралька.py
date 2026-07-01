import turtle

n = int(input())
d = 10

for i in range(n):
    for j in range(4):
        turtle.left(90)
        turtle.forward(d)
        d += 5
turtle.left(90)
turtle.forward(d)
turtle.done()