class SparseArray:
	def __init__(self):
		self.data = {}

	def set(self,index,value):
		if value != 0:
			self.data[index] = value
		elif index in self.data:
			del self.data[index]

	def get(self,index):
		return self.data.get(index,0) # Returns Zero (0) if index is not in the data

# Usage
sparse_array = SparseArray()
sparse_array.set(2,3)
sparse_array.set(7,9)

print(sparse_array.get(2))
print(sparse_array.get(7))
