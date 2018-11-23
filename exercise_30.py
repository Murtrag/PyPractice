from random import choice
def pick_word():
	words = open('files/words.txt').readlines()
	return choice(words)


#print(pick_word())