diccionario = {'nombre' : 'Carlos', 'edad' : 22, 'cursos': ['Python','JavaScript'] }
print(diccionario)
print (diccionario['nombre']) #Carlos
print (diccionario['edad'])#22
print (diccionario['cursos']) #['Python','Django','JavaScript']


dic =  dict(nombre='nestor', apellido='Plasencia', edad=22)

print(dic)


for key,value in diccionario.items():
	print(key + " " + str(value))

# Devuelve el numero de elementos que tiene el diccionario
print(len(diccionario))

# Devuelve una lista con las claves del diccionario
print(diccionario.keys())


# Devuelve una lista con los valores del diccionario
print(diccionario.values())


# Devuelve el valor del elemento con clave key. Sino devuelve default
print(diccionario.get("nombree", "hola"))

# Insertamos un elemento en el diccionario con su clave:valor
diccionario['key'] = 'value'
print(diccionario)

# Eliminamos el elemento del diccionario con clave key
diccionario.pop('key')
print(diccionario)

# Devuleve la copia de un diccionario dict2 = dict.copy()
dict2 = diccionario.copy()
print(dict2)
print(diccionario)

# devuelve un lista de tuplas formadas por los pares clave:valor
print(diccionario.items())

# Añade los elementos de un diccionario a otro
diccionario.update(dic)
print(diccionario)

#diccionario.clear()
#print(diccionario)

print("----------------")
# Vemos cuantos elementos tiene nuestro diccionario
numElem = len(diccionario)
print("Numero de elementos del diccionario len(futbolistas) = %i" %numElem)

# Imprimimos una lista con las claves del diccionario
keys = diccionario.keys();
print ("Claves del diccionario futbolistas.keys(): \n%s" %keys)

# Imprimimos en una lista los valores del diccionario
values = diccionario.values()
print ("Valores del diccionario futbolistas.values(): \n%s" %values)


