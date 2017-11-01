'''
var = "HOLA"

#[H,O,L,A]

for i in var:
	print(i)

print("ACABE")



print('Multiplo de dos "contador" ')
cuenta = 0
for i in range(1,100):
	if i % 2 == 0:
		cuenta = cuenta + 1

print(cuenta)


print("Acumulador")
suma = 0
for i in range(0,5):
	print(i)
	suma = suma + i

print("Resultado: ", suma)


elefante = "ELEFANTE"
counter = 0
eCounter = 0
for i in elefante:
    counter = counter + 1
    if i == "E":
        eCounter = eCounter + 1
    if eCounter == 3:
        print ("encontré la tercera ‘E’ en la posición", counter)

'''

precio = 300
print("El precio del articulo 'x' es de ", precio)
cantidad = int(input("Indique la cantidad del articulo 'x' que desea \n"))
if cantidad > 5: 
	calculo = (precio * cantidad) *.95
	print("El total de tu compra es " ,calculo)
else:
	print("El total de tu compra es ", (precio *cantidad))








