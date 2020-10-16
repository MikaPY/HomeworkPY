# Vowels(гласные) = a,e,i,o,u
# Consonant(согласные) = b,c,d,f,g,h,j,k,l,m,n,p,q,r,s,t,v,w,x,y,z


alphabet = input("Input a letter of the alphabet - " ) # Исп. ввода из с клавиатуры.

if alphabet in 'a' 'e' 'i' 'o' 'u': # Если введенная буква из списка, то это гласная буква.
	print(" - This is a vowel letter " ) 
else: # Если нет, тогда это согласная буква.
	print(" - This is a consonant letter " ) 




num = int(input('\tEnter a num: ')) # Исп. ввода с клавиатурыю.
module = num % 2 # Деление по модулю.
if module > 0: # Остаток больше 0.
	print('\t\nOdd number ! ') 
else: 
	print('\t\nEven number ! ')





# 1 

year = int(input('Enter the year: '))
if year % 4 != 0:
	print('Обычный')
elif year % 100 == 0:
	if year % 400 == 0:
		print('Високосный')
	else:
		print('Обычный')
else:
	print('Високосный')


# 2 

year = int(input('Введите год: '))
if year % 400 == 0:
	print('Високосный год')
elif year % 100 == 0:
	print('Обычный год')
elif year % 4 == 0:
	print('Високосный год')
else: 
	print('Обычный год')





import random as r  # Импорт модуля  случайного числа.

bot_point = 0 # Куда будут собираться очки.
user_point = 0  # Куда будут собираться очки.


bot_John = r.randint(1, 3) # Исп. случайного числа от 1 до 3. 
user_Bob = int(input('Enter a num: ')) # Ввод с клавиатуры.

if bot_John == user_Bob: # Проверим одинаковы ли объёкты.
	user_point += 1 # Присвоим 1 очко.
else: # Если if не True, тогда
	bot_point += 1 # Присвоим 1 очко.


bot_Garry = r.randint(1,3)	
user_Paul = int(input('Enter a num: '))

if bot_Garry == user_Paul:
	user_point += 1
else:
	bot_point += 1


if bot_point < user_point: # Сравним у кого больше очков.
	print('You win !', bot_point, user_point)  # Если больше у юзера, то он выиграл.
elif bot_point > user_point: # Сравним у кого больше очков.
	print('You lost ! ') # Если больше у бота, то ты проиграл.
else: # Если не if и не elif, тогда
	print('Not winner') # Ничья.