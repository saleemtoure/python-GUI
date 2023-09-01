import tkinter as tk
from tkinter import messagebox


class ListGUI:
    def __init__(self):
        self.root = tk.Tk()

        self.label = tk.Label(self.root, text="Din Liste", font=("Arial", 19))
        self.label.pack(padx=10, pady=10)

        self.entrybox = tk.Entry(self.root, font=("Arial", 16), width=20)
        self.entrybox.bind("<Return>", self.add_objective)
        self.entrybox.pack(padx=10, pady=10)

        self.scrollbar = tk.Scrollbar(self.root)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)
        self.listbox = tk.Listbox(
            self.root, font=("Arial", 16), activestyle="dotbox", width=20
        )
        self.listbox.pack(padx=10, pady=10)
        self.listbox.config(yscrollcommand=self.scrollbar.set)
        self.listbox.bind("<<ListboxSelect>>", self.delete_objective)
        self.scrollbar.config(command=self.listbox.yview)

        self.clear_btn = tk.Button(text="Clear", padx=10, pady=10, command=self.reset)
        self.clear_btn.pack(padx=10, pady=10)

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()

    def add_objective(self, event):
        self.listbox.insert("end", self.entrybox.get())

    def delete_objective(self, event):
        if self.listbox.curselection() == ():
            pass
        else:
            if messagebox.askyesno(
                title="Quit?", message="Vil du slette denne tasken?"
            ):
                self.listbox.delete(self.listbox.curselection())

    def reset(self):
        self.listbox.delete(0, "end")

    def on_closing(self):
        if messagebox.askyesno(title="Quit?", message="Vil du virkelig avslutte"):
            self.root.destroy()


ListGUI()
