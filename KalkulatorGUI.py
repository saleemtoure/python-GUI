import tkinter as tk
from tkinter import messagebox

utregning=""
def leggTilUtregning(symbol):
    global utregning
    utregning+=str(symbol)
    resultatBox.delete(1.0,"end")
    resultatBox.insert(1.0,utregning)
def evaluerUtregning():
    global utregning
    try:
        utregning=str(eval(utregning))
        resultatBox.delete(1.0,"end")
        resultatBox.insert(1.0,utregning)
    except:
        clearFelt()
        resultatBox.insert(1.0,"Error")
def clearFelt():
    global utregning
    utregning=""
    resultatBox.delete(1.0,"end")

# def backspace():
#     resultatBox.insert(1.0,int(str(utregning)[:-1]))
root=tk.Tk()
root.geometry("400x600")
root.title("Kalkulator")

label=tk.Label(root,text="Kalkulator",font=("Arial",18))
label.pack(padx=20,pady=20)

resultatBox=tk.Text(root, height=1, font=("Arial", 24))
resultatBox.pack(padx=10, pady=10)

buttonframe=tk.Frame(root)
buttonframe.columnconfigure(0,weight=1)
buttonframe.columnconfigure(1,weight=1)
buttonframe.columnconfigure(2,weight=1)
buttonframe.columnconfigure(3,weight=1)

btn_d = tk.Button(buttonframe, text=chr(247),command=lambda: leggTilUtregning("/"), font=("Helvetica", 18))
btn_d.grid(row=0, column=3, sticky=tk.W + tk.E)
# btn_bs = tk.Button(buttonframe, text=chr(9003),command=backspace,font=("Helvetica", 18))
# btn_bs.grid(row=0, column=2, sticky=tk.W + tk.E)
btn_c = tk.Button(buttonframe, text="C",command=clearFelt, font=("Helvetica", 18))
btn_c.grid(row=0, column=1, sticky=tk.W + tk.E)
# btn_sqr = tk.Button(buttonframe, text="x\u00b2",command=lambda: kvadrer(), font=("Helvetica", 18))
# btn_sqr.grid(row=0, column=0, sticky=tk.W + tk.E)
#
btn_g = tk.Button(buttonframe, text="*",command=lambda: leggTilUtregning("*"), font=("Helvetica", 18))
btn_g.grid(row=1, column=3, sticky=tk.W + tk.E)
btn9 = tk.Button(buttonframe, text=9,command=lambda: leggTilUtregning(9), font=("Helvetica", 18))
btn9.grid(row=1, column=2, sticky=tk.W + tk.E)
btn8 = tk.Button(buttonframe, text=8,command=lambda: leggTilUtregning(8),font=("Helvetica", 18))
btn8.grid(row=1, column=1, sticky=tk.W + tk.E)
btn7 = tk.Button(buttonframe, text=7,command=lambda: leggTilUtregning(7), font=("Helvetica", 18))
btn7.grid(row=1, column=0, sticky=tk.W + tk.E)

#
btn_m = tk.Button(buttonframe, text="-",command=lambda: leggTilUtregning("-"), font=("Helvetica", 18))
btn_m.grid(row=2, column=3, sticky=tk.W + tk.E)
btn6 = tk.Button(buttonframe, text=6,command=lambda: leggTilUtregning(6), font=("Helvetica", 18))
btn6.grid(row=2, column=2, sticky=tk.W + tk.E)
btn5 = tk.Button(buttonframe, text=5, command=lambda: leggTilUtregning(5),font=("Helvetica", 18))
btn5.grid(row=2, column=1, sticky=tk.W + tk.E)
btn4 = tk.Button(buttonframe, text=4,command=lambda: leggTilUtregning(4), font=("Helvetica", 18))
btn4.grid(row=2, column=0, sticky=tk.W + tk.E)

#
btn_p = tk.Button(buttonframe, text="+",command=lambda: leggTilUtregning("+"),font=("Helvetica", 18))
btn_p.grid(row=3, column=3, sticky=tk.W + tk.E)
btn3 = tk.Button(buttonframe, text=3, command=lambda: leggTilUtregning(3),font=("Helvetica", 18))
btn3.grid(row=3, column=2, sticky=tk.W + tk.E)
btn2 = tk.Button(buttonframe, text=2,command=lambda: leggTilUtregning(2), font=("Helvetica", 18))
btn2.grid(row=3, column=1, sticky=tk.W + tk.E)
btn1 = tk.Button(buttonframe, text=1,command=lambda: leggTilUtregning(1), font=("Helvetica", 18))
btn1.grid(row=3, column=0, sticky=tk.W + tk.E)

#
btn0 = tk.Button(buttonframe, text=0,command=lambda: leggTilUtregning(0), font=("Helvetica", 18))
btn0.grid(row=4, column=1, sticky=tk.W + tk.E)
btn_k = tk.Button(buttonframe, text=",",command=lambda: leggTilUtregning("."), font=("Helvetica", 18))
btn_k.grid(row=4, column=2, sticky=tk.W + tk.E)
btn_e = tk.Button(buttonframe, text="=",command=evaluerUtregning, font=("Helvetica", 18))
btn_e.grid(row=4, column=3, sticky=tk.W + tk.E)

buttonframe.pack(fill="x")
root.mainloop()


