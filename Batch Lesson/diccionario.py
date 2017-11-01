diccionario = {'nombre' : 'Carlos', 'edad' : 22, 'cursos': ['Python','JavaScript'] }
print(diccionario)
print (diccionario['nombre']) #Carlos
print (diccionario['edad'])#22
print (diccionario['cursos']) #['Python','Django','JavaScript']


dic =  dict(nombre='nestor', apellido='Plasencia', edad=22)

print(dic)


for key,value in diccionario.items():
	print(key + " " + str(value))