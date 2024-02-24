'''
A To-Do List application is a useful project that helps users manage
and organize their tasks efficiently. This project aims to create a
command-line or GUI-based application using Python, allowing

users to create, update, and track their to-do lists
'''
import tkinter as tk
from tkinter import messagebox
#from tkinter.font import Font



# Define font
my_font = ("Segoe Print", 15)

# Create the main window
window = tk.Tk()
window.title("My to do list")
window.configure(bg = "#fdf5df")

# Create frame
my_frame = tk.Frame(window)
my_frame.pack(pady=15)

# Create listbox
my_list = tk.Listbox(my_frame,
      font=my_font,
      width=20,
      height=5,
      bg="SystemButtonFace",
      bd=0,
      fg="#f92cb5",
      activestyle= "none",
      highlightthickness=0,
      selectbackground="#bbeef1"
      )
my_list.pack(side="left", fill="both")

#create a list
my_stuff =["Workout","Eat Breakfast","Bath","Read","Watch tv"]

#add to the list
for item in my_stuff:
    my_list.insert(tk.END,item)

# Create the scrollbar
scrollbar = tk.Scrollbar(my_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Add the scrollbar to the to-do list
my_list.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=my_list.yview)

# Create the task entry field
entry = tk.Entry(window, font=my_font)
entry.pack(pady=20)

# Function to add a new task to the to-do list
def add_task():
    task = entry.get()
    if task:
        my_list.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

# Function to delete a selected task from the to-do list
def delete_task():
    try:
        index = my_list.curselection()
        my_list.delete(index)
    except:
        messagebox.showwarning("Warning", "Please select a task to delete.")

# Function to update/edit the selected task
def update_task():
    try:
        index = my_list.curselection()
        updated_task = entry.get()
        if updated_task:
            my_list.delete(index)
            my_list.insert(index, updated_task)
            entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter an updated task.")
    except:
        messagebox.showwarning("Warning", "Please select a task to update.")

# Function to mark the selected task as done
def mark_as_done():
    try:
        index = my_list.curselection()
        task = my_list.get(index)
        updated_task = task + " (Done)"
        my_list.delete(index)
        my_list.insert(index, updated_task)
    except:
        messagebox.showwarning("Warning", "Please select a task to mark as done.")

#create button font and size
button_font = ("Segoe Print", 10)
# Create buttons to add, delete, update, and mark as done tasks
add_button = tk.Button(window, text="Add Task", command=add_task, bg= "#5ebec4",fg="#fdf5df", font=button_font)
add_button.pack(pady=10)
delete_button = tk.Button(window, text="Delete Task", command=delete_task, bg= "#5ebec4",fg="#fdf5df",font=button_font)
delete_button.pack(pady=10)
update_button = tk.Button(window, text="Update Task", command=update_task, bg= "#5ebec4",fg="#fdf5df", font=button_font)
update_button.pack(pady=10)
mark_done_button = tk.Button(window, text="Mark as Done", command=mark_as_done, bg= "#5ebec4",fg="#fdf5df", font=button_font)
mark_done_button.pack(pady=10)

# Start the GUI main loop
window.mainloop()

