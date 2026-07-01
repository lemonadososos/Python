import turtle

t = turtle.Turtle()
t.speed(0)
t.hideturtle()
screen = turtle.Screen()
screen.bgcolor("lightblue")
screen.setup(width=800, height=700)

# =====================================================
# ПАРА 2 — ОБЛАКО
# =====================================================


def clouds (CLOUD_COLOR):
    t.color(CLOUD_COLOR)
    for i in range(3):
        for circle_x, circle_y, radius in coords:
            if i >= 1:
                circle_x -= 170
                circle_y -= 80
            if i >= 2:
                circle_x -= 160
                circle_y += 60
            t.penup()
            t.goto(circle_x, circle_y - radius)
            t.pendown()
            t.begin_fill()
            t.circle(radius)
            t.end_fill()


coords = [
    (100, 280, 40),
    (70, 290, 30),
    (130, 290, 30),
    (50, 270, 25),
    (150, 270, 25),
    (100, 260, 35)
]

clouds("white")

turtle.done()