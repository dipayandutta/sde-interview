'''
Question - Return the average of all contiguous subarrays of size k.
'''

def subarray_average(arr,k):
	result = []
	window_sum = sum(arr[:k])

	result.append(window_sum /k)

	for i in range(k,len(arr)):
		window_sum += arr[i]
		window_sum -= arr[i-k]
		result.append(window_sum / k)
	
	allaverage = sorted(result)
	return allaverage[::-1][0]

arr = [2, 1, 5, 1, 3, 2]
k = 3

print(subarray_average(arr,k))
