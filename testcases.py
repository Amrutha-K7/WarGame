from wargame import Gameplay,Card

#--------------------------------------------------------Building Custom decks------------------------------------------
player1_cards=[]
player2_cards=[]

def build_custom_deck(custom_suits, custom_ranks,player_cards):
    for suit in custom_suits:
        for rank in custom_ranks:
            # create card object
            created_card = Card(suit, rank)
            player_cards.append(created_card)

#This testcase is to check if the player1 wins or not: expectation is that player1 wins
def basic_player1_win_testcase():
    global player1_cards,player2_cards
    #clear the global variables
    player1_cards=[]
    player2_cards=[]
    suits1 = ['Hearts']
    ranks1 = [3, 4, 5, 6, 7, 8,9]
    suits2 = ['Clubs']
    ranks2 = [2, 3, 4, 5, 6, 7, 8]
    build_custom_deck(suits1,ranks1,player1_cards)
    build_custom_deck(suits2,ranks2,player2_cards)



#This testcase is to check if the player2 wins or not: expectation is that player2 wins
def basic_player2_win_testcase():
    global player1_cards,player2_cards
    #clear the global variables
    player1_cards=[]
    player2_cards=[]
    suits1 = ['Hearts']
    ranks1 = [2, 3, 4, 5, "Jack", 7, 8]
    suits2 = ['Clubs']
    ranks2 = [3, 4, 5, 6, "Ace", 8,9]
    build_custom_deck(suits1,ranks1,player1_cards)
    build_custom_deck(suits2,ranks2,player2_cards)


#This testcase is to check if the player1 wins with one of the war condition during the game
def basic_war_testcase(): 
    global player1_cards,player2_cards
    #clear the global variables
    player1_cards=[]
    player2_cards=[]
    suits1 = ['Hearts']
    ranks1 = [6, 3, 'Ace', 5, "Jack", 7, 9]
    suits2 = ['Clubs']
    ranks2 = [2, 3, 4, 'King', "Jack", 2, 8]
    build_custom_deck(suits1,ranks1,player1_cards)
    build_custom_deck(suits2,ranks2,player2_cards)


#This testcase is to check if the player1 and player2 go into draw or not
def basic_draw_testcase():
    global player1_cards,player2_cards
    #clear the global variables
    player1_cards=[]
    player2_cards=[]
    suits1 = ['Hearts']
    ranks1 = [2, 3, 4, 5, "Jack", 7, 8]
    suits2 = ['Clubs']
    ranks2 = [2, 3, 4, 5, "Jack", 7, 8]
    build_custom_deck(suits1,ranks1,player1_cards)
    build_custom_deck(suits2,ranks2,player2_cards)
#-----------------------------------------Test cases--------------------------------------------------------


name_of_player1 = "cookie"
name_of_player2 = "mickey"
war = Gameplay(name_of_player1,name_of_player2)

basic_player1_win_testcase() #add custom deck cards into player1_cards and player2_cards
war.deal_test_cards(player1_cards,player2_cards)
war.start_game()

print("********************************************************************************")
basic_player2_win_testcase() #add custom deck cards into player1_cards and player2_cards
war.deal_test_cards(player1_cards,player2_cards)
war.start_game()

print("********************************************************************************")
basic_war_testcase() #add custom deck cards into player1_cards and player2_cards
war.deal_test_cards(player1_cards,player2_cards)
war.start_game()

print("********************************************************************************")
basic_draw_testcase() #add custom deck cards into player1_cards and player2_cards
war.deal_test_cards(player1_cards,player2_cards)
war.start_game()