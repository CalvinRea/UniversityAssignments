card_values={"K":10,"Q":10,"J":10}
hand=[]
aces=0
value=0

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
		print("Blackjack!")
	else:
		print(hand[0]+1," or ",hand[0]+11)
	
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
		print("Bust!")
	elif(value_a!=value_b):
		print(value_a," or ",value_b)
	else:
		print(value_b)
		
		
		
		
		
		
		
		
		
		

