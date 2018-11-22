from random import randint

min = 0
max = 100
while True:
	guess = randint(min,max)
	print(guess)
	answer = input("is it to high or too low? ( l/h/c ): ")
	#l = lower
	#h = higher
	#c = complete


	if answer == "l":
		max = guess - 1
	elif answer == "h":
		min = guess + 1
	elif answer == "x":
		print("huraa!")
		break