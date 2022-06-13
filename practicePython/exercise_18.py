from random import randint

print("Welcome to the Cows and Bulls Game!")
r_number = str(randint(1000,9999))

while True:
	guess = input("guess a 4 digit number: ")
	cows = [r_number[x]==guess[x] for x in range(len(r_number))].count(True)  #4
	bulls = [x in guess for x in r_number].count(True)-cows
	print("{} cows, {} bulls".format(cows,bulls))
	if guess == r_number:
		break