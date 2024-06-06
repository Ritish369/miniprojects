# Module for basic graphics
import turtle

# import os
import winsound

window = turtle.Screen()
window.title("Pong by Ritish")
window.bgcolor("black")
window.setup(width=800, height=600)

# Turns the animation on/off(on by dflt) but here stops the screen from updating.
# Allows to explicitly update manually otherwise just to speed up the game quite a bit.
window.tracer(0)

# Score tracking
score_1 = 0
score_2 = 0

# Paddle 1(Left side)
# This is a Turtle object
paddle_1 = turtle.Turtle()
# Speed of animation, not of the paddle moving on the screen
# Sets the speed to the max possible it can
paddle_1.speed(0)
paddle_1.shape("square")
paddle_1.color("white")
# By dflt, shape is 20 x 20 pixels
paddle_1.shapesize(stretch_wid=5, stretch_len=1)
# Because turtles draw a line as they move, but we don't want to see the
# line path of the paddle that's why used penup() fn
paddle_1.penup()
# Coordinates of the screen horizontally
paddle_1.goto(-350, 0)

# Paddle 2(Right side)
# Paddle 1
# This is a Turtle object
paddle_2 = turtle.Turtle()
# Speed of animation, not of the paddle moving on the screen
# Sets the speed to the max possible it can
paddle_2.speed(0)
paddle_2.shape("square")
paddle_2.color("white")
# By dflt, shape is 20 x 20 pixels
paddle_2.shapesize(stretch_wid=5, stretch_len=1)
# Because turtles draw a line as they move, but we don't want to see the
# line path of the paddle that's why used penup() fn
paddle_2.penup()
# Coordinates of the screen horizontally
paddle_2.goto(350, 0)

# Ball
# Paddle 1
# This is a Turtle object
ball = turtle.Turtle()
# Speed of animation, not of the paddle moving on the screen
# Sets the speed to the max possible it can
ball.speed(0)
ball.shape("square")
ball.color("white")
# Because turtles draw a line as they move, but we don't want to see the
# line path of the paddle that's why used penup() fn
ball.penup()
# Coordinates of the screen horizontally to start from(location)
ball.goto(0, 0)
# Separating the ball movement into two i.e., x-movement & y-movement
# Everytime the ball moves, it moves by 2 pixels
ball.dx = 0.2
ball.dy = -0.2

# Pen (for writing the scores)
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
# Don't want to see the pen but the text it writes
pen.hideturtle()
# Place to write
pen.goto(0, 260)
# What to write
pen.write("Player 1: 0  Player 2: 0", align="center", font=("Courier", 24, "normal"))


# Function for moving paddle 1 up
def paddle_1_up():
    # Getting the y coordinate of the paddle
    y = paddle_1.ycor()
    # 20 pixels
    y += 20
    paddle_1.sety(y)


# Function for moving paddle 1 down
def paddle_1_down():
    # Getting the y coordinate of the paddle
    y = paddle_1.ycor()
    # 20 pixels
    y -= 20
    paddle_1.sety(y)


# Function for moving paddle 2 up
def paddle_2_up():
    # Getting the y coordinate of the paddle
    y = paddle_2.ycor()
    # 20 pixels
    y += 20
    paddle_2.sety(y)


# Function for moving paddle 1 down
def paddle_2_down():
    # Getting the y coordinate of the paddle
    y = paddle_2.ycor()
    # 20 pixels
    y -= 20
    paddle_2.sety(y)


# Keyboard binding
# This fn tells the window to listen for the keyboard input
window.listen()
# Tells to call paddle_1_up fn when "w" key is pressed on board & similar for other fns
window.onkeypress(paddle_1_up, "w")
window.onkeypress(paddle_1_down, "s")
# For paddle 2(Using arrow keys)
window.onkeypress(paddle_2_up, "Up")
window.onkeypress(paddle_2_down, "Down")

# Main game loop
while True:
    # Updates the screen explicitly for each loop run which we didn't do
    # in tracer fn
    window.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking(What happens when the balls hits the borders ?)
    # At the border, bounce/reverse the direction of the ball(top & bottom)
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        # & so that no delay of stop at collision
        # afplay for MAC
        # aplay for Linux
        # os.system("aplay jump-play-14839.mp3&")
        # SND_ASYNC does the same thing as of &
        winsound.PlaySound("jump-play-14839.mp3", winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        # os.system("aplay jump-play-14839.mp3&")
        winsound.PlaySound("jump-play-14839.mp3", winsound.SND_ASYNC)

    # Left & right borders
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_1 += 1
        pen.clear()
        pen.write(
            f"Player 1: {score_1}  Player 2: {score_2}",
            align="center",
            font=("Courier", 24, "normal"),
        )

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_2 += 1
        pen.clear()
        pen.write(
            f"Player 1: {score_1}  Player 2: {score_2}",
            align="center",
            font=("Courier", 24, "normal"),
        )

    # Paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (
        ball.ycor() < paddle_2.ycor() + 40 and ball.ycor() > paddle_2.ycor() - 40
    ):
        ball.setx(340)
        ball.dx *= -1
        # os.system("aplay jump-play-14839.mp3&")
        winsound.PlaySound("jump-play-14839.mp3", winsound.SND_ASYNC)

    if (ball.xcor() < -340 and ball.xcor() > -350) and (
        ball.ycor() < paddle_1.ycor() + 40 and ball.ycor() > paddle_1.ycor() - 40
    ):
        ball.setx(-340)
        ball.dx *= -1
        # os.system("aplay jump-play-14839.mp3&")
        winsound.PlaySound("jump-play-14839.mp3", winsound.SND_ASYNC)
