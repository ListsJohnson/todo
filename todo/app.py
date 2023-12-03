# todo/app.py
import tkinter as tk
from todo.views.main_view import MainView

class ToDoApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("To-Do App")
        self.root.geometry("800x600")

        # Create the main view
        self.main_view = MainView()

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    todo_app = ToDoApp()
    todo_app.run()
