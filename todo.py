import tkinter as tk
from tkinter import messagebox

#functions for buttons

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def remove_task():
    selected_task = listbox.curselection()
    if selected_task:
        listbox.delete(selected_task)

def clear_list():
    listbox.delete(0, tk.END)

#creation of window and buttons

window = tk.Tk()
window.title("To-Do List")

entry = tk.Entry(window)
entry.pack(pady=10)

label=tk.Label(window,text="Todo List for Codsoft", fg="red")
label.pack(pady=20)

add_button = tk.Button(window, text="Add Task", command=add_task, bg="Blue",fg="white")
add_button.pack()

remove_button = tk.Button(window, text="Remove Task", command=remove_task,bg="Blue",fg="white")
remove_button.pack()

clear_button = tk.Button(window, text="Clear List", command=clear_list,bg="Blue",fg="white")
clear_button.pack()

listbox = tk.Listbox(window)
listbox.pack()

#starting of the main loop 
window.mainloop()
