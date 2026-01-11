for i in range(1,3):
	print(i)  # stores in a memory at once

def simple_yield():
	for i in range(1,3):
		yield i

result = simple_yield()

for data in result:
	print(data)
