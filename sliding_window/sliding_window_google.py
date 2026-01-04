from collections import deque

def max_sliding_window(nums,k):
	dq = deque() # store indices
	result = []

	for i in range(len(nums)):
		
		#1. Remove the elements out of the window
		if dq and dq[0] == i-k:
			dq.popleft()

		#2. Remove smaller elements 
		while dq and nums[dq[-1]] < nums[i]:
			dq.pop()

		#3. Add current index
		dq.append(i)

		#4. Store result once window is formed
		if i>= k -1:
			result.append(nums[dq[0]])

	return result

nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3

print(max_sliding_window(nums,k))
