# views/main_view.py
import tkinter as tk
from todo.views.task_lists_view import TaskListsView

class MainView(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("To-Do App")
        self.geometry("800x600")

        # Display the task lists view
        self.task_lists_view = TaskListsView(self)
        self.task_lists_view.pack(fill=tk.BOTH, expand=True)

def main():
    app = MainView()
    app.mainloop()

if __name__ == "__main__":
    main()
