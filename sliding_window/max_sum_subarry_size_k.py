'''
Question - Given an integer array and a number k, find the maximum sum of any contiguous subarray of size k

Fixed Window Size 
Avoid recomputing sums

'''

def max_sum_subarray(arr,k):
	window_sum = sum(arr[:k])
	max_sum = window_sum

	for i in range(k,len(arr)):
		window_sum += arr[i]
		window_sum -= arr[i-k]
		max_sum = max(max_sum,window_sum)

	return max_sum

arr = [2, 1, 5, 1, 3, 2]
k = 3

print(max_sum_subarray(arr,k))

