'''
Question - Count Digit and Letters
Count number of digits and alphabets in a string.
Input:
"py3thon2025"
Output:
Letters: 6, Digits: 5
'''
# This is the inefficient way with greater time complexity
def count_letter_digit(string):
	numbers = [number for number in range(0,11)]
	countNumber = 0
	countLetter = 0
	numberArray = []
	letterArray = []

	for char in string:
		for number in numbers:
			if str(number) == char:
				countNumber+=1
				numberArray.append(char)
		if char not in numberArray:
			countLetter+=1
			letterArray.append(char)
	print("Digits: ",len(numberArray))
	print("Letters: ",len(letterArray))

string="py3thon2025"
count_letter_digit(string)

# Efficient Way
def countltrdigit(string):
	letters = 0
	digits = 0

	for char in string:
		if char.isalpha():
			letters +=1 
		elif char.isdigit():
			digits +=1
	print("Letters: ",letters)
	print("Digits: ",digits)

countltrdigit(string)

