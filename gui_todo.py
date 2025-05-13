import tkinter as tk
from tkinter import messagebox

# List to store tasks
tasks = []

def add_task():
    description = task_entry.get()
    if description != "":
        task = {'description': description, 'status': 'incomplete'}
        tasks.append(task)
        update_task_list()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error ⚠️", "Please enter a task description.")

def delete_task():
    try:
        task_index = int(task_listbox.curselection()[0])
        task = tasks.pop(task_index)
        update_task_list()
        messagebox.showinfo("Task Deleted 🗑️", f"Task '{task['description']}' deleted! 🗑️")
    except IndexError:
        messagebox.showwarning("Selection Error ⚠️", "Please select a task to delete.")

def complete_task():
    try:
        task_index = int(task_listbox.curselection()[0])
        tasks[task_index]['status'] = 'complete'
        update_task_list()
        messagebox.showinfo("Task Complete ✅", f"Task '{tasks[task_index]['description']}' marked as complete! ✅")
    except IndexError:
        messagebox.showwarning("Selection Error ⚠️", "Please select a task to mark as complete.")

def update_task_list():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        # Add emojis based on task status
        status_emoji = "✅" if task['status'] == 'complete' else "❌"
        task_listbox.insert(tk.END, f"{task['description']} {status_emoji}")

# Create the main window
root = tk.Tk()
root.title("To-Do List Application")

# Create GUI elements
task_label = tk.Label(root, text="Enter Task:")
task_label.pack()

task_entry = tk.Entry(root, width=40)
task_entry.pack()

add_button = tk.Button(root, text="Add Task ✏️", command=add_task)
add_button.pack()

task_listbox = tk.Listbox(root, width=50, height=10)
task_listbox.pack()

complete_button = tk.Button(root, text="Mark Complete ✅", command=complete_task)
complete_button.pack()

delete_button = tk.Button(root, text="Delete Task 🗑️", command=delete_task)
delete_button.pack()

# Run the GUI application
root.mainloop()
