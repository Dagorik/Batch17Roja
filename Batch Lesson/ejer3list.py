lista = []
entrada = int(input('Cuantas palabras tiene la lista? '))

for x in range(1,entrada+1):
	valor = input('Ingresa la palabra numero ' + str(x))
	lista.append(valor)
print(lista)

palabra_a_buscar = input("¿Qué palabra quiere buscar?: ")
palabra_que_sustituye = input("¿Con qué palabra quiere sustituir?: ")

for palabra in lista:
    if palabra == palabra_a_buscar:
        indice = lista.index(palabra) 
        lista[indice] = palabra_que_sustituye
print("La lista actual es: ", lista)