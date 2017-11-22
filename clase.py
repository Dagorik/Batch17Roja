class Auto:
	def __init__(self,nombre_cons,color,motor):
		self.nombre = nombre_cons
		self.color = color
		self.ruedas = "4"
		self.motor = motor
		print("CREANDO UN AUTO NUEVO")

	def arranca(self):
		print("RUUUUUNN el " + self.nombre)

	def frena(self):
		print("FRENANDO el " + self.nombre)

	def get_color(self):
		print(self.color)

	def set_color(self,new_color):
		self.color = new_color

