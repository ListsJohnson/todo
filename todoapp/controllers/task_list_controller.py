# controllers/task_list_controller.py
from todoapp.models.tasklist import TaskList

class TaskListController:
    @staticmethod
    def create_task_list(title):
        try:
            new_task_list = TaskList(title)
            return new_task_list
        except Exception as e:
            print(f"Error creating task list: {e}")
            # Log the error or raise a more specific exception if needed
            return None

    @staticmethod
    def add_task(task_list, task):
        try:
            task_list.add_task(task)
            return True  # Return True to indicate success
        except Exception as e:
            print(f"Error adding task to task list: {e}")
            # Log the error or raise a more specific exception if needed
            return False  # Return False to indicate failure

    @staticmethod
    def remove_task(task_list, task):
        try:
            task_list.remove_task(task)
            return True  # Return True to indicate success
        except Exception as e:
            print(f"Error removing task from task list: {e}")
            # Log the error or raise a more specific exception if needed
            return False  # Return False to indicate failure
