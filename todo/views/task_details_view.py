# views/task_details_view.py
import tkinter as tk
from todo.controllers.task_controller import TaskController

class TaskDetailsView(tk.Frame):
    def __init__(self, master, task):
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

        for subtask in task.subtasks:
            subtask_label = tk.Label(self.subtasks_frame, text=f"Subtask: {subtask}")
            subtask_label.pack(pady=5)

    def add_subtask(self):
        subtask = tk.simpledialog.askstring("New Subtask", "Enter the title for the new subtask:")
        if subtask:
            TaskController.add_subtask(self.task, subtask)
            self.refresh_subtasks()

    def refresh_subtasks(self):
        # Refresh the displayed subtasks
        for widget in self.subtasks_frame.winfo_children():
            widget.destroy()

        for subtask in self.task.subtasks:
            subtask_label = tk.Label(self.subtasks_frame, text=f"Subtask: {subtask}")
            subtask_label.pack(pady=5)
