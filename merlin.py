"""Game MERLIN with TKinter.
Here is a basic outline of how the code goes:

Module importation and variable making
Various python functions that makes cards
Card functions
Tkinter program
Wild functions
Refresh function
Main function
"""
#imports modules and makes variables
from tkinter import *
from random import random
kurseddane, algor, maunder, fullton = 0,0,0,0
counties = ['FULLTON','ALGOR','MAUNDER','KURSEDDANE']
cards = []
hand = []
AIhand = []
x = 0
wildCard = {}

#python functions
def makeCard(n1,n2,w):
    x = {'name1': n1, 'name2':n2, 'fullname': n1 + " " + n2, 'worth': w}
    cards.append(x)
    
def cutDeck():
    if len(cards) == 0:
        counties = ['ALGOR','FULLTON','MAUNDER','KURSEDDANE','FULLTON','ALGOR','MAUNDER','KURSEDDANE','WILD']
        ranks = {'FOOTSOLDIER': 1,'SERGEANT':2,'HORSEMAN': 3, 'GENERAL': 4}
        x = len(counties) - 1
        while x > -1:
            for rank in ranks:
                makeCard(counties[x],rank,ranks[rank])
            x -= 1
        for card in hand:
            if card in cards:
                position = cards.index(card)
                del(cards[position])
        for card in AIhand:
            if card in cards:
                position = cards.index(card)
                del(cards[position])
cutDeck()

def addCardsToHand():
    global cards, hand
    if len(hand) < 4:
        draw = int(len(cards) * random())
        hand.append(cards[draw])
        del(cards[draw])
        addCardsToHand()
addCardsToHand()

#ai functions
def makeAIhand():
    if len(AIhand) < 4:
        draw = int(len(cards) * random())
        AIhand.append(cards[draw])
        del(cards[draw])
        makeAIhand()
def AIcountyPick(num):
    card = AIhand[num]
    if not card['name1'] == 'WILD':
        return card['name1']
    else:
        countyPick = counties[int(4 * random())]
        return countyPick

def AIwar(placement,county):
    global kurseddane, algor, maunder, fullton
    army = AIhand[placement]['worth']
    if county == 'KURSEDDANE':
        kurseddane -= army
    elif county == 'ALGOR':
        algor -= army
    elif county == 'MAUNDER':
        maunder -= army
    elif county == 'FULLTON':
        fullton -= army
    text.configure(text='King Arthur Intellect played an ' + AIhand[placement]['name2'] + ' against ' + county) 
    del(AIhand[placement])
#card functions
def card0func():
    global maunder, kurseddane, algor, fullton, wildCard, card0
    if not hand[0]['name1'] == 'WILD':
        army = hand[0]['worth']
        county = hand[0]['name1']
        if county == 'KURSEDDANE':
            kurseddane += army
        elif county == 'ALGOR':
            algor += army
        elif county == 'MAUNDER':
            maunder += army
        elif county == 'FULLTON':
            fullton += army
        del(hand[0])
        main()
    else:
        wildCard = hand[0]
        del(hand[0])
        wild()

def card1func():
    global maunder, kurseddane, algor, fullton, wildCard, card1
    if not hand[1]['name1'] == 'WILD':
        army = hand[1]['worth']
        county = hand[1]['name1']
        if county == 'KURSEDDANE':
            kurseddane += army
        elif county == 'ALGOR':
            algor += army
        elif county == 'MAUNDER':
            maunder += army
        elif county == 'FULLTON':
            fullton += army
        del(hand[1])
        main()
    else:
        wildCard = hand[1]
        del(hand[1])
        wild()

def card2func():
    global maunder, kurseddane, algor, fullton, wildCard,card2
    if not hand[2]['name1'] == 'WILD':
        army = hand[2]['worth']
        county = hand[2]['name1']
        if county == 'KURSEDDANE':
            kurseddane += army
        elif county == 'ALGOR':
            algor += army
        elif county == 'MAUNDER':
            maunder += army
        elif county == 'FULLTON':
            fullton += army
        del(hand[2])
        main()
    else:
        wildCard = hand[2]
        del(hand[2])
        wild()

