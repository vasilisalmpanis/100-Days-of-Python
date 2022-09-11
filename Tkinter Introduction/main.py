import tkinter


window = tkinter.Tk()
window.wm_title("Mile to Kilometer Converter")
window.minsize(width=100, height=100)
window.config(padx=25, pady=25)

#label
mylabel = tkinter.Label(text="Miles", font=("Ariel", 15, "normal"))
mylabel.grid(row=0, column=3)


mylabel1 = tkinter.Label(text="is equal to", font=("Ariel", 15, "normal"))
mylabel1.grid(row=1, column=1)


mylabel2 = tkinter.Label(text="Km", font=("Ariel", 15, "normal"))
mylabel2.grid(row=1, column=3)


mylabel3= tkinter.Label(text="0", font=("Ariel", 15, "normal"))
mylabel3.grid(row=1, column=2)


def convert():
    con = float(input.get()) * 1.60934

    return round(con, 2)


def button_click():
    mylabel3["text"] = convert()

mybutton = tkinter.Button(text="Calculate", command=button_click)
mybutton.grid(column=2, row=2)


input = tkinter.Entry(width= 5)
input.grid(column=2, row=0)


window.mainloop()

