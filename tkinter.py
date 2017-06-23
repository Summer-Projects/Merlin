"""from tkinter import *
main_window = Tk()
count_label = Label(main_window, text="Count: 0")
count_label.grid(row=0, column=1)
count_value = 0
def increment_count():
    global count_value, count_label
    count_value = count_value + 1
    count_label.configure(text="Count: " + str(count_value))
incr_button = Button(main_window, text="Increment", command=increment_count)
incr_button.grid(row=0, column=0)
quit_button = Button(main_window, text="Quit", background="red", command=main_window.destroy)
quit_button.grid(row=1, column=0)"""

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
    counties = ['FULLTON','MAUNDER','KURSEDDANE','ALGOR','FULLTON','MAUNDER','KURSEDDANE','ALGOR','WILD']
    ranks = {'FOOTSOLDIER': 1,'SERGEANT': 2,'HORSEMAN': 3, 'GENERAL': 4}
    rank = random.choice(ranks)
    countie = random.choice(counties)


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
maunder.grid(row=2, column=5)

quitGame = Button(program, text="Quit", command=program.destroy)
quitGame.grid(row=3, column=3)
