# views/task_list_details_view.py
import tkinter as tk
from todo.controllers.task_controller import TaskController

class TaskListDetailsView(tk.Frame):
    def __init__(self, master, task_list):
        super().__init__(master)
        self.task_list = task_list

        self.label = tk.Label(self, text=f"Task List: {task_list.title}", font=("Helvetica", 16, "bold"))
        self.label.pack(pady=10)

        # Display tasks in the task list
        self.task_list_frame = tk.Frame(self)
        self.task_list_frame.pack(fill=tk.BOTH, expand=True)

        for task in task_list.tasks:
            task_label = tk.Label(self.task_list_frame, text=task.title, cursor="hand2", font=("Helvetica", 12, "bold"))
            task_label.pack(pady=5)
            task_label.bind("<Button-1>", lambda event, t=task: self.show_task_details(t))

        # Add a button to add a new task
        self.new_task_button = tk.Button(self, text="New Task", command=self.create_new_task)
        self.new_task_button.pack(pady=10)

    def create_new_task(self):
        title = tk.simpledialog.askstring("New Task", "Enter the title for the new task:")
        if title:
            task = TaskController.create_task(title)
            self.task_list.add_task(task)
            self.refresh_task_list()

    def refresh_task_list(self):
        # Refresh the displayed task list
        for widget in self.task_list_frame.winfo_children():
            widget.destroy()

        for task in self.task_list.tasks:
            task_label = tk.Label(self.task_list_frame, text=task.title, cursor="hand2", font=("Helvetica", 12, "bold"))
            task_label.pack(pady=5)
            task_label.bind("<Button-1>", lambda event, t=task: self.show_task_details(t))

    def show_task_details(self, task):
        # TODO: Implement logic to show the details view for the selected task
        pass
