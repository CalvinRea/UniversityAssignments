value=0
ace=False
fc_values={"A":0,"K":10,"Q":10,"J":10}
cards=[input(),input()]
values=[]

for card in cards:
	value=0
	rank=card[0:len(card)-1]
	if rank in fc_values.keys():
		value = fc_values[rank]
	else:
		value = int(rank)
	values.append(value)	

value=values[0]+values[1]
if(value==0):
	print("2 or 12")
elif(value==values[0] or value==values[1]):
	if(11+value==21):
		print("Blackjack!")
	else:
		a=str(11+value)
		b=str(1+value)
		print(b+" or "+a)
else:
	print(value)
		
