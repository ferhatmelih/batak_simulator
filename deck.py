# -*- coding: utf-8 -*-
import random
# dictionary for cars to numbers
card_types = {'spades':101,'hearts':102,'clubs':103,'diamonds':104}
card_numbers = {'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':11,'Q':12,'K':13,'1':14}

#inverse dictionary for printing  
inv_card_types = {'101':'Spades','102':'Hearts','103':'Clubs','104':'Diamonds'}
inv_card_numbers = {'2':'2','3':'3','4':'4','5':'5','6':'6','7':'7','8':'8','9':'9','10':'10','11':'Jack','12':'Queen','13':'King','14':'Ace'}

class Card:
	def __init__(self,card_type,card_number):
		self.type = card_types[card_type]
		self.number = card_numbers[card_number]

	def __str__(self):
		#override "print" for card class members
		write_output = inv_card_numbers[str(self.number)]+ " of " + inv_card_types[str(self.type)]
		return write_output

	def __eq__(self,other):
		#override "equal" method for card class members
		return self.type == other.type and self.number == other.number
	

class Deck:
  def __init__(self):
		self.allCards = []
		for card_number in card_numbers:
			for card_type in card_types:
				new_card = Card(card_type,card_number)
				self.allCards.append(new_card)
		self.mixedCards = []
		for i in range(52):
			current_index = random.randint(0, 51-i)
			self.mixedCards.append(self.allCards.pop(current_index))
		self.hands = [self.mixedCards[0:13], self.mixedCards[13:26],self.mixedCards[26:39],self.mixedCards[39:52]]

	#shuffle the deck if necesseary 
  def shuffle_cards(self):
  	mixedCards_f = []
  	for i in range(52):
  		current_index = random.randint(0, 51-i)
  		mixedCards_f.append(self.mixedCards.pop(current_index))
  	self.mixedCards=mixedCards_f
  	self.hands = [self.mixedCards[0:12],self.mixedCards[13:25],self.mixedCards[26:38],self.mixedCards[39:51]]
  def is_Split_Faire(self,hands_in):
  	for hand in hands_in:
  		existBig=False
  		for card in hand:
  			if card.number>10:
  				existBig=True
  		if existBig:
  			pass
  		else:
  			print ("*********** unfair hand ***************")
  			return False
  	return True

  def print_cards(self,cards,*args):
    if len(args)>0:
      print args[0],
    for card in cards:
      print card,",",
    print " "

  def print_hands(self):
  	numHand=0
  	for hand in self.hands:
  		numHand += 1 
  		for card in hand:
  			print "Hand ", numHand, " has ",card





""" TEST AREA """
sAce = Card('spades','1')
s2 = Card('spades','2')
s3 = Card('spades','3')
s4 = Card('spades','4')
s5 = Card('spades','5')
s6 = Card('spades','6')

dAce = Card('diamonds','1')
d2 = Card('diamonds','2')
d3 = Card('diamonds','3')
d4 = Card('diamonds','4')
d5 = Card('diamonds','5')
d6 = Card('diamonds','6')

hAce = Card('hearts','1')
h2 = Card('hearts','2')
h3 = Card('hearts','3')
h4 = Card('hearts','4')
h5 = Card('hearts','5')
h6 = Card('hearts','6')

cAce= Card('clubs','1')
c2 = Card('clubs','2')
c3 = Card('clubs','3')
c4 = Card('clubs','4')
c5= Card('clubs','5')
c6= Card('clubs','6')





#deck = Deck()

	
#for i in range(52):
# print deck.mixedCards[i]
#print len(deck.allCards)
