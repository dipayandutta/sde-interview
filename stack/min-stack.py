'''
To Find the minimum element in the stack
'''

class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self,x):
        self.stack.append(x)

        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)

    def pop(self):
        if not self.stack:
            return None

        removed = self.stack.pop()

        if removed == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self):
        if not self.stack:
            return None 
        return self.stack[-1]

    def getMin(self):
        return self.min_stack[-1]

s = MinStack()
s.push(5)
s.push(3)
s.push(7)
s.push(2)

print(s.getMin())  # 2
s.pop()
print(s.getMin())  # 3

