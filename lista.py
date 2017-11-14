list1 = [2,3,1,4,5]
list2 = ["A","B","C","D"]
list3 = ["MATEMATICAS","HISTORIA",1999,8983]
list4 = [list1,list2,list3]
'''
print(list1)
print(list2)
print(list3)
print(list4) 

for i in list3:
	print(i)
'''

frutas = ['naranja','manzana','pera','fresa',
'banana','manzana','kiwi']
print(frutas)

frutas.append('uva')
print("APPEND")
print(frutas)

#frutas.extend(list2)
#print(frutas)

frutas.insert(0,'melon')
print("INSERT1")
print(frutas)


frutas.pop(3)
print("POP")
print(frutas)


frutas.remove("manzana")
print("REMOVE")
print(frutas)


frutas.reverse()
print("REVERSE")
print(frutas)


frutas.sort(reverse = True)
print("SORT")
print(frutas)

print("COUNT")
print(frutas.count('manzana'))

print("INDEX")
print(frutas.index('naranja',0))


for i in len(frutas):
	print(i)
	if i == "manzana":
		print("MANZANA")



