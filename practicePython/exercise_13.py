def fib_list(x):
	resp = [1,1]
	for _ in range(x-2):
		resp.append(resp[-1]+resp[-2])
	else:
		return resp

print(fib_list(19))


