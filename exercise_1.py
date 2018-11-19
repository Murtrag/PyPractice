import datetime
name = input("Enter your name: ")
age = input("Enter your age: ")
mul = input('Enter number of copies: ')

current_year = datetime.datetime.today()
hundret_at = current_year + datetime.timedelta(days=365*(100-int(age)))

for _ in range(int(mul)):
	print("Your are going to be 100yrs old in {}".format(hundret_at.year))