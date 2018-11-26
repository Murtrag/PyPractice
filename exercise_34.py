#birthday_dates = {"Lukas":"04:01:1993", "Hadam":"14:01:1993"}
import json
with open("files/birth_dates.txt") as f:
	birthday_dates = json.loads(f.read())
#print(birthday_dates)
print("Welcome to the birthday dictionary. We know the birthdays of:")
for name in birthday_dates:
	print(name)
else:
	print("type end to quit \n type add to add new date")
while True:
	print("Who's birthday do you want to look up?")
	seek = input()
	if seek == "end": 
		break
	elif seek == "add":
		name, date = input("type name:date : ").split(":")
		birthday_dates[name]=date
		with open("files/birth_dates.txt", "w") as f:
			json.dump(birthday_dates, f)
	else:
		print(seek,"'s birthday is ",birthday_dates[seek])
