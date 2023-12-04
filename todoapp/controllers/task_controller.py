# controllers/task_controller.py
from todoapp.models.task import Task

class TaskController:
    @staticmethod
    def create_task(title, due_date=None, notes=None, subtasks=None):
        try:
            # TODO: Implement logic to create a new task
            new_task = Task(title, due_date, notes, subtasks)
            return new_task
        except Exception as e:
            print(f"Error creating task: {e}")
            # You might want to log the error or handle it in a way that makes sense for your application
            return None

    @staticmethod
    def edit_task(task, title=None, due_date=None, notes=None, subtasks=None):
        try:
            # TODO: Implement logic to edit an existing task
            if title:
                task.title = title
            if due_date:
                task.due_date = due_date
            if notes:
                task.notes = notes
            if subtasks:
                task.subtasks = subtasks
        except Exception as e:
            print(f"Error editing task: {e}")
            # You might want to log the error or handle it in a way that makes sense for your application

    @staticmethod
    def add_subtask(task, subtask):
        try:
            task.add_subtask(subtask)
        except Exception as e:
            print(f"Error adding subtask: {e}")
            # You might want to log the error or handle it in a way that makes sense for your application
