#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
dividendo = int(input("Escriba el dividendo: "))
divisor = int(input("Escriba el divisor: "))

if dividendo % divisor == 0:
    print('La división es exacta. Cociente:', dividendo // divisor)
else:
    print('La división no es exacta. Cociente:', dividendo // divisor, 'Resto:', dividendo % divisor)


print("COMPARADOR DE NÚMEROS")
numero_1 = int(input("Escriba un número: "))
numero_2 = int(input("Escriba otro número: "))

if numero_1 > numero_2:
    print("Menor:", numero_2, "Mayor:", numero_1)
elif numero_1 < numero_2:
    print("Menor:", numero_1,"Mayor:", numero_2)
else:
    print("Los dos números son iguales")


print("COMPARADOR DE AÑOS")
fecha_1 = int(input("¿En qué año estamos?: "))
fecha_2 = int(input("Escriba un año cualquiera: "))

if fecha_1 > fecha_2:
    print("Desde el año", fecha_2, "han pasado", fecha_1 - fecha_2, "años")
elif fecha_1 < fecha_2:
	print("Para llegar al año", fecha_2, "faltan", fecha_2 - fecha_1, "años")
else:
    print("¡Son el mismo año!")

print("COMPARADOR DE TRES NÚMEROS")
numero_1 = float(input("Escriba un número: "))
numero_2 = float(input("Escriba otro número: "))
numero_3 = float(input("Escriba otro número más: "))

if (numero_1 == numero_2 != numero_3 or numero_1 == numero_3 != numero_2 or
    numero_2 == numero_3 != numero_1):
    print("Ha escrito uno de los números dos veces.")
elif numero_1 == numero_2 == numero_3:
    print("Ha escrito tres veces el mismo número.")
else:
    print("Los tres números que ha escrito son distintos.")
'''


A=int(input("ingrese un numero\n"))
B=int(input("ingrese otro numero\n"))
C=int(input("ingrese un nuemero\n"))

if(A > B and A > C):
	print("El numero mayor es " + str(A))
else:
	if(B > A and B > C):
		print("El numero mayor es " + str(B))
	else:
		print("El numero mayor es " + str(C))

print(max(A,B,C))
    