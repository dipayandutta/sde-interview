for i in range(1,3):
	print(i)  # stores in a memory at once

print("Yield Output")
print("------------")


def simple_yield():
	for i in range(1,3):
		yield i
print(next(simple_yield()))
print(next(simple_yield()))

'''
result = simple_yield()

for data in result:
	print(data)

'''
