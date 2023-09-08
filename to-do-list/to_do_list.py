import os
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk, filedialog
import sv_ttk


class ListGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("To Do List - github.com/saleemtoure")
        sv_ttk.set_theme("dark")

        self.root.maxsize(370, 500)
        self.root.minsize(370, 500)

        self.label = ttk.Label(self.root, text="TO DO", font=("Arial", 19))
        self.label.pack(padx=10, pady=10)

        self.entrybox = ttk.Entry(self.root, font=("Arial", 16), width=20)
        self.entrybox.bind("<Return>", self.add_objective)
        self.entrybox.pack(padx=10, pady=10)

        self.listbox = ttk.Treeview(self.root, show="tree")
        self.listbox.pack(padx=10, pady=10, fill="both", expand=True)

        self.listbox.bind("<<TreeviewSelect>>", self.delete_objective)

        self.out_btn = ttk.Button(text="Save as txt file", command=self.save)
        self.out_btn.pack(pady=2)

        self.inn_btn = ttk.Button(text="Load list from txt file", command=self.load)
        self.inn_btn.pack()

        self.clear_btn = ttk.Button(text="Clear", command=self.reset)
        self.clear_btn.pack(padx=10, pady=10)

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()

    def add_objective(self, event):
        self.listbox.insert("", "end", text=self.entrybox.get())

    def delete_objective(self, event):
        if self.listbox.selection() == ():
            pass
        else:
            if messagebox.askyesno(
                title="Quit?", message="Do you want to delete this task?"
            ):
                self.listbox.delete(self.listbox.selection())

    def save(self):
        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt", filetypes=[("Text Files", "*.txt")]
        )
        if file_path == "":
            pass
        elif os.path.exists(file_path):
            f = open(file_path, "w")
            for task in self.listbox.get_children():
                f.write(f"{self.listbox.item(task)['text']}\n")
            f.close()

    def load(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if file_path == "":
            pass
        else:
            f = open(file_path, "r")
            self.reset()
            for line in f:
                self.listbox.insert("", "end", text=line)
            f.close()

    def reset(self):
        for task in self.listbox.get_children():
            self.listbox.delete(task)

    def on_closing(self):
        if messagebox.askyesno(title="Quit?", message="Do you really want to quit?"):
            self.root.destroy()


ListGUI()
