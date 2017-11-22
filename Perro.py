from Animal import Animal

class Perro(Animal):
	def __init__(self,nombre,color,raza,edad):
		self.nombre = nombre
		self.color = color
		self.raza = raza
		self.edad = edad

	def ladra(self):		
		return "GUUAU"

	def mueve_cola(self):
		return "Mueve la cola"
