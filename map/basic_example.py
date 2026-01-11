def custom_power(x,y):
	return x**y

x = [10,2,3]
y = [2,4,3]
result = list(map(custom_power,x,y))
print(result)
