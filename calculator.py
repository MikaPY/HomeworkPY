def plus(x,y):
	return ('your answer:'+ str(x + y)) # for addition


def minus(x,y): # for subtraction
	return x - y


def multiply(x,y): # for multiplication
	return x * y

def devision(x,y): # for division
	return x / y 


# 	try:
# 		res = x / y
# 	except ZeroDivisionError:
# 		print('Not divisible by zero')
# 		res = 0
# print(res)


# def devision(x,y):
# 	try:
# 		x / 0
# 	except ZeroDivisionError:
# 		print('Not dev by zero')
# 	else:
# 		x / y 

def exponentiation(x,y): # for square root 
	return  x**(1./y)

def result():
	choice = float(input('Enter a num: ')) # for user
	num1 = input('\n+,-,/,*,x \n\tEnter a operator: ') # for user
	choice1 = float(input('Enter a num: ')) # for user 
	while True:
		try:
			res = choice / choice1 
		except: ZeroDivisionError:
			print('Not divisible by zero')
			res = 0
	# print(res)
	

	if num1 == '+':
		print(plus(choice,choice1))
	elif num1 == '-':
		print(minus(choice,choice1))-
	elif num1 == '*':
		print(multiply(choice,choice1))
	elif num1 == '/':
		print(devision(choice,choice1,res))
	elif num1 == 'x':
		print(exponentiation(choice,choice1)

result()







