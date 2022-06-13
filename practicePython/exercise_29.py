#from exercise_24 import create_board
from exercise_26 import check_if_win


game = [[0, 0, 0],
		[0, 0, 0],
		[0, 0, 0]]

def create_board(dim, table):
	line = "-"+"---"*dim
	for level in range(dim):
		print(line)
		print(str(table[level]).translate({91: 124, 93: 124, 44: 124, 49: 79, 50: 88, 48: 32, 32: None}).replace("|",' |'))
	else:
		print(line)
#create_board(3,game)


counter = 0
while counter < len([1 for x in game for i in x]):
	create_board(3,game)
	if check_if_win(game)==1:
		print("wygrywa gracz 1!")
		break
	elif check_if_win(game)==2:
		print("wygrywa gracz 2!")
		break
	print(check_if_win(game))
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
	create_board(3,game)