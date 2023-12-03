# views/task_lists_view.py
import tkinter as tk
from todo.controllers.task_list_controller import TaskListController
from todo.views.task_list_details_view import TaskListDetailsView

class TaskListsView(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.label = tk.Label(self, text="Task Lists", font=("Helvetica", 16, "bold"))
        self.label.pack(pady=10)

        # Display the task lists
        self.task_lists_frame = tk.Frame(self)
        self.task_lists_frame.pack(fill=tk.BOTH, expand=True)

        # Add a button to create a new task list
        self.new_list_button = tk.Button(self, text="New Task List", command=self.create_new_list)
        self.new_list_button.pack(pady=10)

    def create_new_list(self):
        title = tk.simpledialog.askstring("New Task List", "Enter the title for the new task list:")
        if title:
            task_list = TaskListController.create_task_list(title)
            TaskListDetailsView(self.master, task_list).pack(fill=tk.BOTH, expand=True)
