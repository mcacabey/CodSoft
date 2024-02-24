import tkinter as tk
from math import sqrt

# Create a window
window = tk.Tk()
window.title("Calculator")
window.configure(bg="#f92cb5")

# Define font for the calculator
font = ("Gill Sans MT", 10)

def lab(val):
    tk.Label(window, text=str(val), width=5, borderwidth=3).grid(row=0, column=4, pady=8, columnspan=2)

lab(": )")

display = tk.Entry(window, font=("default, 11"), insertontime=0, bd=5, width=21, borderwidth=10, foreground="#ff0000", highlightthickness=5, highlightcolor="#f5d0d0", highlightbackground="#f5d0d0")
display.grid(row=0, rowspan=2, column=0, columnspan=4, padx=5, pady=5)
display.bind("<Key>", lambda display: "break")

def view(val):
    tk.Label(window, borderwidth=3, relief="sunken", text=str(val), width=34, bg="#f5d0d0", fg="#000000").grid(row=2, column=0, columnspan=5, pady=5)

view("Calculations here")

def button_click(number):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(tk.END, current + str(number))

def button_clear():
    display.delete(0, tk.END)

def button_equal():
    try:
        expression = display.get()
        result = eval(expression)
        display.delete(0, tk.END)
        display.insert(tk.END, result)
    except:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")

def button_sqrt():
    try:
        expression = display.get()
        result = sqrt(eval(expression))
        display.delete(0, tk.END)
        display.insert(tk.END, result)
    except:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")

def button_power():
    try:
        expression = display.get()
        result = eval(expression) ** 2  # Change this line to compute the power as needed
        display.delete(0, tk.END)
        display.insert(tk.END, result)
    except:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")

# Define buttons for numbers 0-9
buttons = []
for i in range(10):
    button = tk.Button(window, text=str(i), padx=20, pady=15,  command=lambda i=i: button_click(i))
    buttons.append(button)

button1 = tk.Button(window, bg="#bbeef1",  text="1", padx=20, pady=15, command=lambda: button_click("1"))
button1.grid(row=6, column=0)

button2 = tk.Button(window, bg="#bbeef1", text="2", padx=20, pady=15, command=lambda: button_click("2"))
button2.grid(row=6, column=1)

button3 = tk.Button(window, bg="#bbeef1", text="3", padx=20, pady=15, command=lambda: button_click("3"))
button3.grid(row=6, column=2)

button4 = tk.Button(window, bg="#bbeef1", text="4", padx=20, pady=15, command=lambda: button_click("4"))
button4.grid(row=5, column=0)

button5 = tk.Button(window, bg="#bbeef1", text="5", padx=20, pady=15, command=lambda: button_click("5"))
button5.grid(row=5, column=1)

button6 = tk.Button(window, bg="#bbeef1", text="6", padx=20, pady=15, command=lambda: button_click("6"))
button6.grid(row=5, column=2)

button7 = tk.Button(window, bg="#bbeef1", text="7", padx=20, pady=15, command=lambda: button_click("7"))
button7.grid(row=4, column=0)

button8 = tk.Button(window, bg="#bbeef1", text="8", padx=20, pady=15, command=lambda: button_click("8"))
button8.grid(row=4, column=1)

button9 = tk.Button(window, bg="#bbeef1",  text="9", padx=20, pady=15, command=lambda: button_click("9"))
button9.grid(row=4, column=2)


subtract_button = tk.Button(window, bg="#5ebec4", fg="#fdf5df", text="-", padx=18, pady=15, command=lambda: button_click("-"))
subtract_button.grid(row=5, column=3)

multiply_button = tk.Button(window, bg="#5ebec4", fg="#fdf5df", text="x", padx=17, pady=15, command=lambda: button_click("*"))
multiply_button.grid(row=4, column=3)

divide_button = tk.Button(window, bg="#5ebec4", fg="#fdf5df", text="/", padx=19, pady=8, command=lambda: button_click("/"))
divide_button.grid(row=3, column=3)

button_clear = tk.Button(window, bg="#5ebec4", fg="#fdf5df", text="C", padx=16, pady=8, command=button_clear)
button_clear.grid(row=3, column=0)

add_button = tk.Button(window, bg="#5ebec4", fg="#fdf5df", text="+", padx=17, pady=42, command=lambda: button_click("+"))
add_button.grid(row=6, column=3, rowspan=2)

equal_button = tk.Button(window, bg="#5ebec4", fg="#fdf5df", text="=", padx=18, pady=115, command=button_equal)
equal_button.grid(row=3, column=4, rowspan=5)

dot_button = tk.Button(window, bg="#5ebec4", fg="#fdf5df", text=".", padx=20, pady=15, command=lambda: button_click("."))
dot_button.grid(row=7, column=2)

button0 = tk.Button(window, bg="#5ebec4", fg="#fdf5df", text="0", padx=50, pady=15, command=lambda: button_click("0"))
button0.grid(row=7, column=0, columnspan=2)

sqrt_button = tk.Button(window, bg="#5ebec4", fg="#fdf5df", text="\u221A", padx=19, pady=8, command=button_sqrt)
sqrt_button.grid(row=3, column=1)

button_power = tk.Button(window, bg="#5ebec4", fg="#fdf5df", text="^2", padx=16, pady=8, command=button_power)
button_power.grid(row=3, column=2)

window.resizable(False, False)

# Run the main event loop
window.mainloop()
