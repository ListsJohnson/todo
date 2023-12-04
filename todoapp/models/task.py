# models/task.py
class Task:
    def __init__(self, title, due_date=None, notes=None, subtasks=None):
        if not title:
            raise ValueError("Task title cannot be empty.")
        
        self.title = title
        self.due_date = due_date
        self.notes = notes or ""
        self.subtasks = subtasks or []

    def add_subtask(self, subtask):
        if not subtask:
            raise ValueError("Subtask cannot be empty.")
        
        self.subtasks.append(subtask)

    def __str__(self):
        return f"Task: {self.title}, Due Date: {self.due_date or 'N/A'}, Notes: {self.notes or 'N/A'}, Subtasks: {self.subtasks}"
