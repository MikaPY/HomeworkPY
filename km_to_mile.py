class Conversion:
	def __init__(self,km):
		self.km = km
		self.ratio = 0.621371

	def convert(self):
		return self.km * self.ratio
		

res = Conversion(10)
print(res.convert())