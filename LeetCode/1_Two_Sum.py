# -*- coding: utf-8 -*-

# https://leetcode.com/problems/two-sum/

class Solution(object):
	def __init__(self):
		self.name = 'leetcode'

	def findIndices(self, nums, target):
		length = len(nums)
		for i in range(length):
			for j in range(i+1, length):
				if nums[i] + nums[j] == target:
					return [i, j]

	# better answer from others'
	def twoSum(self, nums, target):
		if len(nums) <= 1:
		    return False
		buff_dict = {}
		for i in range(len(nums)):
		    if nums[i] in buff_dict:
				return [buff_dict[nums[i]], i]
		    else:
				buff_dict[target - nums[i]] = i

if __name__ == '__main__':
	s = Solution()
	print(s.findIndices([2, 7, 11, 15], 9))
