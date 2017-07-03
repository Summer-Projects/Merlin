from tkinter import *
from random import *
from sys import *

program = Tk()

def fultonFunc():
    print("Fulton")

def algorFunc():
    print("Algor")

def kurseddaneFunc():
    print("Kurseddane")

def maunderFunc():
    print("Maunder")

def card():
    card1 = Button(program, text="card", command=maunderFunc)
    card1.grid(row=3, column=0)
    card2 = Button(program, text="card", command=maunderFunc)
    card2.grid(row=3, column=1)
    card3 = Button(program, text="card", command=maunderFunc)
    card3.grid(row=3, column=2)
    card4 = Button(program, text="card", command=maunderFunc)
    card4.grid(row=3, column=3)

fulton = Button(program, text="Fulton 0", command=fultonFunc, padx=25, pady=30)
fulton.grid(row=0, column=0)

algor = Button(program, text="Algor 0", command=algorFunc, padx=27, pady=30)
algor.grid(row=0, column=3)

kurseddane = Button(program, text="Kurseddane 0", command=kurseddaneFunc, padx=10, pady=30)
kurseddane.grid(row=2, column=0)

maunder = Button(program, text="Maunder 0", command=maunderFunc, padx=16, pady=30)
maunder.grid(row=2, column=3)

card1 = Button(program, text="card", command=kurseddaneFunc, padx=25, pady=25)
card1.grid(row=4, column=0)
card2 = Button(program, text="card", command=algorFunc, padx=25, pady=25)
card2.grid(row=4, column=1)
card3 = Button(program, text="card", command=fultonFunc, padx=25, pady=25)
card3.grid(row=4, column=2)
card4 = Button(program, text="card", command=maunderFunc, padx=25, pady=25)
card4.grid(row=4, column=3)

text = Label(program, text="Text text text")
text.grid(row=5, column=3)

quitGame = Button(program, text="Quit", command=program.destroy, padx=25, pady=25)
quitGame.grid(row=6, column=6)
