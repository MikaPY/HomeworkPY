import random as r 
all_steps = [1,2,3,4,5,6,7,8,9]
steps = []
print('			    Hi, you play Tic Tac Toe')
print('')

def table():
	print('')
	print('')
	print('				',all_steps[0],' | ',all_steps[1],' | ',all_steps[2],' ')
	print('				 __    __   __')
	print('				',all_steps[3],' | ',all_steps[4],' | ',all_steps[5],'')
	print('				 __    __   __')
	print('				',all_steps[6],' | ',all_steps[7],' | ',all_steps[8],' ')
	print('')
	print('')


def player():
	while True:

		player_step = int(input('Enter a num: '))
		if player_step in range(1,10):
			if player_step not in steps:
				steps.append(player_step)
				result = player_step -1
				all_steps[result] = 'X'
				break

def bot():
	while True:
		botStep = r.randint(1,9)
		if botStep not in steps:
			steps.append(botStep)
			result = botStep -1 
			all_steps[result] = 'O'
			break


while True:
	table()
	player()
	table()
	bot()


		