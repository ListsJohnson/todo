# views/task_list_details_view.py
import tkinter as tk
from tkinter import simpledialog
from todo.controllers.task_controller import TaskController

class TaskListDetailsView(tk.Frame):
    def __init__(self, master, task_list):
        try:
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
        except Exception as e:
            print(f"Error initializing TaskListDetailsView: {e}")
            # You might want to log the error or handle it in a way that makes sense for your application

    def create_new_task(self):
        try:
            title = tk.simpledialog.askstring("New Task", "Enter the title for the new task:")
            if title:
                task = TaskController.create_task(title)
                self.task_list.add_task(task)
                self.refresh_task_list()
        except Exception as e:
            print(f"Error creating new task: {e}")
            # You might want to log the error or handle it in a way that makes sense for your application

    def refresh_task_list(self):
        try:
            # Refresh the displayed task list
            for widget in self.task_list_frame.winfo_children():
                widget.destroy()

            for task in self.task_list.tasks:
                task_label = tk.Label(self.task_list_frame, text=task.title, cursor="hand2", font=("Helvetica", 12, "bold"))
                task_label.pack(pady=5)
                task_label.bind("<Button-1>", lambda event, t=task: self.show_task_details(t))
        except Exception as e:
            print(f"Error refreshing task list: {e}")
            # You might want to log the error or handle it in a way that makes sense for your application

    def show_task_details(self, task):
        try:
            # TODO: Implement logic to show the details view for the selected task
            pass
        except Exception as e:
            print(f"Error showing task details: {e}")
            # You might want to log the error or handle it in a way that makes sense for your application
