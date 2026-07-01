import turtle

# --- Настройки экрана ---
t = turtle.Turtle()
t.speed(1)
t.hideturtle()
screen = turtle.Screen()
screen.bgcolor("lightblue")
screen.setup(width=800, height=700)

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

main_text("purple", 20, 36,"С 8 Марта!")
main_text("deeppink", -10, 20,"Дорогие женщины!")
main_text("blue", -35, 14,"Пусть каждый день будет ярким!")

turtle.done()