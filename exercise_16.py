import string
import random

def pass_get(level):
	opt1=["tajne","haslo","moje","niezgadniesz"]
	opt2=[str(num) for num in range(0,10)]
	opt3=list(string.ascii_lowercase)
	opt4=list(string.ascii_uppercase)
	opt5=list("!@#$%^&*()_+=-`")
	opt6=list("[]\\;',./{}|:\"<>?")
	pass_parts = [opt1,opt2,opt3,opt4,opt5,opt6]

	password = [opt1[random.randint(0,len(opt1)-1)],opt2[random.randint(0,9)]] 
	random.shuffle(password)
	if level == 1: return "".join(password)

	for item in range(2,level+1):
		which_list = item if item <=5 else random.randint(1,5)
		password.append(  pass_parts[which_list][random.randint(0,len(pass_parts[which_list])-1)]  )
		random.shuffle(password)

		if level == item: return "".join(password)

level = int(input("how strong password do you want to generate? type a number: "))

print(pass_get(level))
