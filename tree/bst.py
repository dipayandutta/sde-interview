'''
**The tree you've built looks like this:**
```
        10
       /  \
      5    20
     / \
    2   8
'''
class Node:
    def __init__(self,value):
        self.value = value
        self.left  = None 
        self.right = None 

root = Node(10)
root.left = Node(5)
root.right = Node(20)

root.left.left = Node(2)
root.left.right = Node(8)

print(root.value) # 10
print(root.left.value) #5 
print(root.right.value) # 20
print(root.left.left.value) # 2 
print(root.left.right.value) # 8


