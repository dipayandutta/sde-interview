s = "hello"
stack = []

for ch in s:
    stack.append(ch)
print(stack)
reverse_str = ""
while stack:
    reverse_str += stack.pop()

print(reverse_str)
