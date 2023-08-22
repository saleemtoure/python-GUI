import tkinter as tk

root = tk.Tk()
root.geometry("400x400")
root.title("Converter")
root.config(bg="#856ff8")

label = tk.Label(root, text="Converter", font=("Arial", 18))
label.pack(padx=20, pady=20)

root.mainloop()
