'''
Question:- Reverse Words
========
Given a sentence, reverse each word without reversing word order.
Input:
"Linux loves Python"
Output:
"xuniL sevol nohtyP"
'''

def reverseWords(string):
	words = string.split()
	reverse_words = []
	for word in words:
		reverse_words.append(word[::-1])
	return " ".join(reverse_words)

string = "Linux loves Python"
result = reverseWords(string)
print(result)

