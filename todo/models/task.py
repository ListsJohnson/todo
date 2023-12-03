# models/task.py
class Task:
    def __init__(self, title, due_date=None, notes=None, subtasks=None):
        self.title = title
        self.due_date = due_date
        self.notes = notes or ""
        self.subtasks = subtasks or []

    def add_subtask(self, subtask):
        self.subtasks.append(subtask)

    def __str__(self):
        return f"Task: {self.title}, Due Date: {self.due_date}, Notes: {self.notes}, Subtasks: {self.subtasks}"
