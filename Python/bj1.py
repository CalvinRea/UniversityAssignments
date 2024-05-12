card=input()
rank=card[0:len(card)-1]
card_values={"A":"1 or 11",
"K":10,
"Q":10,
"J":10
}

if rank in card_values.keys():
	print(card_values[rank])
else:
	print(rank)
