from random import randint
a = [randint(1,20) for _ in range(randint(3,15))]
b = [randint(1,20) for _ in range(randint(3,15))]
#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

#b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

print(set(a) & set(b))

common = []
for item in b:
	if item in a and item not in common:
		common.append(item)
else:
	print(common)