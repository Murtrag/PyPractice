word = "kajtek"

print("Welcome to Hangman!")
guess_place = list("_"*len(word))
used = []

miss = 0
while miss < 6:
	guess = input("Guess your letter: ")
	if guess in used:
		print("You have already pick that letter ",guess," so try again")
		continue
	if guess in word:		
		for x,letter in enumerate(word, start=0):
			if letter == guess:
				guess_place[x] = letter
	else:
		print("miss shoot!")
		miss +=1
	used += guess
	print(" ".join(guess_place))

