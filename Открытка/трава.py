import turtle

t = turtle.Turtle()
t.speed(0)
t.hideturtle()
screen = turtle.Screen()
screen.bgcolor("lightblue")
screen.setup(width=800, height=700)
def grass (GRASS_COLOR, BLADE_COUNT, BLADE_HEIGHT, BLADE_HEIGHT_MOD, BLADE_TURN, START_X, START_Y):
    t.color(GRASS_COLOR)
    for i in range(BLADE_COUNT):
        t.penup()
        t.goto(START_X + i * 25, START_Y)
        t.pendown()
        d = 1 if i % 2 == 0 else -1
        t.setheading(75 + (i % 5) * 10)
        t.width(3 - (i % 2))
        n = BLADE_TURN + (i % BLADE_HEIGHT_MOD)
        for j in range(int(n / 10)):
            t.forward(BLADE_HEIGHT)
            t.left(5 * d)
        t.width(1)

grass("green", 35, 10, 30,70, -400, -300)

turtle.done()