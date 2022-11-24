import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageDraw

# We initiate the main window together with the labels and buttons #
window = tk.Tk()
window.title('Image Watermark')
img1 = None
window.geometry("500x800")
my_font1 = ('times', 18, 'bold')
l1 = tk.Label(window, text='Add Photo', width=30, font=my_font1)
l1.grid(column=1, row=1)
btn1 = tk.Button(window, text='open image', command=lambda: open_img()).grid(row=2, column=1)
textBox = tk.Text(window, height=2, width=10)
textBox.grid(row=3, column=1)
Button_2 = tk.Button(window, height=1, width=10, text="Add Text", command=lambda: retrieve_input())
Button_2.grid(row=3, column=2)
Button_3 = tk.Button(window, height=1, width=10, text="Add Logo", command=lambda: add_logo()).grid(row=4, column=2)


# Adds the photo we want as watermark and saves it in our current folder #
def add_logo():
    x = openfilename()
    image = Image.open(x)
    size = (100, 100)
    crop_image = image.copy()
    crop_image.thumbnail(size)

    # add watermark
    copied_image = img1.copy()
    copied_image.paste(crop_image, (10, 10))
    copied_image.save("watermark.jpg")


# Retrieves and adds the text we want as watermark and saves it in our current folder #
def retrieve_input():
    input_value = textBox.get("1.0", "end-1c")
    watermark_image = img1
    draw = ImageDraw.Draw(img1)
    draw.text((0, 0), input_value,
              (0, 0, 0))
    watermark_image.save("geeks.jpg")


# Displays the image we want to watermark #
def open_img():
    global img1
    x = openfilename()
    img1 = Image.open(x)
    img2 = img1.copy()
    img2 = img2.resize((400, 400), Image.ANTIALIAS)
    img2 = ImageTk.PhotoImage(img2)
    panel = tk.Label(window, image=img2)
    panel.image = img2
    panel.grid(row=5, column=1)


# open file dialog box to select image #
def openfilename():
    filename = filedialog.askopenfilename(title='"pen')
    return filename


window.mainloop()
