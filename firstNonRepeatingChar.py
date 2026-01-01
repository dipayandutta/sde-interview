'''
Question - First Non-Repeating Characte
Return the first character that does not repeat.
Input:
"swiss"
Output:
"w"
'''
'''
|=============|
|   #LOGIC    |
|=============|
Count frequency of each character
Iterate original string
Return first character with count == 1
'''

def first_non_repeating_char(string):
	freq = {} # Dictonary
	for char in string:
		freq[char] = freq.get(char,0)+1 #Try to get the value for key char

	for char in string:
		if freq[char] == 1:
			return char
	return None

string="swiss"
print(first_non_repeating_char(string))
