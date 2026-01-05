'''
Implementation of Linked List in python
'''

class Node:
	def __init__(self,data):
		self.data = data 
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None


	def insert_at_begining(self,data):
		new_node = Node(data)
		new_node.next = self.head
		self.head = new_node

	
	def display(self):
		current = self.head
		while current:
			print(current.data, end="-->")
			current = current.next
		print("NULL")

ll = LinkedList()
ll.insert_at_begining(1)
ll.display()

