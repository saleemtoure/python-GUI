import tkinter as tk
from tkinter import messagebox


class MyGUI:
    def __init__(self):
        self.root = tk.Tk()

        self.menubar = tk.Menu(self.root)

        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Close", command=self.onClosing)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Close Without Question", command=exit)

        self.actionmenu = tk.Menu(self.menubar, tearoff=0)
        self.actionmenu.add_command(label="Show Message", command=self.showMessage)

        self.menubar.add_cascade(menu=self.filemenu, label="File")
        self.menubar.add_cascade(menu=self.actionmenu, label="Action")

        self.root.config(menu=self.menubar)

        self.label = tk.Label(self.root, text="Your Message", font=("Arial", 19))
        self.label.pack(padx=10, pady=10)

        self.textbox = tk.Text(self.root, height=5, font=("Arial", 16))
        self.textbox.bind(
            "<KeyPress>", self.shortcut
        )  # for å gjøre at enter knappen kan brukes for å trykke på knappen
        self.textbox.pack(padx=10, pady=10)

        self.checkState = tk.IntVar()
        self.check = tk.Checkbutton(
            self.root,
            text="Show Messagebox",
            font=("Arial", 16),
            variable=self.checkState,
        )
        self.check.pack(padx=10, pady=10)

        self.button = tk.Button(
            self.root, text="Show Message", font=("Arial", 18), command=self.showMessage
        )
        self.button.pack(padx=10, pady=10)

        self.clearbtn = tk.Button(
            self.root, text="Clear", font=("Arial", 18), command=self.clear
        )
        self.clearbtn.pack(padx=10, pady=10)

        self.root.protocol("WM_DELETE_WINDOW", self.onClosing)
        self.root.mainloop()

    def showMessage(self):
        if self.checkState.get() == 0:
            print(self.textbox.get("1.0", tk.END))
        else:
            messagebox.showinfo(
                title="Message", message=self.textbox.get("1.0", tk.END)
            )

    def shortcut(self, event):
        # for å finne ut hvilken event du vil mappe noe til
        # print(event)
        # print(event.keysym)
        # print(event.state)
        if event.state == 4 and event.keysym == "Return":
            self.showMessage()

    def onClosing(self):
        # messagebox.showinfo(title="Closing Message", message="Seionara")
        if messagebox.askyesno(title="Quit?", message="Vil du virkelig avslutte"):
            self.root.destroy()

    def clear(self):
        self.textbox.delete("1.0", tk.END)


MyGUI()
