"""
    Problem: 46. Permutations
    Website: https://leetcode.com/problems/permutations/
    Difficulty: Medium
    Author: ZYZ
    Language: Python3
    Result: Accepted
    Runtime: 48 ms, faster than 71.27% of Python3 online submissions for Permutations.
    Memory Usage: 14 MB, less than 5.36% of Python3 online submissions for Permutations.
"""


class Solution:
    """
    Given a collection of distinct integers, return all possible permutations.

    Input: [1,2,3]
    Output:
    [
      [1,2,3],
      [1,3,2],
      [2,1,3],
      [2,3,1],
      [3,1,2],
      [3,2,1]
    ]
    """

    def permute(self, nums):
        if len(nums) == 0:
            return []
        elif len(nums) == 1:
            return [[nums[0]]]
        # elif len(nums) == 2:
        #     return [[nums[0], nums[1]], [nums[1], nums[0]]]

        res = []
        for i in range(len(nums)):
            temp = self.permute(nums[:i] + nums[i + 1:])
            for item in temp:
                res.append([nums[i]] + item)

        return res

    def permute2(self, nums):
        if len(nums) == 0:
            return []
        elif len(nums) == 1:
            return [[nums[0]]]

        res = []
        insert = [nums[0]]
        small = self.permute2(nums[1:])

        for item in small:
            for i in range(len(item) + 1):
                res.append(item[:i] + insert + item[i:])

        return res


s = Solution()
a = [i for i in range(3)]
print(s.permute(a))
# print(s.permute2(a))
