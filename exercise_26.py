#game = [[2,2,1],
#		[1,2,1],
#		[1,1,2]]

def check_if_win(game):
	col_res = {}
	for col in game:
		if all(x == col[0] for x in col):
			print("wygrał gracz ", col[0])
			return col[0]

		for iteration,x in enumerate(col, start=1):  #created dict to check more complex conditions
			if not iteration in col_res:
				col_res[iteration] =  [x]
			else:
				col_res[iteration].append(x)
	else:
		for row in col_res:  #loop to check rows and across
			if all(col_res[row][0]==item for item in col_res[row]):
				#print("wygrał gracz ",col_res[row][0])
				return col_res[row][0]
			elif all(col_res[row][0] == col_res[x][x-1] for x in range(1,3)):
				#print("wygrał gracz ",col_res[row][0])
				return col_res[row][0]
			elif all(col_res[row][2] == col_res[x][x-1] for x in range(3,1)):
				#print("wygrał gracz ",col_res[row][2])
				return col_res[row][2]


#print(check_if_win(game))
