# import tkinter
from tkinter import *
from app import App


# basic setting

app = App(500, 500, "Leo Chiu")

window = Tk()

window.title(app.title)
window.geometry(str(app.height) + "x" + str(app.width))


# function


def showMessage():
    lab["text"] = "Hello, World!"
    lab["bg"] = "orange"


# content
# label
lab = Label(
    window,
    font="MicrosoftJhengHei 20 bold"
)

lab1 = Label(
    window,
    text="Sentence A",
    bg="lightblue",
    font="MicrosoftJhengHei 10 bold",
)

lab2 = Label(
    window,
    bg="lightgreen",
    text="Sentence B",
    font="MicrosoftJhengHei 10 bold"

)

lab3 = Label(
    window,
    bg="orange",
    text="Sentence C",
    font="MicrosoftJhengHei 10 bold"

)


# button
btn1 = Button(
    window,
    text="Click me !",
    bg="lightblue",
    relief="raised",
    font="MicrosoftJhengHei 15 bold",
    width=10,
    command=showMessage
)

# final pack

# lab.pack(side=TOP, pady=50)
lab.pack(side=TOP, pady=100)
btn1.pack(side=BOTTOM, pady=100)

# main loop

window.mainloop()
