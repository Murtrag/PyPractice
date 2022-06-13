HANGMANPICS = ['''
	  +---+
	  |   |
	      |
	      |
	      |
	      |
	=========''', '''
	  +---+
	  |   |
	  O   |
	      |
	      |
	      |
	=========''', '''
	  +---+
	  |   |
	  O   |
	  |   |
	      |
	      |
	=========''', '''
	  +---+
	  |   |
	  O   |
	 /|   |
	      |
	      |
	=========''', '''
	  +---+
	  |   |
	  O   |
	 /|\  |
	      |
	      |
	=========''', '''
	  +---+
	  |   |
	  O   |
	 /|\  |
	 /    |
	      |
	=========''', '''
	  +---+
	  |   |
	  O   |
	 /|\  |
	 / \  |
	      |
	=========''']

from exercise_30 import pick_word
def initiate():	
	word = pick_word().lower()
	print(word)
	print("Welcome to Hangman!")
	guess_place = list("_"*(len(word)-1))
	used = []
	return word, guess_place, used
word, guess_place, used = initiate()


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
	print(HANGMANPICS[miss])
	print("You have left {} gusses".format(6-miss))


	if "".join(guess_place) == word.strip():
		print('You have finished!')
		play_again = input("Would you like to start again? y/n: ")
		if play_again=="y":
			word, guess_place, used = initiate()
			continue
		else:
			break