import turtle
# --- Настройки экрана ---
t = turtle.Turtle()
t.speed(0)
t.hideturtle()
screen = turtle.Screen()
screen.bgcolor("lightblue")
screen.setup(width=800, height=700)


# =====================================================
# ПАРА 1 — СОЛНЫШКО
# =====================================================

t.color("orange")
t.width(6)
for i in range(16):
    t.penup()
    t.goto(300, 250)
    t.pendown()
    t.setheading(i * 22.5)
    t.forward(90)
t.width(1)
t.penup()
t.goto(275, 195)
t.pendown()
t.color("yellow")
t.begin_fill()
t.circle(60)
t.end_fill()

turtle.done()