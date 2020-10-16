# legar variables

car = 'Alfa Romeo'
horse_power = 240
name = 'Mikael'
lastname = "Saribekyan"
sur_name = "Mkrtchyan"
cars = 100 # шт.
drivers = 30 # шт.
average_passengers_per_car = 5 # шт.
space_in_a_car = 4.0 # шт.
my_height = 177 # см
my_weight = 66 # кг
my_eyes = "Brown" # цвет
my_hair = "Black" # цвет волос
my_teeth = "White" # цвет зубов 
theorem = "Theorem of mathematical logic on natural numbers"
hilarious = 'Clown'
days = "Пн Вт Ср Чт Пт Сб Вс" # дни недели 
athos = "Musketeer" # персона 
cheese_and_crackers = "Food"
poem = ''' 
\tДля счастья мне совсем немного надо.
Хочу тебя \n я нежно обнимать.
Хочу всегда 
я быть с тобою рядом
\n\t\tи никогда не отступать!
'''


# Type checking

num_1 = 150 # integer (целое чилсо)
print(type(num_1))

num_2 = "Text" # string (строка)
print(type(num_2))

num_3 = "14.9" # float (число с плавающей точкой)
print(type(num_3))

num_4 = True
num_5 = False
print(type(num_4))
print(tupe(num_5))


#File size

a = (5, 6 , 7, 10, 12) # tuple весит меньше 
b = [5, 6, 7, 10, 12] # list весит больше 
a.__sizeof__() 
b.__sizeof__() 


# area of a rectangle.

sideA = int(input("Enter num")) # см
sideB = int(input("Enter second num")) # см 
areaS =  (sideA * sideB)
print(areaS)


# area of a square

square = int(input("Enter num"))
area = (square ** 2)
print(area)

