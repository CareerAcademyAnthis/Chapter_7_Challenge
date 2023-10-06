import random
import time


# Making the card for player
def getPlayerCard(i):
    # Suits don't matter so they will just be random
    suit = random.choice(suits)
    # Card p stands for card "player"
    global cardP
    cardP = f'''
   ---------
  |         |
  |  {player_cards[i]} of  |
  |         |
  |    {suit}    |
  |         |
   ---------
'''


# Making the card for the dealer
def getDealerCard(i):
    # Suits don't matter so they will just be random
    suit = random.choice(suits)
    # Card d stands for card "dealer"
    global cardD
    cardD = \
        '  ---------              --------- \n'\
        ' |         |            |         | \n'\
        f' |  {dealer_cards[i]} of  |            |         | \n'\
        ' |         |            |         | \n'\
        f' |    {suit}    |            |         | \n'\
        ' |         |            |         | \n'\
        '  ---------              --------- \n'


# Get a random card number
def randomCardPlayer():
    global type
    type = random.choice(card_type)
    player_cards.append(type)


def randomCardDealer():
    global type
    type = random.choice(card_type)
    dealer_cards.append(type)


# Both the suits and numbers
card_type = ['A ', '2 ', '3 ', '4 ', '5 ', '6 ', '7 ', '8 ', '9 ', '10', 'J ', 'Q ', 'K ']
suits = ["\u2663", "\u2665", "\u2666", "\u2660"]
# Lists for the card
player_cards = []
dealer_cards = []
money = 0
# The face down card
card = \
    '  --------- \n'\
    ' |         | \n'\
    ' |         | \n'\
    ' |         | \n'\
    ' |         | \n'\
    ' |         | \n'\
    '  --------- '


while True:
    # The first cards for each player and dealer
    randomCardPlayer()
    randomCardDealer()
    # The second cards for each player and dealer
    randomCardPlayer()
    randomCardDealer()
    # Printing the two first cards of both dealer and player
    print("The dealer's cards:")
    getDealerCard(0)
    print(f"{cardD}")
    # print(card)
    break
