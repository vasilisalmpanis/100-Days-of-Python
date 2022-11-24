from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from brick import Brick
import time
import random

screen = Screen()
screen.bgcolor("black")
screen.setup(width=850, height=600)
screen.title("Breakout")
screen.tracer(0)
colors = ["green", "red", "blue", "yellow", "pink", "purple"]
bricks = [[0 for i in range(9)] for j in range(3)]
check = [[1 for i in range(9)] for j in range(3)]

r_paddle = Paddle((0, -250))
ball = Ball()
scoreboard = Scoreboard()
x = -365
y = 210
for j in range(3):
    color = random.choice(colors)
    for i in range(9):
        bricks[j][i] = (Brick((x,y), color))
        x = x + 90
    y = y - 27
    x = -365


screen.listen()
screen.onkey(lambda :[r_paddle.go_left()], "Left")
screen.onkey(lambda :[r_paddle.go_right()], "Right")
hit_brick = False
y = 3
x = 9
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.01)
    ball.move()

    #Detect collision with wall
    if ball.ycor() > 280:
        ball.bounce_y()
        hit_brick = False

    if ball.ycor() < -270:
        ball.reset_position()

    if ball.xcor() > 400 or ball.xcor() < -400:
        ball.bounce_x()
        hit_brick = False

    #Detect collision with paddle
    if ball.distance(r_paddle) < 60:
        ball.bounce_y()
        hit_brick = False


    for j in range(y):
        for i in range(x):
            if ball.distance(bricks[j][i]) < 40 and hit_brick==False:
                ball.bounce_y()
                hit_brick = True
                bricks[j][i].disappear()
                scoreboard.r_point()
                if scoreboard.r_score == 27:
                    screen.bye()



    #Detect L paddle misses:
    if ball.ycor() < -250:
        ball.reset_position()
        hit_brick = False

screen.exitonclick()