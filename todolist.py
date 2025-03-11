import tkinter as tk
from tkinter import messagebox

# Functionality for the To-Do List
class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("400x500")

        # Task list storage
        self.tasks = []

        # UI Components
        self.create_widgets()

    def create_widgets(self):
        # Label for the title
        title_label = tk.Label(self.root, text="To-Do List", font=("Arial", 20, "bold"))
        title_label.pack(pady=10)

        # Listbox to display tasks
        self.task_listbox = tk.Listbox(self.root, width=40, height=15, font=("Arial", 14))
        self.task_listbox.pack(pady=10)

        # Entry widget to add new tasks
        self.task_entry = tk.Entry(self.root, width=30, font=("Arial", 14))
        self.task_entry.pack(pady=10)

        # Buttons for adding, removing, and clearing tasks
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)

        add_button = tk.Button(button_frame, text="Add Task", command=self.add_task, width=12)
        add_button.grid(row=0, column=0, padx=5)

        remove_button = tk.Button(button_frame, text="Remove Task", command=self.remove_task, width=12)
        remove_button.grid(row=0, column=1, padx=5)

        clear_button = tk.Button(button_frame, text="Clear All", command=self.clear_tasks, width=12)
        clear_button.grid(row=0, column=2, padx=5)

    def add_task(self):
        # Get task from entry field
        task = self.task_entry.get()
        if task.strip() == "":
            messagebox.showwarning("Input Error", "Task cannot be empty!")
            return
        self.tasks.append(task)
        self.update_task_listbox()
        self.task_entry.delete(0, tk.END)  # Clear the entry field

    def remove_task(self):
        # Get selected task
        selected_task_index = self.task_listbox.curselection()
        if not selected_task_index:
            messagebox.showwarning("Selection Error", "No task selected!")
            return
        task_to_remove = selected_task_index[0]
        del self.tasks[task_to_remove]
        self.update_task_listbox()

    def clear_tasks(self):
        # Confirm clearing
        if messagebox.askyesno("Confirm Clear", "Are you sure you want to clear all tasks?"):
            self.tasks.clear()
            self.update_task_listbox()

    def update_task_listbox(self):
        # Update listbox with tasks
        self.task_listbox.delete(0, tk.END)  # Clear current listbox
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
