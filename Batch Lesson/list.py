list1 = ['physics', 'chemistry', 1997, 2000];
list2 = [2, 3, 1, 4, 5 ];
list3 = ["a", "b", "c", "d"];

frutas = ['naranja', 'manzana', 'pera', 'banana', 'kiwi', 'manzana', 'banana']
print(frutas)
frutas.count('manzana')
frutas.count('mandarina')
frutas.index('naranja')
frutas.index('banana', 4)  # Find next banana starting a position 4
frutas.reverse()
print(frutas)
frutas.append('uva')
print(frutas)
frutas.sort()
print(frutas)
frutas.pop()
print(frutas)
frutas.remove("manzana")
print(frutas)

print("......................")
print(list2)
list2.sort()
print("......................")
print(list2)
print("......................")
list2.extend(["Jose", "Gerardo"])
print(list2)
print("......................")
list2.insert(0,3)
print(list2)


for i in frutas:
	for y in i:
		if y == "z":
			print("En " + i + " esta la letra " + y)