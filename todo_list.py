"""Earlier in the older versions 
users were asked to download tkinter package 
now in the latest version no need to 
download tkinter as it is aldready in-built."""

# Import all the required packages
import tkinter as tk
from tkinter import messagebox

# Class to represent a single task
class Task:
    def __init__(self, description):
        self.description = description
        self.is_done = False

    # Mark the task as done
    def mark_as_done(self):
        self.is_done = True

    # Return a string representation of the task
    def __str__(self):
        status = "Done" if self.is_done else "Not Done"
        return f"[{status}] {self.description}"

# Class to manage the to-do list
class ToDoList:
    def __init__(self):
        self.tasks = []

    # Add a task to the list
    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)

    # Remove a task from the list by index
    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)

    # Update the description of a task
    def update_task(self, index, new_description):
        if 0 <= index < len(self.tasks):
            self.tasks[index].description = new_description

    # Mark a task as done by index
    def mark_task_as_done(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_as_done()

    # Return a list of string representations of all tasks
    def display_tasks(self):
        return [str(task) for task in self.tasks]

# Class to create the GUI for the to-do list application
class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")
        self.todo_list = ToDoList()

        self.task_var = tk.StringVar()

        # Create the main frame
        self.frame = tk.Frame(root)
        self.frame.pack(pady=10)

        # Entry for task description
        self.task_entry = tk.Entry(self.frame, textvariable=self.task_var, width=40)
        self.task_entry.grid(row=0, column=0, padx=10)

        # Button to add task
        self.add_btn = tk.Button(self.frame, text="Add Task", command=self.add_task)
        self.add_btn.grid(row=0, column=1)

        # Listbox to display tasks
        self.tasks_listbox = tk.Listbox(root, width=50, height=15)
        self.tasks_listbox.pack(pady=10)

        # Buttons for update, delete, and mark as done
        self.update_btn = tk.Button(root, text="Update Task", command=self.update_task)
        self.update_btn.pack(side=tk.LEFT, padx=10)

        self.delete_btn = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_btn.pack(side=tk.LEFT, padx=10)

        self.done_btn = tk.Button(root, text="Mark as Done", command=self.mark_task_as_done)
        self.done_btn.pack(side=tk.LEFT, padx=10)

        # Refresh the task list display
        self.refresh_task_list()

    # Add a task to the list
    def add_task(self):
        task_description = self.task_var.get()
        if task_description:
            self.todo_list.add_task(task_description)
            self.task_var.set("")
            self.refresh_task_list()
        else:
            messagebox.showwarning("Warning", "You must enter a task description")

    # Update the selected task
    def update_task(self):
        selected_task_index = self.tasks_listbox.curselection()
        if selected_task_index:
            new_description = self.task_var.get()
            if new_description:
                self.todo_list.update_task(selected_task_index[0], new_description)
                self.task_var.set("")
                self.refresh_task_list()
            else:
                messagebox.showwarning("Warning", "You must enter a new description")
        else:
            messagebox.showwarning("Warning", "You must select a task to update")

    # Delete the selected task
    def delete_task(self):
        selected_task_index = self.tasks_listbox.curselection()
        if selected_task_index:
            self.todo_list.remove_task(selected_task_index[0])
            self.refresh_task_list()
        else:
            messagebox.showwarning("Warning", "You must select a task to delete")

    # Mark the selected task as done
    def mark_task_as_done(self):
        selected_task_index = self.tasks_listbox.curselection()
        if selected_task_index:
            self.todo_list.mark_task_as_done(selected_task_index[0])
            self.refresh_task_list()
        else:
            messagebox.showwarning("Warning", "You must select a task to mark as done")

    # Refresh the task list display in the listbox
    def refresh_task_list(self):
        self.tasks_listbox.delete(0, tk.END)
        for task in self.todo_list.display_tasks():
            self.tasks_listbox.insert(tk.END, task)

# Main function to start the application
if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
