from Animal import Animal

class Pajaro(Animal):
	def __init__(self,color,tipo,tamano):
		self.tipo = tipo
		self.tamano = tamano
		self.color = color
	
	def pia(self):
		return "PIO PIO"

	def vuela(self):
		return "VOLANDO"
