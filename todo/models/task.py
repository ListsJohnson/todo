# models/task.py
class Task:
    def __init__(self, title, due_date=None, notes=None, subtasks=None):
        try:
            if not title:
                raise ValueError("Task title cannot be empty.")
            
            self.title = title
            self.due_date = due_date
            self.notes = notes or ""
            self.subtasks = subtasks or []
        except Exception as e:
            print(f"Error creating task: {e}")
            # You might want to log the error or handle it in a way that makes sense for your application

    def add_subtask(self, subtask):
        try:
            if not subtask:
                raise ValueError("Subtask cannot be empty.")
            
            self.subtasks.append(subtask)
        except Exception as e:
            print(f"Error adding subtask: {e}")
            # You might want to log the error or handle it in a way that makes sense for your application

    def __str__(self):
        return f"Task: {self.title}, Due Date: {self.due_date}, Notes: {self.notes}, Subtasks: {self.subtasks}"
