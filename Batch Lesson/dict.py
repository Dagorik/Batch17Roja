diccionario = {'nombre':'Carlos','edad':22,'cursos':['Python','Flask']}
print(diccionario)
print(diccionario['nombre'])
print(diccionario['edad'])
print(diccionario['cursos'])

dic = dict(nombre='Nestro',apellido='Juarez',edad=22)
#print(dic['nombre'])
print("___________________________")
for key,value in diccionario.items():
	print(key + " : " + str(value))

print("___________________________")

#Devuelve el numero de elementos que tiene el diccionario.
print(len(diccionario))

#Devuelve una lista con las claves del diccionario.
print(diccionario.keys())

#Devuelve una lista con los valores del diccionario.
print(diccionario.values())

#Devuelve el valor del elemento con su clave, Y si no lo encuentra devuelve un valor por default
print(diccionario.get("nombree","JUANITO"))

#Inserta un elemento al diccionario con su clave:valor
diccionario['key'] = 'value'
print(diccionario)

#Elimina el elemento por la clave
diccionario.pop('key')
print(diccionario)

#Devuelbe la copia de un diccionario
diccionario2 = diccionario.copy()
print(diccionario2)

#Añade los elementos de un diccionario a otro
diccionario.update(dic)
print(diccionario)


