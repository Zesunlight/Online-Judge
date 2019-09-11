"""
    Problem: 78. Subsets
    Website: https://leetcode.com/problems/subsets/
    Difficulty: Medium
    Author: ZYZ
    Language: Python3
    Result: Accepted
    Runtime: 40 ms, faster than 74.33% of Python3 online submissions for Subsets.
    Memory Usage: 13.8 MB, less than 5.95% of Python3 online submissions for Subsets.
"""


class Solution:
    """
    Given a set of distinct integers, nums, return all possible subsets (the power set).

    Note: The solution set must not contain duplicate subsets.
    """

    def subsets(self, nums):

        if len(nums) == 0:
            return [[]]
        elif len(nums) == 1:
            return [[nums[0]], []]
        else:
            temp = []
            for item in self.subsets(nums[1:]):
                item.append(nums[0])
                temp.append(item)
            temp.extend(self.subsets(nums[1:]))
            return temp


s = Solution()
n = [1, 2]
print(s.subsets(n))


"""
https://leetcode.com/problems/subsets/discuss/27278/C++-RecursiveIterativeBit-Manipulation
"""

"""
https://leetcode.com/problems/subsets/discuss/27356/5-lines-of-python

class Solution(object):
    def subsets(self, nums):
        result = [[]]
        for num in nums:
            result += [i + [num] for i in result]
        return result
"""