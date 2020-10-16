# Создание запроса.
your_name = input('What is your name? ') # input - ввод данных с клавиатуры.
your_age = int(input('How old are you? ')) # преобразование типа str в тип int.

print('My name is:',your_name, 'I am:',your_age) # вывод данных.


# Перевод строк с исп. служебного символа (\n).
about_Python = ("\nPython is very strong... and fast;\nplays well with others;\nworks everywhere; friendly and easy to learn")

print(about_Python)


# Перевод строк с исп. ''' '''.
about_Python2 = '''Python is very strong... and fast; 
plays well with others;
works everywhere; friendly and easy to learn
'''

print(about_Python2)


# \n - новая строка, \t - вертикальный отступ сверху.
print("Hello \n\t World!")