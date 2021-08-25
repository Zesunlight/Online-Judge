# -*- coding: UTF-8 -*-
"""=================================================
Problem: 268. 丢失的数字
Website: https://leetcode-cn.com/problems/missing-number/
Difficulty: 简单
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 32 ms
Memory Usage: 15.7 MB
=================================================="""

"""
给定一个包含 [0, n] 中 n 个数的数组 nums ，找出 [0, n] 这个范围内没有出现在数组中的那个数。
"""


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        return n * (n + 1) // 2 - sum(nums)
