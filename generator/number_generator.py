def numbers_gen(n):
	for i in range(1,n+1):
		yield 1

gen = (x**x for x in range(5))

for value in gen:
	print(value)
