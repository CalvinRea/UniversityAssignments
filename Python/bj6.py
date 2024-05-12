"""
File:   blackjack.py
Author: Steve James <steven.james@wits.ac.za>
"""


"""
Complete the functions below. You may include any additional functions you like
"""


def output_score(hand):
	card_values={"K":10,"Q":10,"J":10}
	y=hand
	hand=[]
	aces=0
	value=0

	for x in y:
		value=0
		rank=x[0:len(x)-1]
		if rank in card_values.keys():
			value = card_values[rank]
			hand.append(value)
		elif rank=="A":
			aces+=1
		else:
			value = int(rank)
			hand.append(value)

	value=0

	if(len(hand)==1 and aces==1):
		#bj possible
		if(hand[0]==10):
			return"Blackjack!"
		else:
			return str(hand[0]+1)+" or "+str(hand[0]+11)
		
	else:
		
		for card in hand:
			if(value>21):
				break
			value+=card
			
		value_a=value
		value_b=value
		
		for i in range(aces):
			if(value_b>21):
				break
				
			if(value_b<=11-aces):
				#ace can be valued at 11
				value_b+=11
				
			else:
				value_b+=1
		
		for i in range(aces):
			if(value_a>21):
				break
			value_a+=1
		
		
		if(value_b>21):
			return "Bust!"
		elif(value_a!=value_b):
			return str(value_a)+" or "+str(value_b)
		else:
			return str(value_b)
 

def is_blackjack(hand):
	bj=False
	if(len(hand)==2):
		bj=output_score(hand)=="Blackjack!"
	return bj

def is_bust(hand):
	bust=output_score(hand)=="Bust!"
	return bust


def get_high_score(hand):
	card_values={"K":10,"Q":10,"J":10}
	y=[]
	if(type(hand)==type(y)):
		y=hand
	else:
		y.append(hand)
	hand=[]
	aces=0
	value=0
	for x in y:
		value=0
		rank=x[0:len(x)-1]
		if rank in card_values.keys():
			value = card_values[rank]
			hand.append(value)
		elif rank=="A":
			aces+=1
		else:
			value = int(rank)
			hand.append(value)

	value=0

	for card in hand:
		value+=card
		
	for i in range(aces):
		if(value<=11-aces):
			#ace can be valued at 11
			value+=11
		else:
			value+=1
	return value
    

def get_advice(player_hand, dealer_hand):
#adjust for random amount of cards in player hand
	value=get_high_score(player_hand)
	dealer_val=get_high_score(dealer_hand)
	ace=False
	
	for x in player_hand:
		if (x[0:len(x)-1]=="A"):
			ace=True
			break
	
	if(ace):
		#has usable ace
		
		listy=["Hit Hit Hit Hit Hit Hit Hit Hit Hit Hit"
		,"Hit Hit Hit Hit Hit Hit Hit Hit Hit Hit"
		,"Hit Hit Hit Hit Hit Hit Hit Hit Hit Hit"
		,"Hit Hit Hit Hit Hit Hit Hit Hit Hit Hit"
		,"Hit Hit Hit Hit Hit Hit Hit Hit Hit Hit"
		,"Hit Hit Hit Hit Hit Hit Hit Hit Hit Hit"
		,"Stand Stand Stand Stand Stand Stand Stand Hit Hit Hit"
		,"Stand Stand Stand Stand Stand Stand Stand Stand Stand Stand"]
			
		table=[]
		for i in listy:
			table.append(i.split(" "))

		if(value>19):
			value=19
		value-=12
		dealer_val-=2
		return table[value][dealer_val]
	
	else:

		if(value>17):
			value=17
		if(8>=value and value>=4):
			value=8
			
		listy=["Hit Hit Hit Hit Hit Hit Hit Hit Hit Hit"
		,"Hit Hit Hit Hit Hit Hit Hit Hit Hit Hit"
		,"Hit Hit Hit Hit Hit Hit Hit Hit Hit Hit"
		,"Hit Hit Hit Hit Hit Hit Hit Hit Hit Hit"
		,"Hit Hit Stand Stand Stand Hit Hit Hit Hit Hit"
		,"Stand Stand Stand Stand Stand Hit Hit Hit Hit Hit"
		,"Stand Stand Stand Stand Stand Hit Hit Hit Hit Hit"
		,"Stand Stand Stand Stand Stand Hit Hit Hit Hit Hit"
		,"Stand Stand Stand Stand Stand Hit Hit Hit Hit Hit"
		,"Stand Stand Stand Stand Stand Stand Stand Stand Stand Stand"]
		
		table=[]
		for i in listy:
			table.append(i.split(" "))
		
		value-=8
		dealer_val-=2
		return table[value][dealer_val]

def get_winner(player_hand, dealer_hand):
	player=output_score(player_hand)
	dealer=output_score(dealer_hand)

	if(player==dealer):
		return"Push!"
	elif(dealer=="Bust!" or player=="Blackjack!"):
		return"Player wins!"	
	elif(player=="Bust!" or dealer=="Blackjack!"):
		return"Dealer wins!"
	elif(player>dealer):
		return"Player wins!"
	else:
		return"Dealer wins!"


"""
Do not modify any code below this comment!
"""

import random


class Deck:

    def __init__(self):
        self._cards = list()
        self._rng = random.Random(42)
        self.reset()

    def _rank_to_string(self, rank):
        special = {
            1: 'A',
            11: 'J',
            12: 'Q',
            13: 'K'
        }
        return special.get(rank, str(rank))

    def reset(self):
        self._cards.clear()
        for rank in range(1, 14):
            r = self._rank_to_string(rank)
            for suit in ['h', 'c', 's', 'd']:
                self._cards.append(r + suit)
        self._rng.shuffle(self._cards)

    def draw(self):
        return self._cards.pop()



def get_input(message, legal_options):
    while True:
        print(message, end='')
        option = input()
        if len(option) == 0:
            continue
        option = option[0].upper()
        if option in legal_options:
            return option
        else:
            print("Invalid input '{}'".format(option))


def hand_to_string(hand):
    return '{} -> {}'.format(
        ' '.join(hand),
        output_score(hand)
    )


def play_round(deck):
    player_hand = list()
    dealer_hand = list()
    deck.reset()

    dealer_hand.append(deck.draw())
    player_hand.append(deck.draw())
    player_hand.append(deck.draw())

    print('Dealer shows {}'.format(hand_to_string(dealer_hand)))
    print('Player shows {}'.format(hand_to_string(player_hand)))
    if is_blackjack(player_hand):
        print('Player wins!')
        return

    # Player's turn
    playing = True
    while playing and not is_bust(player_hand):
        action = get_input('(H)it, (S)tand, or (A)dvice? ', {'H', 'S', 'A'})
        if action == 'H':
            player_hand.append(deck.draw())
            print('Player shows {}'.format(hand_to_string(player_hand)))
        elif action == 'S':
            playing = False
        else:
            print('Advice: {}'.format(get_advice(player_hand, dealer_hand[0])))

    if playing:
        # player must be bust
        print('Dealer wins!')
        return

    # dealer's turn
    while not is_bust(dealer_hand) and get_high_score(dealer_hand) < 17:
        dealer_hand.append(deck.draw())
        print('Dealer shows {}'.format(hand_to_string(dealer_hand)))

    print(get_winner(player_hand, dealer_hand))


if __name__ == '__main__':

    running = True
    deck = Deck()
    while running:
        option = get_input('(N)ew round or (Q)uit? ', {'N', 'Q'})
        if option == 'N':
            play_round(deck)
            print('******************************************')
        elif option == 'Q':
            running = False
