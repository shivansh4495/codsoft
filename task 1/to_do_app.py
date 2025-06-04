import tkinter as tk
from tkinter import messagebox, filedialog
import os

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        self.root.configure(bg="#2c2c2c")

        
        window_width = 600
        window_height = 600
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)
        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")
        
        
        root.lift()
        root.attributes("-topmost", True)
        root.after(100, lambda: root.attributes("-topmost", False))
        root.focus_force()

        
        self.root.lift()
        self.root.attributes('-topmost', True)
        self.root.after(100, lambda: self.root.attributes('-topmost', False))

        
        self.default_font = ("Arial", 18)

        
        tk.Label(root, text="Task Title (used for save file):", font=self.default_font, bg="#2c2c2c", fg="white").pack(pady=(10, 0))
        self.title_entry = tk.Entry(root, font=self.default_font, width=40)
        self.title_entry.pack(pady=(0, 10))

        
        tk.Label(root, text="Task Description:", font=self.default_font, bg="#2c2c2c", fg="white").pack()
        self.task_entry = tk.Text(root, height=2, width=40, font=self.default_font, wrap="word")
        self.task_entry.pack(pady=(0, 10))

        
        tk.Button(root, text="Add Task", font=("Arial", 14), command=self.add_task).pack(pady=5)

        
        self.task_listbox = tk.Listbox(root, selectmode=tk.SINGLE, font=("Courier", 14), width=60, height=10)
        self.task_listbox.pack(pady=10)

        
        btn_frame = tk.Frame(root, bg="#2c2c2c")
        btn_frame.pack(pady=5)

        tk.Button(btn_frame, text="Check Task", font=("Arial", 14), command=self.check_task).grid(row=0, column=0, padx=10)
        tk.Button(btn_frame, text="Uncheck Task", font=("Arial", 14), command=self.uncheck_task).grid(row=0, column=1, padx=10)
        tk.Button(btn_frame, text="Delete Selected Task", font=("Arial", 14), command=self.delete_task).grid(row=0, column=2, padx=10)

        
        io_frame = tk.Frame(root, bg="#2c2c2c")
        io_frame.pack(pady=10)

        tk.Button(io_frame, text="Save Tasks", font=("Arial", 14), command=self.save_tasks).grid(row=0, column=0, padx=10)
        tk.Button(io_frame, text="Load Tasks", font=("Arial", 14), command=self.load_tasks).grid(row=0, column=1, padx=10)

    def add_task(self):
        task = self.task_entry.get("1.0", tk.END).strip()
        if task:
            self.task_listbox.insert(tk.END, "[ ] " + task)
            self.task_entry.delete("1.0", tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter a task description.")

    def check_task(self):
        try:
            index = self.task_listbox.curselection()[0]
            task = self.task_listbox.get(index)
            if not task.startswith("[x]"):
                self.task_listbox.delete(index)
                self.task_listbox.insert(index, "[x]" + task[3:])
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task to check.")

    def uncheck_task(self):
        try:
            index = self.task_listbox.curselection()[0]
            task = self.task_listbox.get(index)
            if task.startswith("[x]"):
                self.task_listbox.delete(index)
                self.task_listbox.insert(index, "[ ]" + task[3:])
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task to uncheck.")

    def delete_task(self):
        try:
            index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(index)
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task to delete.")

    def save_tasks(self):
        title = self.title_entry.get().strip()
        if not title:
            messagebox.showerror("Error", "Please enter a title for the task file.")
            return

        filename = f"{title}.txt"
        with open(filename, "w") as file:
            file.write(f"** {title.upper()} **\n\n")
            for i in range(self.task_listbox.size()):
                file.write(f"{self.task_listbox.get(i)}\n")
        messagebox.showinfo("Success", f"Tasks saved to '{filename}'.")

    def load_tasks(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if file_path and os.path.exists(file_path):
            self.task_listbox.delete(0, tk.END)
            with open(file_path, "r") as file:
                lines = file.readlines()
                for line in lines:
                    if line.startswith("["):
                        self.task_listbox.insert(tk.END, line.strip())

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()