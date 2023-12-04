# todoapp/app.py
import tkinter as tk
from tkinter import messagebox
from todoapp.views.main_view import MainView

class ToDoApp:
    def __init__(self):
        try:
            self.root = tk.Tk()
            self.root.title("To-Do App")
            self.root.geometry("800x600")

            # Create the main view
            self.main_view = MainView()
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred during application initialization: {e}")
            # You might want to log the error or handle it in a way that makes sense for your application

    def run(self):
        try:
            self.root.mainloop()
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred during application execution: {e}")
            # You might want to log the error or handle it in a way that makes sense for your application

if __name__ == "__main__":
    todo_app = ToDoApp()
    todo_app.run()
