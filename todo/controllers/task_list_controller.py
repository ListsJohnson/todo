# controllers/task_list_controller.py
from todo.models.tasklist import TaskList

class TaskListController:
    @staticmethod
    def create_task_list(title):
        # TODO: Implement logic to create a new task list
        return TaskList(title)

    @staticmethod
    def add_task(task_list, task):
        task_list.add_task(task)

    @staticmethod
    def remove_task(task_list, task):
        task_list.remove_task(task)
