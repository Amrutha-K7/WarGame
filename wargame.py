
import random


TOTAL_CARDS=52
PLAYER_CARDS_COUNT=26

suits = ['Hearts','Clubs','Spades','Diamonds']
ranks = [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']

#a dictionary holding number value for each card rank (or) [key = card rank value= numberic value of the rank]
rank_value_map = {2: 2, 3: 3, 4: 4, 5: 5, 6 : 6 , 7 :7, 8: 8,9:9,10:10,'Jack':11, 'Queen': 12,'King': 13,'Ace':14 }


#Card class includes all the properties of each card like the suit, rank and rank_value mapping of each card
class Card():

    #initializing card properties using the constructor
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = rank_value_map[rank]


#Deck class makes a list of 52 card objects (each card object will have card class properties) and shuffles them
class Deck():

    def __init__(self):
        # list of card objects
        self.deck_of_cards = []  

        #creating cards for all suits, each suit will have 13 cards
        for suit in suits:
            for rank in ranks:
                # create card object
                new_card = Card(suit, rank)
                self.deck_of_cards.append(new_card)
        
        #Now we have self.deck_of_cards containing 52 card objects in the order of the suits
        #so we need to shuffle them for randomness

        def shuffle_cards(self):
             random.shuffle(self.deck_of_cards)

#player calss includes properties of each player like player name and player_cards deck of 26 cards
class Player():

    def __init__(self, name):
        self.player_name = name
        self.player_cards = []

# Gameplay class includes the main logic of the war game, starting with dealing cards to both players,
# 
class Gameplay:
    def __init__(self,player1_name,player2_name):

        # Create deck and shuffle
        self.current_deck = Deck()

        self.current_deck.shuffle()
