import tkinter as tk
from tkinter import messagebox
import sys

COLORS = {
    "background": "#1e1e1e",
    "entry_bg": "#2c2c2c",
    "entry_fg": "#ffffff",
    "btn_bg": "#3c3c3c",
    "btn_fg": "#000000",
    "btn_active_bg": "#5a5a5a",
    "operator_bg": "#ffa500",
    "operator_fg": "#000000",
    "special_bg": "#666666",
    "special_fg": "#000000",
    "equals_bg": "#3399ff",
    "equals_fg": "#000000",
    "equals_active_bg": "#5cabff"
}

class FullCalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("500x600")
        self.root.resizable(False, False)
        self.root.configure(bg=COLORS["background"])
        self.center_window(500, 600)

        self.expression = ""

        self.create_widgets()
        

        
        root.lift()
        root.attributes("-topmost", True)
        root.after(100, lambda: root.attributes("-topmost", False))
        root.focus_force()

    def center_window(self, w, h):
        sw = self.root.winfo_screenwidth()
        sh = self.root.winfo_screenheight()
        x = (sw - w) // 2
        y = (sh - h) // 2
        self.root.geometry(f"{w}x{h}+{x}+{y}")

    def create_widgets(self):
        entry_frame = tk.Frame(self.root, bg=COLORS["background"])
        entry_frame.pack(padx=20, pady=(20, 10), fill="x")

        self.entry = tk.Entry(
            entry_frame,
            font=("Helvetica", 32),
            bg=COLORS["entry_bg"],
            fg=COLORS["entry_fg"],
            justify="right",
            borderwidth=0,
            relief="flat",
            insertbackground=COLORS["entry_fg"]
        )
        self.entry.pack(fill="x", ipady=15)
        self.entry.focus()

        self.root.bind("<Return>", lambda e: self.evaluate())
        self.root.bind("<Escape>", lambda e: self.clear())
        self.root.bind("<BackSpace>", lambda e: self.backspace())

        self.create_buttons()

    def create_buttons(self):
        buttons = [
            ['C', '⌫', '%', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['0', '.', '^', '=']
        ]

        operators = ['/', '*', '-', '+', '^']
        specials = ['C', '⌫', '%']

        btn_frame = tk.Frame(self.root, bg=COLORS["background"])
        btn_frame.pack(padx=20, pady=10, fill="both", expand=True)

        for r, row in enumerate(buttons):
            for c, char in enumerate(row):
                action = lambda val=char: self.button_action(val)

                if char in operators:
                    bg, fg, active_bg = COLORS["operator_bg"], COLORS["operator_fg"], COLORS["operator_bg"]
                elif char in specials:
                    bg, fg, active_bg = COLORS["special_bg"], COLORS["special_fg"], COLORS["special_bg"]
                elif char == '=':
                    bg, fg, active_bg = COLORS["equals_bg"], COLORS["equals_fg"], COLORS["equals_active_bg"]
                else:
                    bg, fg, active_bg = COLORS["btn_bg"], COLORS["btn_fg"], COLORS["btn_active_bg"]

                btn = tk.Button(
                    btn_frame,
                    text=char,
                    font=("Helvetica", 20, "bold"),
                    bg=bg,
                    fg=fg,
                    activebackground=active_bg,
                    activeforeground=fg,
                    relief="flat",
                    borderwidth=0,
                    command=action
                )

                if char == '0':
                    btn.grid(row=r, column=0, columnspan=2, sticky="nsew", padx=6, pady=6)
                elif char == '.':
                    btn.grid(row=r, column=2, sticky="nsew", padx=6, pady=6)
                elif char in ['^', '=']:
                    btn.grid(row=r, column=3, sticky="nsew", padx=6, pady=6)
                else:
                    btn.grid(row=r, column=c, sticky="nsew", padx=6, pady=6)

        for i in range(5):
            btn_frame.grid_rowconfigure(i, weight=1)
        for i in range(4):
            btn_frame.grid_columnconfigure(i, weight=1)

    def add_to_expression(self, value):
        self.expression += str(value)
        self.update_entry()

    def update_entry(self):
        self.entry.delete(0, tk.END)
        self.entry.insert(0, self.expression)

    def clear(self):
        self.expression = ""
        self.update_entry()

    def backspace(self):
        self.expression = self.expression[:-1]
        self.update_entry()

    def evaluate(self):
        try:
            result = eval(self.expression.replace("^", "**"))
            self.expression = str(result)
            self.update_entry()
        except ZeroDivisionError:
            messagebox.showerror("Math Error", "Cannot divide by zero!")
            self.clear()
        except Exception:
            messagebox.showerror("Input Error", "Invalid expression!")
            self.clear()

    def button_action(self, char):
        if char == 'C':
            self.clear()
        elif char == '⌫':
            self.backspace()
        elif char == '=':
            self.evaluate()
        else:
            self.add_to_expression(char)

if __name__ == "__main__":
    root = tk.Tk()
    def on_closing():
        root.destroy()
        sys.exit(0)
    root.protocol("WM_DELETE_WINDOW", on_closing)
    app = FullCalculatorApp(root)
    root.mainloop()
