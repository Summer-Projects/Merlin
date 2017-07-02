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

fulton = Button(program, text="Fulton", command=fultonFunc)
fulton.grid(row=0, column=0)
# fulton number
fulton = Button(program, text="0", command=fultonFunc)
fulton.grid(row=0, column=1)

algor = Button(program, text="Algor", command=algorFunc)
algor.grid(row=0, column=3)
# algor number
algor = Button(program, text="0", command=algorFunc)
algor.grid(row=0, column=4)

kurseddane = Button(program, text="Kurseddane", command=kurseddaneFunc)
kurseddane.grid(row=2, column=0)
# kurseddande number
kurseddane = Button(program, text="0", command=kurseddaneFunc)
kurseddane.grid(row=2, column=1)

maunder = Button(program, text="Maunder", command=maunderFunc)
maunder.grid(row=2, column=3)
# maunder number
maunder = Button(program, text="0", command=maunderFunc)
maunder.grid(row=2, column=4)

card1 = Button(program, text="card", command=kurseddaneFunc)
card1.grid(row=3, column=0)
card2 = Button(program, text="card", command=algorFunc)
card2.grid(row=3, column=1)
card3 = Button(program, text="card", command=fultonFunc)
card3.grid(row=3, column=2)
card4 = Button(program, text="card", command=maunderFunc)
card4.grid(row=3, column=3)

quitGame = Button(program, text="Quit", command=program.destroy)
quitGame.grid(row=4, column=4)
