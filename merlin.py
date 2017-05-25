#import tkinter, random, pygame
"""Game MERLIN"""
from random import random
kurseddane = 0
maunder = 0
fullton = 0
algor = 0
cards = []
hand = []
deckCut = False
def cutDeck(n1,n2,w):
    x = {'name1': n1, 'name2': n2, 'fullname': n1 + " " + n2, 'worth': w}
    cards.append(x)
def main():
    global kurseddane,maunder,fullton,algor,cards,hand,deckCut,random
    pCounties = ['FULLTON','MAUNDER','KURSEDDANE','ALGOR']
    showHand = []
    if not deckCut:
        counties = ['FULLTON','MAUNDER','KURSEDDANE','ALGOR','FULLTON','MAUNDER','KURSEDDANE','ALGOR','WILD']
        ranks = {'FOOTSOLDIER': 1,'SERGEANT': 2,'HORSEMAN': 3, 'GENERAL': 4}
        x = len(counties) - 1
        while x > -1:
            for rank in ranks:
                cutDeck(counties[x],rank,ranks[rank])
            x -= 1
        deckCut = True
    while len(hand) < 4:
        pivk = int(random()*len(cards))
        draw = cards[pivk]
        del(cards[pivk])
        showHand.append(draw['fullname'])
        hand.append(draw)
    def pickCard():
        fullCards = ', '.join(showHand)
        ask = input("Your hand is " + fullCards + ". Which one do you want?")
        print('printing')
        if not ask in showHand:
            print("That is not a card in your hand.")
            pickCard()
        else:
            return ask
    chosen = pickCard()
    def returnCounty(actual):
        counter = 3
        while counter > -1:
            if hand[counter]['fullname'] == chosen:
                actual = counter
                if hand[counter]['name1'] == 'WILD':
                    pickCounty = input('Your card is wild. Which county do you pick?')
                    if not pickCounty in pCounties:
                        print("Sorry, that is not a county")
                        returnCounty()
                    else:
                        return pickCounty
                else:
                    return hand[counter]['name1']
    placement = None
    chosenC = returnCounty(placement)
    def activateCard():
        cardW = hand[placement]['worth']
        if chosenC == 'FULLTON':
            fullton += cardW
        elif chosenC == 'ALGOR':
            algor += cardW
        elif chosenC == 'KURSEDDANE':
            kurseddane += cardW
        elif chosenC == 'MAUNDER':
            kurseddane += cardW
        del(hand[placement])
    activateCard()
    print('Kurseddane is',kurseddane)
    print('Maunder is',maunder)
    print('Algor is',algor)
    print('Fullton is',fullton)
main()
