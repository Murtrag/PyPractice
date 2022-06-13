birthday_dates = {"Lukas":"04:01:1993", "Hadam":"14:01:1993"}

print("Welcome to the birthday dictionary. We know the birthdays of:")
for name in birthday_dates:
	print(name)
else:
	print("type end to quit")
while True:
	print("Who's birthday do you want to look up?")
	seek = input()
	if seek == "end": break
	print(seek,"'s birthday is ",birthday_dates[seek])