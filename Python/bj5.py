def hand_state():
	value=0
	card_values={"K":10,"Q":10,"J":10}
	hand=[]
	aces=0

	x=input()
	while(x!="end"):
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
		x=input()

	value=0
	if(len(hand)==1 and aces==1):
		#bj possible
		if(hand[0]==10):
			return "Blackjack!"
		else:
			return hand[0]+11
		
	else:
		
		for card in hand:
			if(value>21):
				break
			value+=card

		for i in range(aces):
			if(value>21):
				break
				
			if(value<=11-aces):
				#ace should be valued at 11
				value+=11
			else:
				value+=1
		
		if(value>21):
			return "Bust!"
		else:
			return value
			
player=hand_state()
dealer=hand_state()

if(player==dealer):
	print("Push!")
elif(dealer=="Bust!" or player=="Blackjack!"):
	print("Player wins!")	
elif(player=="Bust!" or dealer=="Blackjack!"):
	print("Dealer wins!")
elif(player>dealer):
	print("Player wins!")
else:
	print("Dealer wins!")

												












