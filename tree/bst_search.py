class Node:

    def  __init__(self,value):
        self.value = value
        self.left  = None
        self.right = None


# Search Target from the node

def search(node, target):
    # Base case: empty tree or found it
    if node is None:
        return False
    if node.value == target:
        return True

    # BST RULE: go left if smaller , right if bigger
    if target < node.value:
        return search(node.left,target)
    else:
        return search(node.right,target)

# Build the tree

root = Node(10)
root.left = Node(5)
root.right = Node(20)
root.left.left = Node(2)
root.left.right = Node(8)

# Display the tree
print(f"root node value {root.value}")
print(f"left node value {root.left.value}")
print(f"right node value {root.right.value}")
print(f"Left of the left node value {root.left.left.value}")
print(f"Left of the right node value {root.left.right.value}")


# Test the searching of the tree
print(search(root,8))
print(search(root,3))
print(search(root,2))
