'''
Question - Count the number of Characters in the string 
'''

def charCounter(string):
	freq = {} #Dictonary to store key,value of char:count

	for char in string:
		# freq.get(char,0) --> If char exists , return its value , if not return 0
		freq[char] = freq.get(char,0)+1 # Each time increment by 1
	return freq

string="swisss"
print(charCounter(string))
