class stack:
    def __init__(self):
        self.stack = []

    def push(self,value):
        self.stack.append(value)
        print(f"Pushed Item: {value}")

    def pop(self):
        if self.is_empty():
            print("Stack Underflow!")
            return None
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            print("Stack is empty")
            return None 
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def display(self):
        print("stack: ",self.stack)

s = stack()
s.push(10)
s.push(20)
s.push(30)
s.push(40)

s.peek()
s.pop()
s.peek()
s.display()

