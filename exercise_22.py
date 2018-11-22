hoo_file = open("data.txt", "r")

counter=0
count_group = {}

for line in open("data.txt","r"):
	line =line.split("/")
	if not line[2] in count_group:
		count_group[line[2]]=1
	else:
		count_group[line[2]]+=1

	counter+=1	


print(counter)

for item in count_group:
	print("{} : {}".format(item, count_group[item]))