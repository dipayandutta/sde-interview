'''
yield is used to create a generator , which produces values lazily, instead of computing and storing everything in the memory at once.

This is extremly useful for large data, streams and system level automation
'''
def simple_generator():
	yield 1
	yield 2
	yield 3


gen = simple_generator()
print(next(gen))
print(next(gen))
print(next(gen))
