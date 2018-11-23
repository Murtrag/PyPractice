def create_board(dim):
	line = "-"+"---"*dim
	delimiter = "|"+"  |"*dim
	for level in range(dim):
		print(line)
		print(delimiter)
	else:
		print(line)


#print(create_board(4))