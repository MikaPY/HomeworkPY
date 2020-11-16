class Person():
	'''Описание человека.'''
	def __init__(self,name,lastname,age,work):
		self.name = name
		self.lastname = lastname
		self.age = age
		self.work = work

	def desc(self):
		full_description = f"My name is {self.name} {self.lastname} and i am {self.age} years old,I work as {self.work}."
		return full_description.upper()

i_am = Person('Mikael','Saribekyan',25,'programmer')

print(i_am.desc())