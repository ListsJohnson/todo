# models/tasklist.py
class TaskList:
    def __init__(self, title):
        self.title = title
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        self.tasks.remove(task)

    def __str__(self):
        return f"TaskList: {self.title}, Tasks: {[task.title for task in self.tasks]}"
