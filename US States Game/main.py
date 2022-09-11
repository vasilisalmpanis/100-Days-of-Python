import turtle
import pandas
from turtle import Screen
data = pandas.read_csv("50_states.csv")
education = data.state.to_list()
screen = Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
game = True
all_states = data.state.to_list()
guessed_states = []
while len(guessed_states) < 50:
    guess = screen.textinput(title=f" {len(guessed_states)}/50 Guess the state", prompt="What is the next state?")
    if guess == "exit":
        for i in guessed_states:
            if i in all_states:
                education.remove(i)
        df = pandas.DataFrame(education)
        df.to_csv("to_learn.csv")
        break
    if guess.title() in all_states:
        statedata = data[data["state"] == guess.title()]
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(statedata["x"]), int(statedata["y"]))
        t.write(guess.title())
        guessed_states.append(guess.title())

screen.mainloop()