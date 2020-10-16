# Есть ли фрукты в холодильнике ? Нет
fridge_fruit_banana = input('Есть ли у тебя бананы ? ') == 'no'
fridge_fruit_orange = input('Есть ли у тебя апельсины ? ') == 'no'
fridge_fruit_apple = input('Есть ли у тебя яблоки ? ') == 'no'
result_fridge = not fridge_fruit_banana and not fridge_fruit_orange and not fridge_fruit_apple

print(result_fridge)


# Фруктов нет, нужно их купить ? Да
market_banana = input('Нужно купить бананы ? ') == 'yes'
market_orange = input('Нужно купить апельсины ? ') == 'yes'
market_apple = input('Нужно купить яблоки ? ') == 'yes'
result_market = market_banana and market_orange and market_apple

print(result_market)


# Фрукты куплены, но нет света, нужно их достать.
house_light = input('В твоем доме есть свет ? ') == 'no'
result_house = not house_light and result_fridge

print('Вынь фрукты',house_light)