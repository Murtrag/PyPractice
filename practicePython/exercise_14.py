def remove_duplicates(lista):
	lista = sorted(lista)	
	count = 0
	output=[]
	while count<len(lista):		
		if count+1 < len(lista):
			if lista[count]!= lista[count+1]:
				if lista[count] not in output:
					output.append(lista[count])
				if lista[count+1] not in output:
					output.append(lista[count+1])
		count+=1
	else:
		return output

def remove_duplicates2(lista):
	return list(set(lista))
	


print(remove_duplicates2([4,1,9,2,1,1,9,1,3]))