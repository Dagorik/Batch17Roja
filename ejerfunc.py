original_list = [('Buenas', 'Tardes'), ('Buenos', 'Días'), ('Buenas', 'Noches'), ('Buenos', 'Besos'), ('Buenas', 'Las tenga')]

def tuples_to_dict(list_tuples):
	result_dict = {}
	for x,y in list_tuples:
		current_value = result_dict.get(x, None)
		if current_value:
			if type(current_value) is list:
				current_value.append(y)
			else:
				new_list = [current_value, y]
				result_dict[x] = new_list
		else:
			result_dict.update({x: y})
	return result_dict

print(tuples_to_dict(original_list))
