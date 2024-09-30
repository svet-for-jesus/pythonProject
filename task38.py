#Игра "Крестики-нолики": Создайте игру "Крестики-нолики" для двух игроков на одном компьютере с GUI.
from random import choice
from tkinter import  *
import tkinter as tk

from pyexpat.errors import messages

root=tk.Tk()
root.title("Крестики-нолики")
root.geometry("178x190")

label1=tk.Label(root, text="Ход 1 игрока", anchor="center" )
label1.grid(row=0, column=0, columnspan=3 )

button=tk.Button()
button0=tk.Button(root, textvariable=messages, command=choice, width=7, height=3)
button1=tk.Button(root, textvariable=messages,command=choice,  width=7, height=3)
button2=tk.Button(root, textvariable=messages,command=choice,  width=7, height=3)
button3=tk.Button(root, textvariable=messages,command=choice,  width=7, height=3)
button4=tk.Button(root, textvariable=messages,command=choice,  width=7, height=3)
button5=tk.Button(root, textvariable=messages,command=choice,  width=7, height=3)
button6=tk.Button(root, textvariable=messages,command=choice,  width=7, height=3)
button7=tk.Button(root, textvariable=messages,command=choice,  width=7, height=3)
button8=tk.Button(root, textvariable=messages,command=choice,  width=7, height=3)


def choice(user):
    if user=="first":

    label1 = tk.Label(root, text="Ход 1 игрока", anchor="center")
button0.grid(row=1, column=0)
button1.grid(row=1, column=1)
button2.grid(row=1, column=2)
button3.grid(row=2, column=0)
button4.grid(row=2, column=1)
button5.grid(row=2, column=2)
button6.grid(row=3, column=0)
button7.grid(row=3, column=1)
button8.grid(row=3, column=2)
root.mainloop()