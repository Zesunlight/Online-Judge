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

	def getInformation(self):
		print(self)

if __name__ == '__main__':
	s = Solution()
	print(s.findIndices([2, 7, 11, 15], 9))
