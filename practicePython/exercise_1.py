import datetime
name = input("Enter your name: ")
age = input("Enter your age: ")
mul = input('Enter number of copies: ')

current_year = datetime.datetime.today()
hundret_at = current_year + datetime.timedelta(days=365*(100-int(age)))


print(int(mul)*"Your are going to be 100yrs old in {} \n".format(hundret_at.year))