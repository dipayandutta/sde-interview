class Node:
	def __init__(self,data):
		self.data = data
		self.next = None

def insert(head,data):
	new_node = Node(data)
	new_node.next = head
	return new_node

def display(head):
	current = head

	while current:
		print(current.data,end="-->")
		current = current.next

	print("NULL")



def reverseList(head):
	prev = None
	current = head

	while current:
		new_node = current.next # save next 
		current.next = prev # reverse link
		prev = current # move prev
		current = new_node # move current 

	return prev

head = None
head = insert(head,10)
head = insert(head,20)
head = insert(head,30)

display(head)

# Reverse the list
head = reverseList(head) # After reversing the list, give me the new starting point and remember it as head
print("Reversed List")
display(head)
