from random import randint

number = randint(1,9)

while True:
	guess = int(input("guess what is the number: "))

	if guess<number:
		print("to low")
	elif guess == number:
		print("Thats it!")
		break
	else:
		print("To high!")