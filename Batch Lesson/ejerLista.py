numero = int(input("Digame cuantas palabras tiene la lista: "))

if numero < 1:
    print("Imposible!")
else:
    lista = []
    for i in range(numero):
        print("Digame la palabra", str(i + 1) + ": ",)
        palabra = str(input())
        lista.append(palabra)
    print("La lista creada es:", lista)