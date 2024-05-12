value=0
card_values={"A":0,"K":10,"Q":10,"J":10}
cards=[input(),input(),input()]#first is dealers
values=[]

for card in cards:
	value=0
	rank=card[0:len(card)-1]
	if rank in card_values.keys():
		value = card_values[rank]
	else:
		value = int(rank)
	values.append(value)
	
value=values[1]+values[2]
dealer_val=values[0]
if(values[0]==0):
	dealer_val+=11	
	
if(value==values[1] or value==values[2]):
	#has usable ace
	if(value==0):
		value=12
	else:
		value+=11
	
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
	print(table[value][dealer_val])
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
	print(table[value][dealer_val])
	
		
		
