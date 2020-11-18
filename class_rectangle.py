class Rectangle:
	'''Модель прямоугольника'''
	def __init__(self,width,lendth):
		self.width = width
		self.lendth = lendth

	def area(self):
		return self.width * self.lendth


rectangle_area = Rectangle(5,8)

print(rectangle_area.area())
