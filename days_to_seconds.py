class Converting:
	def __init__(self):
		self.days = 1 
		self.hours = 24
		self.minutes = 60
		self.seconds = 60

	def convert(self):
		res = self.days * self.hours * self.minutes * self.seconds 
		return f"In one day {res} seconds." 


result = Converting()
print(result.convert())
		
