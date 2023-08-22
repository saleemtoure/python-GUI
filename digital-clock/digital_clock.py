import tkinter as tk
import time


class ClockGui:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Digital Clock")
        self.root.configure(bg="azure")
        self.time_now = time.ctime(time.time())
        self.label = tk.Label(self.root, text="", font=("Arial", 19),background="azure", foreground="darkblue")
        self.label.pack(padx=10, pady=10)

        self.update_time()
        self.root.mainloop()

    def update_time(self):
        self.time_now = time.ctime(time.time())
        self.label.config(text=self.time_now)
        self.root.after(1000, self.update_time)


ClockGui()
