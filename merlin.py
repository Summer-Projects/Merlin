"""Game MERLIN"""
from random import random
kurseddane, algor, maunder, fullton = 0,0,0,0
counties = ['FULLTON','ALGOR','MAUNDER','KURSEDDANE']
cards = []
hand = []
showHand = []
AIhand = []
x = 0
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

def addCardsToHand():
    global cards, hand, showHand
    if len(hand) < 4:
        draw = int(len(cards) * random())
        hand.append(cards[draw])
        showHand.append(cards[draw]['fullname'])
        del(cards[draw])
        addCardsToHand()

def chooseCard():
    global showHand, x
    joinedHand = ', '.join(showHand)
    ask = input('Your hand is ' + joinedHand + '. Which card do you pick?').upper()
    if not ask in showHand:
        print("Sorry, that is not a card in your hand")
        chooseCard()
    else:
        x = 0
        while x < 4:
            if showHand[x] == ask:
                break
            x += 1
        del(showHand[x])
    return x
def pickCounty(n):
    global hand
    if hand[n]['name1'] == 'WILD':
        ask = input('You picked a wild card. Which county do you want?').upper()
        if not ask in counties:
            print("Sorry, that is not a county")
            pickCounty(n)
        return ask
    else:
        return hand[n]['name1']

def war(army, county):
    global maunder, kurseddane, algor, fullton
    if county == 'KURSEDDANE':
        kurseddane += army
    elif county == 'ALGOR':
        algor += army
    elif county == 'MAUNDER':
        maunder += army
    elif county == 'FULLTON':
        fullton += army

def aiHand():
    if len(AIhand) < 4:
        draw = int(random()*len(cards))
        AIhand.append(cards[draw])
        del(cards[draw])
        aiHand()

def aiWar(cardNum):
    global maunder, kurseddane, algor, fullton
    card = AIhand[cardNum]
    if card['name1'] == 'WILD':
        choose = int(random()*4)
        county = counties[choose]
    else:
        county = card['name1']
    worth = card['worth']
    if county == 'KURSEDDANE':
        kurseddane -= worth
    elif county == 'ALGOR':
        algor -= worth
    elif county == 'MAUNDER':
        maunder -= worth
    elif county == 'FULLTON':
        fullton -= worth
    print('King Arthur Intellect played a ' + card['name2'] + ' against ' + county)
    del(AIhand[cardNum])
    
def main():
    cutDeck()
    addCardsToHand()
    placement = chooseCard()
    power = hand[placement]['worth']
    county = pickCounty(placement)
    del(hand[placement])
    war(power, county)
    aiHand()
    pick = int(random()*4)
    aiWar(pick)
    nameToNumDict = {'FULLTON': fullton, 'KURSEDDANE': kurseddane, 'MAUNDER': maunder, 'ALGOR': algor}
    for field in nameToNumDict:
        if nameToNumDict[field] > 0:
            print('You have a force of ' + str(nameToNumDict[field]) + ' in ' + field)
        elif nameToNumDict[field] < 0:
            print('King Arthur Intellect has a force of ' + str(nameToNumDict[field] * -1) + ' in ' + field)
        else:
            print('No one has a force in ' + field)
    if kurseddane > 0 and maunder > 0 and fullton > 0 and algor > 0:
        print('Congrats! You have defeated King Arthur Intellect! You are now Lord of Merlin')
    elif kurseddane < 0 and maunder < 0 and fullton< 0 and algor < 0:
        print('King Arthur Intellect has defeated you, and is now Lord of Merlin. You go back to your country in shame')
    else:
        main()
        
main()
