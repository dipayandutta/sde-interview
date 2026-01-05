class Node:
	def __init__(self,data):
		self.data = data
		self.next = None

def insert(head,data):
	new_node = Node(data)

	if head is None:
		return new_node

	current = head # head points to the first node
	while current.next: # Keep looping as there is a next node
		current = current.next # Move the pointer forward by One

	current.next = new_node # Actual insertion
	return head


def display(head):
	current = head
	while current:
		print(current.data, end="-->")
		current = current.next

	print("NULL")

head = None

head = insert(head, 10)
head = insert(head, 20)
head = insert(head, 30)

display(head)
