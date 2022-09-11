from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position, 0)
        self.speed("fastest")

    def go_up(self):
        self.newy = self.ycor() + 20
        self.goto(self.xcor(), self.newy)

    def go_down(self):
        self.newy = self.ycor() - 20
        self.goto(self.xcor(), self.newy)
