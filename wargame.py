
import random


TOTAL_CARDS=52
PLAYER_CARDS_COUNT=26
DEBUG_CODE=0

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

    #Overriding string method for printing Card class Object: prints like "3 of heart"
    def __str__(self):
        return str(self.rank) + ' of ' + self.suit

    #overriding == in python to comapare the Card Object values
    def __eq__(self, other):
        if self.value == other.value:
            return True
        else:
            return False

    #overriding < in python to comapare the Card Object values
    def __lt__(self, other):
        if self.value < other.value:
            return True
        else:
            return False

    #overriding > in python to comapare the Card Object values
    def __gt__(self, other):
        if self.value > other.value:
            return True
        else:
            return False

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

#player calss includes properties of each player like player name and player_cards: deck of 26 cards
class Player():

    def __init__(self, name):
        self.player_name = name
        self.player_cards = [] #contains 26 Card class objects
    
    #this method is used to add cards to each players deck
    def add_cards(self, incoming_cards):

        #case: when a player wins more than one cards, it could be a war or normal gameplay case
        if type(incoming_cards) == type([]):
            self.player_cards.extend(incoming_cards)

        #case: when distributing cards to each player one by one
        else:
            self.player_cards.append(incoming_cards)

    
    def print_player_cards(self):
        print(f'Printing cards of player {self.player_name} for debug:')
        lst = [card.value for card in self.player_cards]
        print(lst)
        print()

    #overriding string method for printing Player class object; prints message like "player1 has 26 cards"
    def __str__(self):
        return f'Player {self.player_name} has {len(self.player_cards)} cards.'


# Gameplay class includes the main logic of the war game, starting with initializing both players, distributing cards
# and then playing the game
class Gameplay:
    def __init__(self,player1_name,player2_name):

        # Create deck of 52 cards
        self.current_deck = Deck()

        # Create two player objects
        self.player1 = Player(player1_name)
        self.player2 = Player(player2_name)


    #This method is used to distribute the cards to both the players after shuffling them
    def deal_deck_cards(self):

        print("Shuffling the deck of 52 cards...")
        #call the shuffle method in Deck class to shuffle the cards before distributing
        self.current_deck.shuffle_cards()

        print("Distributing 26 cards to both the players...")
        #distribute cards one at a time to each player's deck
        for i in range(0,len(self.current_deck.deck_of_cards),2):
            self.player1.add_cards(self.current_deck.deck_of_cards[i])
            self.player2.add_cards(self.current_deck.deck_of_cards[i+1])

        #test code to spot check if the cards are distributed properly
        assert len(self.player1.player_cards) == PLAYER_CARDS_COUNT
        assert len(self.player2.player_cards) == PLAYER_CARDS_COUNT

        #In case if we want to see the cards distributed to both the players for debugging purpose
        if DEBUG_CODE == 1:
            self.player1.print_player_cards()
            self.player2.print_player_cards()
    

    #This method is for distributing custom cards to both the players: this is for debugging various corner cases.
    def deal_test_cards(self,cards1,cards2):
        if DEBUG_CODE == 1:
            print("Dealing the customized cards")

        self.player1.player_cards=[]
        self.player2.player_cards=[]
        print("Distributing Custom deck cards to both the players...")
        self.player1.add_cards(cards1)
        self.player2.add_cards(cards2)

        if DEBUG_CODE == 1:
            self.player1.print_player_cards()
            self.player2.print_player_cards()


    #This method includes the actual game logic
    def start_game(self):
        temp_pile=[]

        #both players have at least 1 card to continue the play
        while len(self.player1.player_cards)>0 and len(self.player2.player_cards)>0:

            #get 1 card from each player from the front the queue
            first_card=self.player1.player_cards.pop(0)
            second_card=self.player2.player_cards.pop(0)

            print()
            print(f"Player1 {self.player1.player_name} has revealed the card: {first_card.value}")
            print(f"Player2 {self.player2.player_name} has revealed the card: {second_card.value}")

            #appending played cards to temp_pile list and comparing
            temp_pile.extend([first_card, second_card])

            #player1 has higher numbered card
            if first_card>second_card:
                 #avoid infinite loop possibility by shuffling and adding the cards won by a player to back of his deck
                random.shuffle(temp_pile)
                self.player1.add_cards(temp_pile)

                string= "both" if len(temp_pile) > 2 else "all"
                    
                print(f"Player1 {self.player1.player_name} gets {string} the cards..")
                #Clear the temporary pile
                temp_pile=[]
            
            #player2 has higher numbered card
            elif second_card > first_card:
                #avoid infinite loop possibility by shuffling and adding the cards won by a player to back of his deck
                random.shuffle(temp_pile)
                self.player2.add_cards(temp_pile)

                string= "all" if len(temp_pile) > 2 else "both"
                print(f"Player2 {self.player2.player_name} gets {string} the cards..")

                # Clear the temporary pile
                temp_pile = []

            #war: Both player cards have same number
            else:

                print("Both the player cards are equal, its a war..")
                #Make sure both the players have >= 3 cards to start the war, else exit and follow the logic to decide the winner
                if len(self.player1.player_cards)>=3 and len(self.player2.player_cards)>=3:
                    #pop 3 cards from both players and add it to temp_pile list and continue the loop to pick the next cards
                    
                    print("Both the players keeping 3 cards face-down..")
                    for _ in range(3):
                        temp_pile.append(self.player1.player_cards.pop(0))
                    for _ in range(3):
                        temp_pile.append(self.player2.player_cards.pop(0))
                else:
                    print("Atleast one of the players does not have adequate cards to continue..")
                    break #break out of while loop and decide the winner
            
            
        # we are here, when atleast one of the players have inadequate cards to continue the game so its
        # Time to decide the winner, 
        print()
        len1=len(self.player1.player_cards)
        len2=len(self.player2.player_cards)
        print(f'Number of cards Player1 {self.player1.player_name}={len1}')
        print(f'Number of cards Player2 {self.player2.player_name}={len2}')

        
        if len1==len2:
            print(f'Game is drawn between Player1 {self.player1.player_name} and Player2 {self.player2.player_name}')
        elif  len1>len2 :
            print(f'Player2 {self.player2.player_name} does not have adequate cards to continue..')
            print()
            print(f'*** Player1 {self.player1.player_name} has won the game ***')
            print()
        else:
            print(f'Player1 {self.player1.player_name} does not have adequate cards to continue..')
            print()
            print(f'*** Player2 {self.player2.player_name} has won the game ***')
            print()


#--------------------------------------------------------Main method------------------------------------------

if __name__ == "__main__":


    #This code is used for running the main game as an end user
    print()
    print("************** Starting War Game **************************\n")
    player1_name = input('Enter the name of the 1st player:   ')
    player2_name = input('Enter the name of the 2nd player:   ')
    print()
    war=Gameplay(player1_name,player2_name)
    #Distribute the cards to both the players
    war.deal_deck_cards()
    war.start_game()