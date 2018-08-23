# -*- coding: utf-8 -*-

#TODO: best estimate of "numTender"
#TODO: obligatory tenderer turn etc ???not sure if effective???
from deck import Deck 
from deck import Card 
import random
import pdb


deck_test = Deck()

class BatakEssiz(object):
	""" kwargs = {'hands': hands, 'starter_player': 0}  """
	def __init__(self, **kwargs):
		super(BatakEssiz, self).__init__()
		self.debug = kwargs['debug']
		self.hands =  kwargs['hands']
		self.starterPlayer = kwargs['starterPlayer']
		self.tender = kwargs['tender']
		#card types are identified with 101,102,103,104 
		self.trump = kwargs['trump']

		self.didTrumpAppear = 0
		self.numCardsToBePlayed = 4 
		self.playGround = []
		self.whosTurn = self.starterPlayer
		self.whoStartedRound = self.whosTurn
		self.playedOutHands = [[],[],[],[]]
		self.scoreTable = [0,0,0,0]
		self.possibleMoves = [ card_p for card_p in self.hands[self.whosTurn] if(card_p.type != self.trump) ]
		#gameState[0]:tender
		#gameState[1]:trump
		#gameState[2]:numCards to play on one turn
		#gameState[3]:playgroundCards
		#gameState[4]:current player's cards, hand
		#gameState[5]:didTrumpAppear if a trump is seen on playground in game history
		self.gameState = [self.tender,self.trump,self.numCardsToBePlayed,self.playGround,self.hands[self.whosTurn],self.didTrumpAppear]

		self.restGameData = [self.whosTurn,self.playedOutHands]



	def start_game(self):
		#initialize game.
		#check for card splitting rules
		#create Log for new game to be played
		#outputs initial game state
		pass

	def player_move(self,gameState,restGameData,legalMoves):
		# One player gets the current game state, his state
		# gets the possible moves from the gameState
		# returns a "move"
		#starts by random choosing bt available choices

		playerMove = legalMoves[ random.randint(0, (len(legalMoves)-1) ) ]

		return playerMove


	def next_state(self,gameState,restGameData,playerMove):
		#gets gameState and applies the move to the gameState
		#makes a record of the game play
		#keeps tables
		#returns the gameState

		self.playGround.append(playerMove)
		#print "old hand: ",deck_test.print_cards( self.hands[self.whosTurn])
		#print "player move: ",playerMove
		self.hands[self.whosTurn].remove(playerMove)
		#print "new hand",deck_test.print_cards( self.hands[self.whosTurn])

		if not(self.didTrumpAppear) and playerMove.type==self.trump:
			self.didTrumpAppear = 1

		if len(self.playGround)==4:
			self.decide_round_winner()
		else:
			self.whosTurn = (self.whosTurn + 1)%4

		self.update_game_state()
		pass

	def decide_round_winner(self):
		starterPlayer = self.whoStartedRound
		playGround = self.playGround
		trumpCardsInPG = [ card_p for card_p in playGround if(card_p.type == self.trump) ]
		#if trump cards exists on playGround
		if len(trumpCardsInPG)>0:
			pgSorted = sorted(trumpCardsInPG, key=lambda x: (x.number), reverse=True)
			biggestCardOnPG = pgSorted[0]
		#if no trump in pGround
		else:
			firstCard = playGround[0]
			firstCardTypesOnPG = [ card_p for card_p in playGround if(card_p.type == firstCard.type) ]
			firstCardTypesOnPG_sorted = sorted(firstCardTypesOnPG, key=lambda x: (x.number), reverse=True)
			biggestCardOnPG = firstCardTypesOnPG_sorted[0]



		index_winner = playGround.index(biggestCardOnPG)
		winner = (index_winner + starterPlayer)%4
		self.scoreTable[winner] += 1
		self.whoStartedRound = winner
		self.whosTurn = winner
		self.playGround = []
		self.numCardsToBePlayed = 4
		self.update_game_state()

	def update_game_state(self):
		self.gameState = [self.tender,self.trump,self.numCardsToBePlayed,self.playGround,self.hands[self.whosTurn],self.didTrumpAppear]
		pass



	def legal_moves(self,gameState,restGameData):
		# gets the gameState and decides on what to be played
		#in Batak, there is no need to keep the history record to know the legal moves
		#this outputs a set of legal moves

		#if first to play on playground
			#if trump has not appeared,
				#all cards except trumps are allowed are legal
			#else if: trump appeared, 
				#ALL CARDS in hand are legal

		#if not first, 
			#if the same type as the "first on playground(FOP)" exists
			 # if cards bigger than FOP available
				 # all cards, same type and bigger are available
			 #else if: no bigger
				 # bigger cards
			#else if: same type as FOP does not exist
				#if trump exists
						#if trump cards on playground
							#trump cards bigger than pGround are OK
						#else if: no trump cards on pGround
							#all trump cards available
				#else if: trump does not exist
					#everything possible, all mean loose

		
		
		#check if no cards on pGround		
		hand = gameState[4]	
		playGround = gameState[3]
		trump = gameState[1]
		trumpCardsInHand = [ card_p for card_p in hand if(card_p.type == trump) ]
		didTrumpAppear = gameState[5]

		#FIRS TO PLAY
		if len(playGround) == 0:

			#check if trump appeared before
				if self.debug:
					print "first to play"
				if didTrumpAppear:
						#all cards in hand
						legalMoves = hand
				else:
					#all except trump
					legalMoves = [ card_p for card_p in hand if(card_p.type != trump) ]

					#in case only trump cards remain in hand, and no trump cards have appeared
					if len(legalMoves) == 0:
						legalMoves = hand


	  #NOT FIRST TO PLAY
		else:
				if self.debug:
					print "not first to play"
				firstCard = gameState[3][0]
				#sort playground cards
				sameKindCards = [ cardSameKind for cardSameKind in hand if(cardSameKind.type == firstCard.type) ]

				#NO SAME KIND
				if len(sameKindCards) == 0:
					if self.debug:
						print "no same kind"
					#NO TRUMP IN HAND
					if len(trumpCardsInHand) == 0:
						#all cards are possbile
						legalMoves = hand

					#TRUMP IN HAND
					else:
						if self.debug:
							print "but trump in hand"
						trumpsInPlayGround = [trump_card for trump_card in sorted(playGround, key=lambda x: (x.type,x.number), reverse=True) if (trump_card.type == trump) ]
					#NO TRUMP IN playgound, NO SAME KIND
						if len(trumpsInPlayGround) == 0:
							#any trump card is OK
							legalMoves = trumpCardsInHand

						#TRUMP ON playground, NO SAME KIND
						else:
							biggestTrumpOnPG = trumpsInPlayGround[0]
							trumpCardsInHandBigger = [bigger_card for bigger_card in trumpCardsInHand if bigger_card.number>biggestTrumpOnPG.number]
							#BIGGER TRUMP THAN ANY ON PG, NO SAME KIND
							if len(trumpCardsInHandBigger) > 0:
								#bigger than biggest trump is OK
								legalMoves = trumpCardsInHandBigger
							#NO BIGGER TRUMP, NO SAME KIND
							else:
								#all trump cards
								legalMoves = trumpCardsInHand

				#SAME KIND exists in HAND
				else:
					if self.debug:
						print "samekind exists in hand"
					#firstCardTypes on playground
					firstCardTypesOnPG = [ card_p for card_p in playGround if(card_p.type == firstCard.type) ]

					firstCardTypesOnPG_sorted = sorted(firstCardTypesOnPG, key=lambda x: (x.type,x.number), reverse=True)
					#biggest of the playground cards 

					biggestCardOnPG = firstCardTypesOnPG_sorted[0]
					#cards 
					sameKindCardsBigger = [bigger_card for bigger_card in hand if (bigger_card.number>biggestCardOnPG.number) and (biggestCardOnPG.type ==bigger_card.type)   ]
					#NO BIGGER CARD
					if len(sameKindCardsBigger) == 0:
						if self.debug:
							print "no same kind bigger_card "
						#if no bigger exists but trump cards exists, trump should be used
						if len(trumpCardsInHand) == 0:
							legalMoves = sameKindCards
						else:
							legalMoves = trumpCardsInHand

					#BIGGER CARDS
					else:
						# if bigger cards available, they are the legal moves
						legalMoves=sameKindCardsBigger
		if len(legalMoves)== 0:
			print "error"
			pdb.set_trace()

		return legalMoves

