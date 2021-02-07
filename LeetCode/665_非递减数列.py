# -*- coding: UTF-8 -*-
"""
=================================================
Problem: 665. 非递减数列
Website: https://leetcode-cn.com/problems/non-decreasing-array/
Difficulty: 简单
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 48 ms
Memory Usage: 15.8 MB
=================================================="""


class Solution:
    """
    给你一个长度为 n 的整数数组，请你判断在 最多 改变 1 个元素的情况下，该数组能否变成一个非递减数列。
    我们是这样定义一个非递减数列的： 对于数组中所有的 i (0 <= i <= n-2)，总满足 nums[i] <= nums[i + 1]。
    """
    def checkPossibility(self, nums: List[int]) -> bool:
        n = 0
        p = -1
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                n += 1
                p = i
            if n > 1:
                return False
        if n == 0:
            return True
        
        if p == 0 or p == len(nums) - 2:
            return True
        if nums[p + 1] >= nums[p - 1]:
            return True
        if nums[p] <= nums[p + 2]:
            return True
        return False


"""
4，2，3
-1，4，2，3
2，3，3，2，4

https://leetcode-cn.com/problems/non-decreasing-array/comments/59727
"""