# views/task_details_view.py
import tkinter as tk
from tkinter import simpledialog
from todoapp.controllers.task_controller import TaskController

class TaskDetailsView(tk.Frame):
    def __init__(self, master, task):
        try:
            super().__init__(master)
            self.task = task

            self.label = tk.Label(self, text=f"Task Details: {task.title}", font=("Helvetica", 16, "bold"))
            self.label.pack(pady=10)

            # Display task details, due date, notes, etc.
            self.due_date_label = tk.Label(self, text=f"Due Date: {task.due_date}")
            self.due_date_label.pack(pady=5)

            self.notes_label = tk.Label(self, text=f"Notes: {task.notes}")
            self.notes_label.pack(pady=5)

            # Add a button to add a subtask
            self.new_subtask_button = tk.Button(self, text="Add Subtask", command=self.add_subtask)
            self.new_subtask_button.pack(pady=10)

            # Display subtasks
            self.subtasks_frame = tk.Frame(self)
            self.subtasks_frame.pack(fill=tk.BOTH, expand=True)

            self.refresh_subtasks()
        except Exception as e:
            print(f"Error initializing TaskDetailsView: {e}")
            # You might want to log the error or raise an exception if needed
            raise e

    def add_subtask(self):
        try:
            subtask = tk.simpledialog.askstring("New Subtask", "Enter the title for the new subtask:")
            if subtask:
                TaskController.add_subtask(self.task, subtask)
                self.refresh_subtasks()
        except Exception as e:
            print(f"Error adding subtask: {e}")
            # You might want to log the error or raise an exception if needed
            raise e

    def refresh_subtasks(self):
        try:
            # Refresh the displayed subtasks
            for widget in self.subtasks_frame.winfo_children():
                widget.destroy()

            for subtask in self.task.subtasks:
                subtask_label = tk.Label(self.subtasks_frame, text=f"Subtask: {subtask}")
                subtask_label.pack(pady=5)
        except Exception as e:
            print(f"Error refreshing subtasks: {e}")
            # You might want to log the error or raise an exception if needed
            raise e
