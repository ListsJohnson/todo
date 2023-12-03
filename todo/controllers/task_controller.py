# controllers/task_controller.py
from todo.models.task import Task

class TaskController:
    @staticmethod
    def create_task(title, due_date=None, notes=None, subtasks=None):
        # TODO: Implement logic to create a new task
        return Task(title, due_date, notes, subtasks)

    @staticmethod
    def edit_task(task, title=None, due_date=None, notes=None, subtasks=None):
        # TODO: Implement logic to edit an existing task
        if title:
            task.title = title
        if due_date:
            task.due_date = due_date
        if notes:
            task.notes = notes
        if subtasks:
            task.subtasks = subtasks

    @staticmethod
    def add_subtask(task, subtask):
        task.add_subtask(subtask)
