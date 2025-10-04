# Import required modules
import turtle
import time
import random

# Game variables
delay = 0.1
score = 0
high_score = 0

# Creating window
wn = turtle.Screen()
wn.title("Snake Game by Badr Ghanjaoui")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.cv._rootwindow.resizable(False, False)
wn.tracer(0)

# Snake head
head = turtle.Turtle()
head.shape("square")
head.color("white")
head.penup()
head.speed(0)
head.goto(0, 0)
head.direction = "Stop"

# Normal food
food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.penup()
food.speed(0)
food.goto(0, 100)

# Special food (appears every 10 seconds, bigger, worth 20 points)
special_food = turtle.Turtle()
special_food.shape("circle")
special_food.color("gold")
special_food.shapesize(stretch_wid=1.5, stretch_len=1.5)
special_food.penup()
special_food.speed(0)
special_food.goto(1000, 1000)  # hidden initially

# Timer to track special food appearance
last_special_food_time = time.time()

# Pen for score
pen = turtle.Turtle()
pen.shape("square")
pen.color("white")
pen.penup()
pen.speed(0)
pen.goto(0, 260)
pen.hideturtle()
pen.write(f"Score: {score}                                        High Score: {high_score}", align="center", font=("Arial", 18, "bold"))

# Functions for movement
def goup():
    if head.direction != "down":
        head.direction = "up"

def godown():
    if head.direction != "up":
        head.direction = "down"

def goleft():
    if head.direction != "right":
        head.direction = "left"

def goright():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# Key bindings
wn.listen()
wn.onkeypress(goup, "Up")
wn.onkeypress(godown, "Down")
wn.onkeypress(goleft, "Left")
wn.onkeypress(goright, "Right")

# Snake body segments
segments = []

# Main game loop
while True:
    wn.update()

    # Check if 10 seconds passed and special food is hidden
    current_time = time.time()
    if current_time - last_special_food_time > 10 and special_food.xcor() > 900:
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        special_food.goto(x, y)
        last_special_food_time = current_time

    # Collision with borders
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "Stop"
        food.color("red")
        food.shape("circle")
        special_food.goto(1000, 1000)
        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()
        score = 0
        delay = 0.1
        pen.clear()
        pen.write(f"Score: {score}                                        High Score: {high_score}", align="center", font=("Arial", 18, "bold"))

    # Collision with normal food
    if head.distance(food) < 20:
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        food.goto(x, y)

        # Add segment
        new_segment = turtle.Turtle()
        new_segment.shape("square")
        new_segment.color("blue")
        new_segment.speed(0)
        new_segment.penup()
        segments.append(new_segment)

        delay -= 0.001
        score += 10
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write(f"Score: {score}                                        High Score: {high_score}", align="center", font=("Arial", 18, "bold"))

    # Collision with special food
    if head.distance(special_food) < 25:  # bigger than normal food
        special_food.goto(1000, 1000)  # hide after eaten

        new_segment = turtle.Turtle()
        new_segment.shape("square")
        new_segment.color("blue")
        new_segment.speed(0)
        new_segment.penup()
        segments.append(new_segment)

        delay -= 0.002
        score += 20  # special food gives 20 points
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write(f"Score: {score}                                        High Score: {high_score}", align="center", font=("Arial", 18, "bold"))

    # Move snake body
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    # Collision with body
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "Stop"
            food.color("red")
            food.shape("circle")
            special_food.goto(1000, 1000)
            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()
            score = 0
            delay = 0.1
            pen.clear()
            pen.write(f"Score: {score}                                        High Score: {high_score}", align="center", font=("Arial", 18, "bold"))

    time.sleep(delay)
