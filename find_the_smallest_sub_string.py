'''
Question - Find the smallest substring containing all characters of t.
s = "ADOBECODEBANC"
t = "ABC"
'''

from collections import Counter

def min_window(s,t):
	need = Counter(t)
	missing = len(t)
	left = start = end = 0

	for right,char in enumerate(s,1):
		if need[char] > 0:
			missing -= 1
		need[char] -= 1

		if missing == 0:
			while left < right and need[s[left]] < 0:
				need[s[left]] += 1

			start,end = left,right

			need[s[left]] += 1
			missing += 1
			left += 1

	return s[start:end]

s = "ADOBECODEBANC"
t = "ABC"

print(min_window(s,t))
