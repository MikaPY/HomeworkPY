class Car():
	'''Простая модель автомобиля.'''
	def __init__(self,make,model,year):
		self.make = make 
		self.model = model
		self.year = year

	def description(self):
		full_description = f"{self.year} {self.make} {self.model}"
		return full_description.title()

buy_a_car = Car('bmw','x5',2020)

print(buy_a_car.description())