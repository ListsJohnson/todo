# controllers/task_list_controller.py
from todo.models.tasklist import TaskList

class TaskListController:
    @staticmethod
    def create_task_list(title):
        try:
            # TODO: Implement logic to create a new task list
            new_task_list = TaskList(title)
            return new_task_list
        except Exception as e:
            print(f"Error creating task list: {e}")
            # You might want to log the error or handle it in a way that makes sense for your application
            return None

    @staticmethod
    def add_task(task_list, task):
        try:
            task_list.add_task(task)
        except Exception as e:
            print(f"Error adding task to task list: {e}")
            # You might want to log the error or handle it in a way that makes sense for your application

    @staticmethod
    def remove_task(task_list, task):
        try:
            task_list.remove_task(task)
        except Exception as e:
            print(f"Error removing task from task list: {e}")
            # You might want to log the error or handle it in a way that makes sense for your application
