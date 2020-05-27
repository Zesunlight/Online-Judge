# -*- coding: UTF-8 -*-
"""
=================================================
Problem: 560. 和为K的子数组
Website: https://leetcode-cn.com/problems/subarray-sum-equals-k/
Difficulty: 中等
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 64 ms, 在所有 Python3 提交中击败了84.06%的用户
Memory Usage: 16 MB, 在所有 Python3 提交中击败了11.11%的用户
=================================================="""


class Solution:
    """
    给定一个整数数组和一个整数 k，你需要找到该数组中和为 k 的连续的子数组的个数。
    """
    def subarraySum(self, nums, k: int) -> int:
        if nums is None or len(nums) == 0:
            return 0
        sub_sum = {0: 1}
        s = 0
        amount = 0
        for i in range(len(nums)):
            s += nums[i]
            if s - k in sub_sum:
                amount += sub_sum[s - k]
            sub_sum[s] = sub_sum.get(s, 0) + 1

        return amount


s = Solution()
print(s.subarraySum([1], 0))

"""
https://leetcode-cn.com/problems/subarray-sum-equals-k/solution/he-wei-kde-zi-shu-zu-by-leetcode-solution/
前缀和 + 哈希表优化
"""
