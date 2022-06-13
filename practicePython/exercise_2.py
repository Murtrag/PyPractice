number = int(input("Just type a number: "))

if number%2:
	print("That is odd number")
elif not number%4:
	print("That is even number and divisible by 4!")
else:
	print("even number!")

num = int(input("Just type a number 1: "))
check = int(input("Just type a number 2: "))

if num%check:
	print('number 2 divide number 1 not evenly')
else:
	print('number 2 divide number 1 evenly')
