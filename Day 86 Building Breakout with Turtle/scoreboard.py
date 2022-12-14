from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-5, 210)
        self.write(self.r_score, align="center", font=("Courier", 60, "normal"))

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()