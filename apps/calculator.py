"""A small calculator built with Tkinter."""
import tkinter as tk


class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculator")
        self.geometry("300x400")
        self.resizable(False, False)
        self.expression = ""
        self._build()

    def _build(self):
        self.display = tk.Entry(self, font=("Segoe UI", 20), justify="right")
        self.display.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=8, pady=8)

        buttons = [
            ("C", 1, 0), ("(", 1, 1), (")", 1, 2), ("/", 1, 3),
            ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("*", 2, 3),
            ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("-", 3, 3),
            ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("+", 4, 3),
            ("0", 5, 0), (".", 5, 1), ("=", 5, 2),
        ]
        for text, row, col in buttons:
            tk.Button(self, text=text, font=("Segoe UI", 16),
                      command=lambda t=text: self.on_press(t)).grid(
                row=row, column=col, sticky="nsew", padx=4, pady=4)
        for i in range(4):
            self.grid_columnconfigure(i, weight=1)
        for i in range(6):
            self.grid_rowconfigure(i, weight=1)

    def on_press(self, key):
        if key == "C":
            self.expression = ""
        elif key == "=":
            try:
                self.expression = str(eval(self.expression, {"__builtins__": {}}))
            except Exception:
                self.expression = "Error"
        else:
            self.expression += key
        self.display.delete(0, tk.END)
        self.display.insert(0, self.expression)


if __name__ == "__main__":
    Calculator().mainloop()
