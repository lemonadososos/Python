import turtle

t = turtle.Turtle()
t.speed(0)
t.hideturtle()
screen = turtle.Screen()
screen.bgcolor("lightblue")
screen.setup(width=800, height=700)

# =====================================================
# ПАРА 3 — ЦВЕТОК
# =====================================================

def flower (STEM_LENGTH, PETAL_COUNT, PETAL_RADIUS, CENTER_RADIUS, PETAL_COLOR, CENTER_COLOR,STEM_COLOR, STEM_WIDTH, FLOWER_COORDS):
    t.color(STEM_COLOR)
    t.width(STEM_WIDTH)
    t.penup()
    t.goto(FLOWER_COORDS, -300)
    t.pendown()
    t.setheading(90)
    t.forward(STEM_LENGTH)
    t.width(1)
    t.color(PETAL_COLOR)
    for i in range(PETAL_COUNT):
        t.penup()
        t.goto(FLOWER_COORDS, -180)
        t.pendown()
        t.setheading(i * 45)
        t.begin_fill()
        t.circle(PETAL_RADIUS)
        t.end_fill()
    t.penup()
    t.goto(FLOWER_COORDS-15, -195)
    t.pendown()
    t.color(CENTER_COLOR)
    t.begin_fill()
    t.circle(CENTER_RADIUS)
    t.end_fill()

flower(120, 8, 30, 20, "pink", "yellow", "darkgreen", 4, 0)
flower(120, 8, 30, 20, "blue", "yellow", "darkgreen", 4, -160)
flower(120, 8, 30, 20, "orange", "yellow", "darkgreen", 4, 160)


turtle.done()