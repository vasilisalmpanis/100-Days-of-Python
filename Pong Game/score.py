from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.goto(0,240)
        self.score1 = 0
        self.score2 = 0
        self.write(f"{self.score1} - {self.score2}", align="center", font=("Courier", 30, "normal"))
        self.hideturtle()


    def add1(self):
        self.score1 +=1
        self.clear()
        self.write(f"{self.score1} - {self.score2}", align="center", font=("Courier", 30, "normal"))



    def add2(self):
        self.score2 +=1
        self.clear()
        self.write(f"{self.score1} - {self.score2}", align="center", font=("Courier", 30, "normal"))