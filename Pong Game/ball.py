from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("circle")
        self.xnew = random.randint(5,10)
        self.ynew = random.randint(5,10)

    def move(self):
        newx = self.xcor() + self.xnew
        newy = self.ycor() + self.ynew
        self.goto(newx, newy)

    def bounce_y(self):
        self.ynew *= -1


    def bounce_x(self):
        self.xnew *= -1


    def reset_pos(self):
        self.goto(0, 0)
        self.bounce_x()