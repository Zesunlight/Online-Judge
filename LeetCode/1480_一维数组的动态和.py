# -*- coding: UTF-8 -*-
"""
=================================================
Problem: 1480. 一维数组的动态和
Website: https://leetcode-cn.com/problems/running-sum-of-1d-array/
Difficulty: 简单
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 40 ms
Memory Usage: 15 MB
=================================================="""


class Solution:
    """
    给你一个数组 nums 。数组「动态和」的计算公式为：runningSum[i] = sum(nums[0]…nums[i]) 。
    请返回 nums 的动态和。
    """
    class Solution:
        def runningSum(self, nums: List[int]) -> List[int]:
            for i in range(1, len(nums)):
                nums[i] += nums[i-1]
            return nums
