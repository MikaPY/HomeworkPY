import random as r 


print('\n\tHi guyes you play 21 game') # Приветсвие 
player_choice = 'up' # Выбор для пользователя
result_choice = r.choice(player_choice) == 'u' #  
point = 0 

while True:
	if player_choice:
		if point >= 21:
			break
		player_choice = input('\n\tEnter a num (1,2,3)')

		if player_choice.isdigit():
			player_choice = int(player_choice)

			if 0 < player_choice < 4:
				print(point, '+',player_choice, '=', point + player_choice)
				point += player_choice
				if point >= 17:
					pc_choice = 20 - point
					player_choice = 1
					print('you lose', 21)
					break

				pc_choice = r.randint(1,3)
				print(point, '+',pc_choice, '=' ,point + pc_choice)
				point += pc_choice
			
			else:
				print('\n\tplease input (1-3)')	
		else:
			print('\n\tplease input number')
			
		



