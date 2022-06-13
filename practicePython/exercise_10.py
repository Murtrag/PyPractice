from random import randint
a = [randint(1,10) for _ in range(randint(1,14))]
b = [randint(1,10) for _ in range(randint(1,14))]


print(set(a) & set(b))