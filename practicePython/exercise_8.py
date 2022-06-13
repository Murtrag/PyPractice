while True:
	table = {"r":1,"p":2,"s":3}
	player_1 = input("player1: choose rock(r) / scissors{s} / paper(p): ")
	player_2 = input("player2: choose rock(r) / scissors{s} / paper(p): ")


	if player_1==player_2:
		print("draw")
	elif player_1=="r" and player_2=="p":
		print("player2 wins")
	elif player_1=="p" and player_2=="r":
		print("player1 wins")

	elif player_1=="r" and player_2=="s":
		print("player1 wins")
	elif player_1=="s" and player_2=="r":
		print("player2 wins")
	elif player_1=="p" and player_2=="s":
		print("player2 winds")
	#elif player_1=="s" and player_2=="p":
	else:
		print("player1 winds")


