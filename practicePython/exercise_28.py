def max_of_three(a,b,c):
	if c<a>b or a==c>b or a==b>c: return a
	elif c<b>a or b==a>c or b==c>a: return b		 
	elif b<c>a or b==c>a or b==a>c: return c


print(max_of_three(2,1,0))
