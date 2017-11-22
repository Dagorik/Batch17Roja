from Perro import Perro
from Pajaro import Pajaro

perrito = Perro("FIDO","CAFE","LABRADOR","3")

comiendo_perrito = perrito.comer()
ladrar = perrito.ladra()
color = perrito.get_color()
print(comiendo_perrito)
print(ladrar)
print(color)

pajarito = Pajaro("ROJO","CARPINTERO","MEDIANO")
comiendo_pajarito = pajarito.comer()
piar = pajarito.pia()
color = pajarito.get_color()
print(comiendo_pajarito)
print(piar)
print(color)

def jauria(Animal):
	return Animal.comer()

print(jauria(perrito))