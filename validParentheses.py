'''
Question :- Valid Parentheses

Check if parentheses are balanced.

Input:
"{[()]}"
Output:
True
Invalid Example:
"{[(])}"
'''

'''
|------------|
|    Logic   |
|------------|
This is a stack problem.
Opening brackets → push to stack
Closing brackets → must match top of stack
'''
def is_valid_parentheses(s):
	stack = []
	mapping = {
        ')': '(',
        '}': '{',
        ']': '['
    }
	for char in s:
		if char in mapping.values():
			stack.append(char)

		elif char in mapping:
			if not stack or stack.pop() != mapping[char]:
				return False
		else:
			return False

	return len(stack) == 0
print(is_valid_parentheses("{[()]}"))   # True
print(is_valid_parentheses("{[(])}"))   # False
print(is_valid_parentheses("()[]{}"))   # True
print(is_valid_parentheses("((("))      # False
print(is_valid_parentheses(""))          # True

