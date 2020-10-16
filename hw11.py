# Create a Python program to open the password,
# having two chances. What happens if the password is incorre.

key = 9190
chance = 0
storage = 0

while chance <= 2:
	storage = int(input('\n\tEnter a 4 digit key - '))
	chance = chance + 1

	if storage == key:
		print('\n\tKey is correct ! ')
		break

	if storage != key:
		print('\n\tKey is not correct !')

	if chance == 2:
		print('\n\tLocked ! ')
		break
