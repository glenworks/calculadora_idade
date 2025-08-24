from tkinter import *
from tkinter import ttk

aba = Tk()
aba.title("Calculadora de Idade")
aba.geometry('320x400')

#cores
cor1 ="#005E7A"
cor2 ="#057996"

#frames do app
frame_up = Frame(aba, width=320, height=150, pady=0, padx=0, relief=FLAT, background=cor1)
frame_up.grid(row=0, column=0)

frame_down = Frame(aba, width=320, height=300, pady=0, padx=0, relief=FLAT, bg=cor2)
frame_down.grid(row=1, column=0)

aba.grid_rowconfigure(0, weight=1)
aba.grid_rowconfigure(1, weight=3) 
aba.grid_columnconfigure(0, weight=1)

aba.mainloop() #cria interface grafica