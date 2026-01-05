class Node:
	def __init__(self,data):
		self.data = data
		self.next = None

def insert_at_beginning(head,data):
	new_node = Node(data)
	new_node.next = head
	return new_node

def insert_at_end(head,data):
	new_node = Node(data)

	if new_node is None:
		return new_node

	current = head
	while current.next:
		current = current.next

	current.next = new_node
	return head

def display(head):
	current = head

	while current:
		print(current.data,end="-->")
		current = current.next

	print("NULL")



head = None
# Insert at beginning
head = insert_at_beginning(head, 20)
head = insert_at_beginning(head, 10)

# Insert at end
head = insert_at_end(head, 30)
head = insert_at_end(head, 40)

display(head)
