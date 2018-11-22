def search(list_v,number):
	check = [True for x in list_v if x==number]
	if check:
		return True
	else:
		return False


#print(search([1,2,3,4],1))

def binary_search(list_v,number):
	'''recursive binary list search'''
	print(list_v," ",len(list_v)//2," ")
	if list_v[0] == number or list_v[len(list_v)//2]==number:
		return True
	if len(list_v)==1 and not number in list_v:
		return False

	if list_v[len(list_v)//2] > number:
		return True if binary_search(list_v[0: len(list_v)//2],number) else False

	elif list_v[len(list_v)//2] < number:
		return True if binary_search( list_v[len(list_v)//2: ],number ) else False


#print(binary_search([1,2,3,4,5,10,100,500],501))