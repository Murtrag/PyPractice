from random import randint

number = randint(1,9)
count = 0
while True:
	count+=1
	guess = input("guess what is the number: ")
	if guess == "exit":
		break
	guess = int(guess)

	if guess<number:
		print("to low")
	elif guess == number:
		print("Thats it! You've guessed it in {} tries".format(count))
		break
	else:
		print("To high!")