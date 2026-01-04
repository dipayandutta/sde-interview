'''
Given an array of integers, return indices of the tow numbers such that they add up to a specific target .

You may assume that each input would have exactly one solution, and you may not the same element twice.

For Example
------------

Given nums = [2,7,11,15], target =9

Because nums[0] + nums[1] = 4
return [0,1]
'''
from typing import List

class Solution:
	def twoSum(self, nums: List[int], traget: int) -> List[int]:
		prevMap = {} # Prev HasMap Val:index

		for i,n in enumerate(nums):
			diff = target -n
			if diff in prevMap:
				return [prevMap[diff],i]
			prevMap[n] = i
		return

nums =[2,1,5,3]
target = 4 
sol = Solution()
print(sol.twoSum(nums,target))
