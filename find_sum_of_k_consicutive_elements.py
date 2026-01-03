'''
Question - Find the maximum sum of k consecutive elements.
'''

def max_subarray_sum(arr,k):
	window_sum = sum(arr[:k])
	max_sum = window_sum
	#print(window_sum)
	#print(arr[:k])

	for i in range(k,len(arr)):
		window_sum += arr[i] # add new
		window_sum -= arr[i-k] # remove old
		max_sum = max(max_sum,window_sum)

	return max_sum
arr = [2, 1, 5, 1, 3, 2]
k = 3

print(max_subarray_sum(arr,k))
