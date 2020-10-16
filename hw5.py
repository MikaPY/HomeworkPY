# Импорт одного модуля.
import time 


# Импорт нескольких модулей.
import random, os 


# Импорт некоторых методов или же переменных.
from math import ceil # Импорт метода ceil


# Псевдонимы для модулей(сокращения).
import Template as tem # Обращение к модулю,как tem.


# Импорт из модуля math, pi и ceil
from math import pi, ceil as c 


# Модуль os для получения текущей директории.
import os 
os.getcwd()



# Импортирование из модуля math число pi.
from math import pi 
r = int(input("Enter a nun: "))
s = pi * r ** 2  
print(s)


# Импортирование созданного модуля.
from myModule import summ
print(summ)


Импорт модуля и добавление псевдонима.

from datetime import datetime as dt 
print(dt.now()) # Метод now. 


# Угадайка с рандоным числом.
from random import randint 
rand = randint(0, 20)
user_num = int(input("Введите число от 0 до 20: "))
while (user_num != rand):
	print("Вы не угадали! ")

	if user_num > rand: 
		print("Число,что вы пытайтесь угадать меньше. ")
	else:
		print("Число что вы пытайтесь угадать больше. ")
	user_num = int(input("Введите число от 0 до 20: "))
print("Вы угадали!")		


# Прикол
import this 


# функция sqrt импортируется из модуля math исп. ключевое слово from
from math import sqrt 