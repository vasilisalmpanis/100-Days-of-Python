from tkinter import*
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def resettimer():
    global reps
    window.after_cancel(timer)
    label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    checkmark.config(text="")
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def starttimer():
    global reps
    reps += 1
    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN*60)
        label.config(text="Long Break", font=(FONT_NAME, 40, "bold"), bg=YELLOW, fg=RED)
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN*60)
        label.config(text="Break", font=(FONT_NAME, 40, "bold"), bg=YELLOW, fg=PINK)
    else:
        count_down(WORK_MIN*60)
        label.config(text="Work", font=(FONT_NAME, 40, "bold"), bg=YELLOW, fg=GREEN)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    a =math.floor(count/60)
    if a<10:
        a = f"0{a}"
    b = count%60
    if b<10:
        b = f"0{b}"
    canvas.itemconfig(timer_text, text=f"{a}:{b}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        starttimer()
        marks = ""
        for i in range(math.floor(reps/2)):
            marks+= "✓"
            checkmark.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Count-Down")
window.config(padx=100, pady=50 ,bg=YELLOW)

label = Label(text="Timer", font=(FONT_NAME, 40, "bold"), bg=YELLOW, fg=GREEN)
label.grid(row=1, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
pomo = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=pomo)
timer_text = canvas.create_text(100, 135, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=2, column=1)

resetb = Button(text="Reset", command=resettimer, highlightthickness=0)
resetb.config()
resetb.grid(row=3, column=2)

startb = Button(text="Start", command=starttimer, highlightthickness=0)
startb.grid(row=3, column=0)

checkmark = Label(bg=YELLOW)
checkmark.config(pady=10)
checkmark.grid(row=3, column=1)



window.mainloop()
