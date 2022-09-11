from turtle import Screen
from paddle import Paddle
from score import Scoreboard
from ball import Ball
import time

my = Screen()
my.bgcolor("black")
my.setup(height=600, width=800)
my.title("Pong")
my.tracer(0)
paddle1 = Paddle(350)
paddle2 = Paddle(-350)
my.listen()
baller = Ball()
my.onkey(key="w", fun=paddle1.go_up)
my.onkey(key="s", fun=paddle1.go_down)
my.onkey(key="Up", fun=paddle2.go_up)
my.onkey(key="Down", fun=paddle2.go_down)
scores = Scoreboard()
game_on = True
while game_on:
    time.sleep(0.1)
    my.update()
    baller.move()
    if baller.ycor()>280 or baller.ycor()<-280:
        baller.bounce_y()

    if baller.distance(paddle1)<40 and baller.xcor()>330:
        baller.bounce_x()
    if baller.distance(paddle2)<40 and baller.xcor()<-330:
        baller.bounce_x()
    if baller.xcor() > 370:
        baller.reset_pos()
        scores.add1()
    if baller.xcor() < -370:
        baller.reset_pos()
        scores.add2()
my.exitonclick()