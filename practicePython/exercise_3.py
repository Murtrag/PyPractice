a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

print("\n".join([str(x) for x in a if int(x)<5]))

new_list = [x for x in a if int(x)<5]
print(new_list)

for number in a:
	if number<5:
		print(number,end=" ")
print("\n\n")

ceiling = int(input("Give a ceiling number: "))
print(' '.join([str(x) for x in a if int(x)<ceiling])) 