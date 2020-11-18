class Armenia:
	def capital(self):
		print('Yerevan is the capital of Armenia')

	def language(self):
		print('Armenian is the state language')

class France:
	def capital(self):
		print('Paris is the capital of France')

	def language(self):
		print('France is the state language')

desc_am = Armenia()
desc_fr = France()

for desc in (desc_am, desc_fr):
	desc.capital()
	desc.language()
