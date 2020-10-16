# Create a program that uses the two input()
# functions, and the weight and height parameters 
# for calculating the body mass index.

weight = int(input("Enter your weight: "))
height = float(input("Enter yuor height: "))
bmi = weight/(height * height)

print(bmi)



# Convert units: square meter [m2] to hectare [ha] 
# using the input () function and do the same thing 
# the other way around.

hectare = float(input("Enter the number to count: "))
square_meter = 10.000
count = hectare * square_meter

print(count)


#Узнать расход топлива.

fuel_tank = float(input("What is the tank capacity?- "))
dstance = float(input("How far do you want to go?- "))
passed_way = 100
res = fuel_tank / distance * 100

print(res)

print(round(res,'liters per 100 kilometers'))


# Узнать дистанцию.

fuel_tank = int(input("What is the tank capacity? - "))
fuel_consumption = float(input("What is the fuel consumption? - "))
cycles_of_km = fuel_tank / fuel_consumption
distance_km = cycles_of_km * 100
distance_m = distance_km * 1000

print(distance_m)


# Супермаркет.

price = float(input("Enter the price: "))
cost = float(input("Enter the cost: "))
income =(float(input('Enter the income: ')))
remains = price - cost 
result = remains + income / 20

print(remains,'- Your cost')
print(result,'%','- Your income')


# ATM

refill = float(input("Пополите ваш баланс - "))
result = refill * 5 / 100

print(result)


# Pound & kg

pound = float(input("Enter a num: "))
kg = 2.2046 # 1 фунт = 2.2046 кг.
result = pound / kg

print(result,'kg')
print(round(result))


# Mile and km
mile = float(input("Enter a num: "))
km = 1.609
result = mile * km # 1 миля = 1.609 км

print(result)