def is_palindrome(string):
	string = string.lower()
	if len(string)<1:
		return True
	if string[0] != string[-1]:
		return False
	return is_palindrome(string[1:-1])

# Test the function
print(is_palindrome("radar"))  # Output: True
print(is_palindrome("hello"))  # Output: False
