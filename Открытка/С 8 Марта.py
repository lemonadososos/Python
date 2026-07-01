import turtle
import random
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

def sun  (LINE_COLOR, SUN_COLOR,LINE_COUNT, LNIE_LENGTH, SUN_RADIUS):
    t.color(LINE_COLOR)
    t.width(6)
    for i in range(LINE_COUNT):
        t.penup()
        t.goto(300, 250)
        t.pendown()
        t.setheading(i * 22.5)
        t.forward(LNIE_LENGTH)
    t.width(1)
    t.penup()
    t.goto(275, 195)
    t.pendown()
    t.color(SUN_COLOR)
    t.begin_fill()
    t.circle(SUN_RADIUS)
    t.end_fill()

sun("orange", "yellow", 16, 90, 60)

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

# =====================================================
# ПАРА 3 — ЦВЕТОК
 # =====================================================

def flower (STEM_LENGTH, PETAL_COUNT, PETAL_RADIUS, CENTER_RADIUS, PETAL_COLOR, CENTER_COLOR,STEM_COLOR, STEM_WIDTH, FLOWER_COORDS):
    t.color(STEM_COLOR)
    t.width(STEM_WIDTH)
    t.penup()
    t.goto(FLOWER_COORDS, -350)
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




# =====================================================
# ПАРА 5 — ТРАВА
# =====================================================

def grass (GRASS_COLOR, BLADE_COUNT, BLADE_HEIGHT, BLADE_HEIGHT_MOD, BLADE_TURN, START_X, START_Y, GRASS_OFFSET):
    t.color(GRASS_COLOR)
    for i in range(BLADE_COUNT):
        t.penup()
        t.goto(START_X + i * random.randint(GRASS_OFFSET,GRASS_OFFSET + 5), START_Y)
        t.pendown()
        d = 1 if i % 2 == 0 else -1
        t.setheading(75 + (i % 5) * 10)
        t.width(3 - (i % 2))
        n = BLADE_TURN + (i % BLADE_HEIGHT_MOD)
        for j in range(int(n / 10)):
            t.forward(random.randint(BLADE_HEIGHT, BLADE_HEIGHT + 5))
            t.left(5 * d)
        t.width(1)

grass("green", 70, 10, 3,70, -400, -350, 10)

# =====================================================
# ПАРА 4 — СЕРДЕЧКО
# =====================================================

def heart (HEART_COLOR, CIRCLE_TURN, LINE_LENGTH,HEART_COORDS):
    t.penup()
    t.goto(HEART_COORDS, 0)
    t.pendown()
    t.color(HEART_COLOR)
    t.begin_fill()
    t.setheading(140)
    t.forward(LINE_LENGTH)
    t.circle(-CIRCLE_TURN, 200)
    t.setheading(60)
    t.circle(-CIRCLE_TURN, 200)
    t.forward(LINE_LENGTH)
    t.end_fill()

heart("red", 35, 62, -250)
heart("red", 35, 62, 250)

# НАДПИСЬ
def main_text(TEXT_COLOR, TEXT_COORDS, TEXT_FONT_SIZE, SUB_TEXT):
    t.penup()
    t.goto(0, TEXT_COORDS)
    t.pendown()
    t.color(TEXT_COLOR)
    t.write( SUB_TEXT, align="center", font=("Arial", TEXT_FONT_SIZE, "bold"))

main_text("purple", 0, 36,"С 8 Марта!")
main_text("deeppink", 50, 20,"Дорогие женщины!")
main_text("blue", -25, 14,"Пусть каждый день будет ярким!")

turtle.done()