#hand_sorted = sorted(hand1, key=lambda x: (x.type,x.number), reverse=True)




		
	def decider_on_winner(self,gameState,restGameData):
		#when there are no cards left
		#this function is called to decide the winnder
		#makes result tables and stores them 
		pass

	def __str__(self):
		#return gameState as a string
		print(" ************* GAME STATE ************")
		print "Round Number", 13-len( self.gameState[4] )
		print "whosTurn:", self.whosTurn,"th Player"
		print "tender is: ", self.gameState[0]
		print "trump is: ", self.gameState[1]
		print "cardsOnPlayground are: ", self.gameState[3]
		print "currentPlayerCards are: "
		for card in self.gameState[4]:
			print card, ",",
		print " "
		#print "possbile moves are: "
		#for card in self.restGameData:
		#	print card, ",",
		#print " "	
		return " --------------- GAME PRINTED ----------------- "




""" ***TR to EN dictionary*** 
yer: "playgroung"
el: hand
ihale: tender
ihaleyi alan: tenderer
koz: trump
tur: round"""

""""gameState" should be hashable so to make comparing easier in monte carlo sims
"gameState" should include
	- cards on the playground
	- the length of the cards on the playground "numCardsToBePlayed" 
		this effects the gameState bc it makes a difference if somebody can play a higher card or not
	- cards on your hand
	- "isTenderer"
	- tender
	- the trump
	- the number of trumps on your hand
	- (later) previously used cards 
	- (later) remaning "koz" cards in the deck
	- (later) previously used cards matched to each player 

"legalMoves" is a list of cards

"move" is just one card


"gameState" is indep from whos turn it is as a player(0,1,2,3)
	therefore a seperate var should keep player turn
	call this var "whosTurn"

	also gameState is indep from which player has that certain deck, 
		so each player _hand_ should be kept seperately from the gameState

 $$$ if games take a long time to run, then a simple "gameState" can be assigned with taking feature vectors into account $$$

 """


""" 	***LIST OF ALL VARS ***
move [ a card]
whosTurn [ a number from 0-3]
legalMoves [a list of card]
hand [one hand of cards containing 13 cards in the beginning]
handList [a list of hands of each player, respevtively handList[0:3]]
numCardsToBePlayed [remaning num of cards to be added to the playground, 0 to 4 ]
tender [from 5 to 13, default is 5]
possibleMoves [card list]

gameState 
 - tender
 - trump
 - numCardsToBePlayed
 - cardsOnPlayground
 - hands[whosTurn] (hand of the current player)
 - didTrumpAppear

restGameData
 - whosTurn
 - playedOutHands
 - roundWins (each players' win number)
"""





