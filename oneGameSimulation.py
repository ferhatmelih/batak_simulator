# -*- coding: utf-8 -*-

"""
##########GAME#########
#1 initialize a random deck

#2 split the deck into 4 
  - check if applicable to game rules (all players should have at least one card bigger than 10)

#3 init starting vars
	- tender = 7
	- starter_player is 0
	- trump is spades

  taking "tender" input is postponed now and is given as 7 as default
  also, the tender is always the first player (won't effect the simulation results)

#4 start the game

#5 print out the first gameState
 - with the hand of 0 th player
 - 

#6 put a random card, by first player

#7 print out possible moves by next player 

# add cards by other players and finish a full round. 

# record round winner, change the starter

# 2nd round gameState print

# 3rd round

# 4th round


"""
 
from deck import *
from batakEssiz import BatakEssiz
import time

#1
deck = Deck()

#2 shuffle cards until each hand is "FAIR" (containing at least 1 card over 10)
hands = deck.hands
while ( not(deck.is_Split_Faire(hands)) ):
	deck.shuffle_cards()
	hands = deck.hands
	print("unfair devide, shuffled")

#3
input_vars = {'hands':hands,'starterPlayer':0,'tender':5,'trump':101,'debug':True}

#4
game = BatakEssiz(**input_vars)


#5
#print game


#6
print "hand nums at start",len(game.hands[0]),len(game.hands[1]),len(game.hands[2]),len(game.hands[3])
start_time = time.time()
for i in range(52):
	legalMoves = game.legal_moves(game.gameState,game.restGameData)
	playerMove = game.player_move(game.gameState,game.restGameData,legalMoves)
	game.next_state(game.gameState,game.restGameData,playerMove)
	deck.print_cards(game.gameState[3],"CARDS ON PG ",i,": ")
	print "hand nums at round",len(game.hands[0]),len(game.hands[1]),len(game.hands[2]),len(game.hands[3])




#print "hand nums at end",len(game.hands[0]),len(game.hands[1]),len(game.hands[2]),len(game.hands[3])

print game.scoreTable
print len(game.hands)
print "end_time:",time.time()-start_time













"""
print "before shuffle ",deck.hands[0][0]
deck.shuffle_cards()
print "after shuffle ", deck.hands[0][0]
"""


"""
card1 = Card('spades','1')
card2 = Card('diamonds','2')
card3 = Card('diamonds','2')
hand1 = [card1,card2,card3,5]
hand2 = [card2,card3,card1]
hand3 = [card1,card2,card3]
hand4 = [card1,card2,card3,5]
print hand1
print hand1 == hand3
"""

"""
hand = game.hands[0]
trump = 101
possibleMoves = [ card_p for card_p in hand if(card_p.type != trump) ]
print "possible moves: "
for card in possibleMoves:
 print card
print len(possibleMoves)
"""

"""
hand1 = game.hands[0]
handSorted = sorted(hand1, key=lambda x: (x.type,x.number), reverse=True)
trumpCardsSorted = [trump_card for trump_card in sorted(hand1, key=lambda x: (x.type,x.number), reverse=True) if (trump_card.type == trump) ]
deck.print_cards(trumpCardsSorted)
"""

"""fakeGameState = game.gameState
		#gameState[0]:tender
		#gameState[1]:trump
		#gameState[2]:numCards to play on one turn
		#gameState[3]:playgroundCards
		#gameState[4]:current player's cards, hand
		#gameState[5]:didTrumpAppear if a trump is seen on playground in game history
playground = [d3,d5]
hand = [s2,sAce,s5,h2,h5,d4]
fakeGameState[3] = playground
fakeGameState[4] = hand 
fakeGameState[5] = 0
legalMoves = game.legal_moves(fakeGameState,game.restGameData)
"""


