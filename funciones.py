def mi_funcion():
	#Todo el bloque de codigo que se ejecuta cuando se llame la funcion
	print("HOLA SOY UNA FUNCION")

#mi_funcion()

#Parametro y parametro con un valor por default
def suma_de_dos_numeros(num1,num2,num4=None):
	print(num4)
	suma = num1 + num2
	print(str(suma))

#Llamar la funcion
#suma_de_dos_numeros(3,5,4)

def funcion_return(num1,num2):
	suma = num1 + num2
	return suma

def return_mult(num1,num2,num3):
	if num1 ==2:
		return "NUMERO 2"
	else:
		return num3

sumar = funcion_return(2,2)
#print(sumar)

multiple = return_mult(3,2,999)
print(multiple)

