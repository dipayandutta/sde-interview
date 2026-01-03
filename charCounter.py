'''
Question - Count the number of Characters in the string 
'''

def charCounter(string):
	freq = {} #Dictonary to store key,value of char:count

	for char in string:
		freq[char] = freq.get(char,0)+1
	return freq

string="swisss"
print(charCounter(string))