def card3func():
    global maunder, kurseddane, algor, fullton, wildCard,card3
    if not hand[3]['name1'] == 'WILD':
        army = hand[3]['worth']
        county = hand[3]['name1']
        if county == 'KURSEDDANE':
            kurseddane += army
        elif county == 'ALGOR':
            algor += army
        elif county == 'MAUNDER':
            maunder += army
        elif county == 'FULLTON':
            fullton += army
        del(hand[3])
        main()
    else:
        wildCard = hand[3]
        del(hand[3])
        wild()

#makes tkinter program
program = Tk()
text = Label(program, text="Pick one of your cards")
text.grid(row=5, column=1, columnspan=2)
quitGame = Button(program, text="Quit", command=program.destroy, padx=25, pady=25)
quitGame.grid(row=6, column=6)
fulltonTK = Button(program, text="Fullton: " + str(fullton), padx=25, pady=30)
fulltonTK.grid(row=0, column=1)
algorTK = Button(program, text="Algor: " + str(algor), padx=27, pady=30)
algorTK.grid(row=0, column=2)
kurseddaneTK = Button(program, text="Kurseddane: " + str(kurseddane), padx=10, pady=30)
kurseddaneTK.grid(row=2, column=1)
maunderTK = Button(program, text="Maunder: " + str(maunder), padx=16, pady=30)
maunderTK.grid(row=2, column=2)
card0 = Button(program, text=hand[0]['fullname'], command=card0func, padx=25, pady=25,width=23)
card0.grid(row=4, column=0)
card1 = Button(program, text=hand[1]['fullname'], command=card1func, padx=25, pady=25,width=23)
card1.grid(row=4, column=1)
card2 = Button(program, text=hand[2]['fullname'], command=card2func, padx=25, pady=25,width=23)
card2.grid(row=4, column=2)
card3 = Button(program, text=hand[3]['fullname'], command=card3func, padx=25, pady=25,width=23)
card3.grid(row=4, column=3)

#wild functions
def wild():
    fulltonTK.configure(command=fulltonWild)
    algorTK.configure(command=algorWild)
    maunderTK.configure(command=maunderWild)
    kurseddaneTK.configure(command=kurseddaneWild)
    text.configure(text='Pick a county for a wild card')
    
def fulltonWild():
    global fullton,wildCard
    army = wildCard['worth']
    fullton += army
    wildCard = {}
    main()
def algorWild():
    global algor,wildCard
    army = wildCard['worth']
    algor += army
    wildCard = {}
    main()
def maunderWild():
    global maunder,wildCard
    army = wildCard['worth']
    maunder += army
    wildCard = {}
    main()
def kurseddaneWild():
    global kurseddane, wildCard
    army = wildCard['worth']
    kurseddane += army
    wildCard = {}
    main()
#tkinter functins
def refresh():
    card0.configure(text=hand[0]['fullname'])
    card1.configure(text=hand[1]['fullname'])
    card2.configure(text=hand[2]['fullname'])
    card3.configure(text=hand[3]['fullname'])
    fulltonTK.configure(text='Fullton: ' + str(fullton))
    algorTK.configure(text='Algor: ' + str(algor))
    maunderTK.configure(text='Maunder: ' + str(maunder))
    kurseddaneTK.configure(text='Kurseddane: ' + str(kurseddane))

def main():
    cutDeck()
    addCardsToHand()
    makeAIhand()
    AIcardPick = int(4*random())
    AIcounty = AIcountyPick(AIcardPick)
    AIwar(AIcardPick,AIcounty)
    refresh()
<<<<<<< HEAD
    countiesList = [kDict,mDict,fDictn,aDict]
    for stuff in countiesList:
        backgrounds(stuff)
=======
>>>>>>> 74e3be5dd110cf4a0bad27e2e17e1ff47e854326
    if kurseddane > 0 and maunder > 0 and fullton > 0 and algor > 0:
        text.configure(text="Congrats! You have defeated King Arthur Intellect and are Lord of Merlin!")
    elif kurseddane < 0 and maunder < 0 and fullton< 0 and algor < 0:
        text.configure(text="King Arthur Intellect has defeated you. You go back to your country in shame.")
        
main()
