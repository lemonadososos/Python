import turtle

n = int(input())
d = 10

for i in range(n):
    d += 5
    for j in range(4):
        turtle.backward(d)
        turtle.right(90)
turtle.done()