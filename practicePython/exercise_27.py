game = [[0, 0, 0],
		[0, 0, 0],
		[0, 0, 0]]

counter = 0
while counter < len([1 for x in game for i in x]):
	player = 'one' if counter%2 else "two"
	tick = input("Player {}: Where would you like to place your char \nformat: 1,2 \n>> ".format(player))
	coordinates = [int(x) for x in tick.split(',')]

	if game[coordinates[0]-1][coordinates[1]-1] == 0:
		game[coordinates[0]-1][coordinates[1]-1] = 1 if counter%2 else 2
		counter+=1
	else:
		print("This move is forbidden")
		continue
else:
	print(game)
	


