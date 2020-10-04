# -*- coding: UTF-8 -*-
"""
=================================================
Problem: 5531. 特殊数组的特征值
Website: https://leetcode-cn.com/problems/special-array-with-x-elements-greater-than-or-equal-x/
Difficulty: 简单
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 48 ms
Memory Usage: 13.4 MB
=================================================="""


class Solution:
    """
    给你一个非负整数数组 nums 。如果存在一个数 x ，使得 nums 中恰好有 x 个元素 大于或者等于 x ，那么就称 nums 是一个 特殊数组 ，而 x 是该数组的 特征值 。
    注意： x 不必 是 nums 的中的元素。
    如果数组 nums 是一个 特殊数组 ，请返回它的特征值 x 。否则，返回 -1 。
    可以证明的是，如果 nums 是特殊数组，那么其特征值 x 是 唯一的 。
    """
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        if nums[0] >= n:
            return n
        for i in range(1, n):
            if nums[-i] >= i > nums[-i - 1]:
                return i
        return -1
