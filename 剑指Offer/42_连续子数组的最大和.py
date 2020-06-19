# -*- coding: UTF-8 -*-
"""
=================================================
Problem: 面试题42. 连续子数组的最大和
Website: https://leetcode-cn.com/problems/lian-xu-zi-shu-zu-de-zui-da-he-lcof/
Difficulty: 简单
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 96 ms, 在所有 Python3 提交中击败了33.41%的用户
Memory Usage: 18.4 MB, 在所有 Python3 提交中击败了100.00%的用户
=================================================="""


class Solution:
    """
    请实现两个函数，分别用来序列化和反序列化二叉树。
    """
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        for i in range(1, len(nums)):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
            res = max(res, nums[i])
        return res
