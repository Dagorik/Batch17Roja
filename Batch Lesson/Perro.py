from Animal import Animal

class Perro(Animal):
	def __init__(self,nombre):
		self.nombre4 = nombre

	def ladrar(self):
		print("GUUAU")

	def get_name(self):
		print(self.nombre4)

	def set_name(self,new_name):
		self.nombre4 = new_name

'''
perrito = Perro("Fido")
perrito.ladrar()
perrito.comer()
perrito.set_name("FIRULAIS")
perrito.get_name()
'''