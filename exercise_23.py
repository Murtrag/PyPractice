happy = open("happy.txt")
prime = open("prime.txt")

with open("happy.txt") as happy:
	with open("prime.txt") as prime:
		results = []
		for num_1 in happy:
			num_1 = int(num_1.strip())
			for num_2 in prime:	
				num_2 = int(num_2.strip())
				if num_1 == num_2:
					results.append(num_1)		
			else:
				prime.seek(0)
			

					


print(results)

