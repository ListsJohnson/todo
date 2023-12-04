# models/tasklist.py
class TaskList:
    def __init__(self, title):
        if not title:
            raise ValueError("Task list title cannot be empty.")
        
        self.title = title
        self.tasks = []

    def add_task(self, task):
        if not task:
            raise ValueError("Task cannot be empty.")
        
        self.tasks.append(task)

    def remove_task(self, task):
        try:
            self.tasks.remove(task)
        except ValueError as ve:
            print(f"Error removing task from task list: {ve}")
            # Task not found in the list
        except Exception as e:
            print(f"Error removing task from task list: {e}")
            # You might want to log the error or handle it in a way that makes sense for your application

    def __str__(self):
        return f"TaskList: {self.title}, Tasks: {[task.title for task in self.tasks]}"
