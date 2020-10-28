import random as r

start_game = input('\n\tDo you want to play blot? -') 
if start_game == '\n\tYes':
	print('\n\tBeginning of game,good luck !')
elif start_game == '\n\tNo':
	print('Exiting the game,See you soon !')



suits = ['Diamonds-♦','Hearts-♥','Spades-♠','Clubs-♣'] * 4 
numbs = ['7','8','9','10','Jack','Lady','King','Ace'] * 4 
for i in suits:
	for j in numbs:
		pack = i + j 
# r.shuffle(suits)
# r.shuffle(numbs)
print(pack)


