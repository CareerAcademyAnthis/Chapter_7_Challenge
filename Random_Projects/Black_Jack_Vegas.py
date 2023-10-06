import random

"""
Welcome to Black Jack Vegas

Game rules you will use one deck to play black jack against the dealer. You win the game if you get to 21 or your cords
have a higher value than the dealers cards without going over 21.

Aces = 1 or 11, All other cards are face value.
Jack, Queen, and King are 10

Dealer rules
Dealer has to hit (take a card) if less than 16
Dealer has to stay if over 17
If the dealer reaches 21 on the first deal they need to say Black Jack.


"""

print("Welcome to Black Jack Vegas \nGame rules you will use one deck to play black jack against the dealer.\n"
      "You win the game if you get to 21 or your cords have a higher value than the dealers cards without going over 21.\n"
      "Aces = 1 or 11, All other cards are face value. Jack, Queen, and King are 10\n"
      "Dealer rules\n"
      "Dealer has to hit (take a card) if less than 16\n"
      "Dealer has to stay if over 17\n"
      "If the dealer reaches 21 on the first deal they need to say Black Jack.\n\n")


def get_deck():
    card_value = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', "A"]
    card_suit = ['H', "S", "D", "C"]
    deck = []
    for suit in card_suit:
        for value in card_value:
            x = f"{value}{suit}"
            deck.append(x)
    return deck


get_deck()
game_deck = get_deck()
used_cards = []


def get_card():
    random_card = random.randint(0, len(game_deck))
    card = game_deck.pop(random_card)
    used_cards.append(card)
    return card


player_hand = []
dealer_hand = []


def deal():
    player_hand.append(get_card())
    player_hand.append(get_card())
    dealer_hand.append(get_card())
    dealer_hand.append(get_card())




    print(f"Your hand: {player_hand}")
    print(f"Dealers Hand: {dealer_hand[1:]}")




def hit():
    x = True
    while x == True:
        hit_question = input("Would you like to hit? (yes/no)")
        if hit_question == 'yes':
            player_hand.append(get_card())
            print(f"Your hand: {player_hand}")
        else:
            x = False



player_score = []
def score_player_hand():
    for card in player_hand:
        score_cards = [x for x in card]
        #print(score_cards)
        if len(score_cards) == 3:
            score = 10
        elif score_cards[0] == 'K' or score_cards[0] == 'Q' or score_cards[0] == 'J':
            score = 10
        elif score_cards[0] == "A":
            score = 11
        else:
            score = int(score_cards[0])

        #print(score)
        player_score.append(score)



    return sum(player_score)
dealer_score = []
def score_dealer_hand():
    for card in dealer_hand:
        d_score_cards = [x for x in card]
        #print(score_cards)
        if len(d_score_cards) == 3:
            d_score = 10
        elif d_score_cards[0] == 'K' or d_score_cards[0] == 'Q' or d_score_cards[0] == 'J':
            d_score = 10
        elif d_score_cards[0] == "A":
            d_score = 11
        else:
            d_score = int(d_score_cards[0])

        #print(score)
        dealer_score.append(d_score)

    if sum(dealer_score) <= 16:
        dealer_hand.append(get_card)
        sum(dealer_score)
        if sum(dealer_score) > 21:
            print("Bust")
    elif sum(dealer_score) == 21:
        print("Dealer has Black Jack")
    else:
        return sum(dealer_score)


deal()
print(f"{dealer_hand} his score is {score_dealer_hand()}")
hit()

if score_player_hand() > 21:
    print(f"{player_hand} Sorry you busted.")
else:
    print(f"{player_hand} your score is {score_player_hand()}")






