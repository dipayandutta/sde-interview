def count_up_to(n):
	i = 1
	while i<=n:
		yield i
		i+=1

gen = count_up_to(5)
print(next(gen))
print(next(gen))
print(next(gen))
