fridge_banana = input('Есть ли бананы ? ') == 'y'
fridge_orange  = input('Есть ли апельсины ? ') == 'y'
fridge_apple  =  input('Есть ли яблоки ? ') == 'y'
result_fruit = not fridge_banana and fridge_orange and fridge_apple

print('Нужно купить бананы ',result_fruit)


light = input('Есть ли у вас свет ? ') =='y'
result_light = not light

print('Света нет, нужно достать бананы ',result_light)


result_all = result_light or result_fruit

print(result_all)



