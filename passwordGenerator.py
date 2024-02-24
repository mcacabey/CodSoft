
from tkinter import *
import random, string

window = Tk()
window.title("Password Generator")
window.configure(bg = "#fdf5df")



# intro text
my_font = ("Gill Sans", 15)
title = StringVar()
label = Label(window,fg="#5ebec4" ,textvariable=title, anchor=N, pady=10,font=my_font).pack()
title.set("Password strength:")

# choice part


def sel():
    selection = choice.get()

choice = IntVar()
R1 = Radiobutton(window, text="BASIC",font ="Impact Regular",fg="#f9bec4", variable=choice, value=1, command=sel).pack(anchor=CENTER)
R2 = Radiobutton(window, text="MEDIUM",font ="Impact Regular",fg="#f9bec4", variable=choice, value=2, command=sel).pack(anchor=CENTER)
R3 = Radiobutton(window, text="EXTRA", font ="Impact Regulars",fg="#f9bec4",variable=choice, value=3, command=sel).pack(anchor=CENTER)
labelchoice = Label(window)
labelchoice.pack()

# pass lenght information
lenlabel = StringVar()
lenlabel.set("Password length:")
lentitle = Label(window,font="my_font", fg="#5ebec4", textvariable=lenlabel).pack()

# pass lenght number
val = IntVar()
spinlenght = Spinbox(window, from_=8, to_=24, textvariable=val, width=13).pack()

# passprint

def callback():
    lsum.config(text=passgen())


# clickable button
button_font = ("Segoe Print", 10)
passgenButton = Button(window,bg="#5ebec4" ,fg="#fdf5d5",font =button_font,text="Generate Password", relief=RIDGE, bd=5, height=2, command=callback, pady=3)
passgenButton.pack()
password = str(callback)

# password result message
lsum = Label(window, text="")
lsum.pack(side=BOTTOM)

# function
lownum = string.ascii_uppercase + string.ascii_lowercase + string.digits
lowupp = string.ascii_uppercase + string.ascii_lowercase
symbols = """`~!@#$%^&*()_-+={}[]\|:;"'<>,.?/"""
everything = lowupp + lownum + symbols


def passgen():
    if choice.get() == 1:
        return "".join(random.sample(lowupp, val.get()))
    elif choice.get() == 2:
        return "".join(random.sample(lownum, val.get()))
    elif choice.get() == 3:
        return "".join(random.sample(everything, val.get()))


window.mainloop()