def is_prime(number):
	if not number%2:
		return "prime"
	else:
		return "odd"
number = int(input("type a number: "))
print("this number ",number," is ",is_prime(number)," ")
