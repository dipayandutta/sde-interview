'''
Question - Find Missing Number
--------
Given numbers from 1..n with one missing, find the missing number.
Input:
[1,2,3,5]
Output:
4
Constraint:
Do not sort the list.
Sum of numbers from 1..n: n(n+1)/2
'''

def find_missing_number(numbers):
	n = len(numbers)+1
	expected_sum = n*(n+1)/2
	actual_sum = sum(numbers)
	return int(expected_sum - actual_sum)

numbers = [1, 2, 3, 5]
print(find_missing_number(numbers))
