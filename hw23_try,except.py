def plus(x,y):
	return ('your answer:'+ str(x + y))


def minus(x,y):
	return x - y

def multiply(x,y):
	return x * y

def devision(x,y):
	try:
		x / 0
	except ZeroDivisionError:
		print('Not dev by zero')
	else:
		x / y 


def exponentiation(x,y):
	return x ** y


def result():
	choice = int(input('Enter a num: '))
	num1 = input('\n+,-,/,* \n\tEnter a operator: ')
	choice1 = int(input('Enter a num: '))
	if num1 == '+':
		print(plus(choice,choice1))
	elif num1 == '-':
		print(minus(choice,choice1))
	elif num1 == '*':
		print(multiply(choice,choice1))
	elif num1 == '/':
		print(devision(choice,choice1))
	elif num1 == '**':
		print(exponentiation(choice,choice1)

result()
