import tkinter as tk
from tkinter.ttk import *
from time import strftime 


relogio = tk.Tk()

relogio.title("Relógio")

def exibirHora():
    hora = strftime("%H:%M:%S %p")
    display.config(text= hora)
    display.after(1000, exibirHora)
    
display = Label(relogio,
    font=("helvetica", 32, "bold"),
    background= "black",
    foreground ="green")
            
display.pack(anchor="center")

exibirHora()                
                                
relogio.mainloop()