# # Нахождение через import math.

# import math 
# res = math.factorial(2)

# print(res)




# # Нахождение в ручную через формулу.

# n = 5 
# factorial  = 1*2*3*4*n
# print(factorial)


# street = 'St. Mark’s Place Fulton Street Park Avenue Lafayette Avenue' 
# price = '95k$ 78k$ 84k$ 100k$' 

# ent_str = input('Choose a street ? ') == street
# ent_prc = input('Choose a price ? ') == pric


# res_all = ent_str in street and price in ent_prc

# print('Your choice',res_all)		 


street = 'Fulton Street Park Avenue'
price = '350 364'
ent_str = input('Choose a street ? ') 
ent_prc = input('Choose a price ? ')
res = ent_str in street  and  ent_prc in price 
print(res)
