# views/my_day_view.py
import tkinter as tk
from tkinter import simpledialog
from todoapp.controllers.task_controller import TaskController

class MyDayView(tk.Frame):
    def __init__(self, master):
        try:
            super().__init__(master)

            self.label = tk.Label(self, text="My Day", font=("Helvetica", 16, "bold"))
            self.label.pack(pady=10)

            # Display tasks designated for the current day
            self.my_day_frame = tk.Frame(self)
            self.my_day_frame.pack(fill=tk.BOTH, expand=True)

            # Add a button to add a new task for the day
            self.new_task_button = tk.Button(self, text="Add Task for Today", command=self.add_task_to_day)
            self.new_task_button.pack(pady=10)
        except Exception as e:
            print(f"Error initializing MyDayView: {e}")
            # You might want to log the error or raise an exception if needed
            raise e

    def add_task_to_day(self):
        try:
            title = tk.simpledialog.askstring("New Task", "Enter the title for the new task:")
            if title:
                task = TaskController.create_task(title)
                # TODO: Implement logic to add the task to tasks designated for today
                self.refresh_my_day()
        except Exception as e:
            print(f"Error adding task to day: {e}")
            # You might want to log the error or raise an exception if needed
            raise e

    def refresh_my_day(self):
        try:
            # TODO: Implement logic to refresh the displayed tasks designated for the day
            pass
        except Exception as e:
            print(f"Error refreshing My Day: {e}")
            # You might want to log the error or raise an exception if needed
            raise e
