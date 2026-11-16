"""A minimal to-do list built with Tkinter."""
import tkinter as tk
from tkinter import messagebox


class TodoApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("To-do list")
        self.geometry("400x500")
        self._build()

    def _build(self):
        self.entry = tk.Entry(self, font=("Segoe UI", 14))
        self.entry.pack(fill="x", padx=8, pady=8)
        self.entry.bind("<Return>", lambda _event: self.add_task())

        tk.Button(self, text="Add task", command=self.add_task).pack(fill="x", padx=8)
        self.listbox = tk.Listbox(self, font=("Segoe UI", 12))
        self.listbox.pack(fill="both", expand=True, padx=8, pady=8)
        tk.Button(self, text="Delete selected", command=self.delete_task).pack(fill="x", padx=8, pady=(0, 8))

    def add_task(self):
        text = self.entry.get().strip()
        if not text:
            messagebox.showwarning("Empty", "Type a task first.")
            return
        self.listbox.insert(tk.END, text)
        self.entry.delete(0, tk.END)

    def delete_task(self):
        selection = self.listbox.curselection()
        if not selection:
            messagebox.showinfo("No selection", "Select a task to delete.")
            return
        self.listbox.delete(selection[0])


if __name__ == "__main__":
    TodoApp().mainloop()
