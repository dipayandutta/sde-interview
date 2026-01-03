'''

Question - Given a string , Return its reverse


Constraints
Do not use built-in reverse helpers like [::-1] (interviewer may restrict this).
'''


def stringReverse(string):
	if(len(string)==0):
		return string
	else:
		return string[-1] + stringReverse(string[:-1])

string="linux"
print(stringReverse(string))


'''
Optimize Solution

Logic
------

Start from the last character of the string, move backward one character at a time, and stop after reaching the first character

range() function
-----------------
range(start, stop, step)

start → where counting begins
stop → where counting stops (not included)
step → how much to move each time

l i n u x
0 1 2 3 4 <--- index

len(s) = 5 
len(s)-1 = 4 (index of x)

Then -1 --> Move Backward , decrement by 1 each iteration
'''

def string_reverse_iterative(s):
	result = []
	for i in range(len(s)-1,-1,-1):
		result.append(s[i])
	return ''.join(result)

print(string_reverse_iterative(string))
