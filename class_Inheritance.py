class Country:
	''' Общая модель страны'''
	def __init__(self,capital,population):
		self.capital = capital
		self.population = population
		'''Описание'''
	def description(self):
		full_description = f"{self.capital} {self.population}"
		return full_description.title()


class Armenia(Country):
	'''Модель страны - Армения'''
	def __init__(self,capital,population,nationality):
		super().__init__(capital,population)
		self.nationality = nationality

	def res_Armenia(self):
		full_description_am = f"The capital - {self.capital}, population - {self.population}, nationality - {self.nationality}"
		return full_description_am.upper()

res = Armenia('Yerevan','3 million','armenians')
print(res.res_Armenia())


class France(Country):
	'''Модель страны - Франция'''
	def __init__(self,capital,population,nationality,president):
		super().__init__(capital,population)
		self.nationality = nationality
		self.president = president

	def res_France(self):
		full_description_fr = f"The capital - {self.capital}, population - {self.population}, nationality - {self.nationality}, president - {self.president}"
		return full_description_fr.upper()

res = France('Paris','65 million','french','Emmanuel Macron')
print(res.res_France())

