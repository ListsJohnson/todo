# views/main_view.py
import tkinter as tk
from todoapp.views.task_lists_view import TaskListsView

class MainView(tk.Tk):
    def __init__(self):
        try:
            super().__init__()

            self.title("To-Do App")
            self.geometry("800x600")

            # Display the task lists view
            self.task_lists_view = TaskListsView(self)
            self.task_lists_view.pack(fill=tk.BOTH, expand=True)
        except Exception as e:
            print(f"Error initializing main view: {e}")
            # You might want to log the error or raise an exception if needed
            raise e

def main():
    try:
        app = MainView()
        app.mainloop()
    except Exception as e:
        print(f"Error running the application: {e}")
        # You might want to log the error or raise an exception if needed
        raise e

if __name__ == "__main__":
    main()
