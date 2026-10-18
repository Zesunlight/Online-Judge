# -*- coding: UTF-8 -*-
"""
=================================================
Problem: 283. 移动零
Website: https://leetcode.cn/problems/move-zeroes/description/
Difficulty: 简单
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 7 m
Memory Usage: 20.34 MB
=================================================="""

from typing import List


class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero = 0
        for i in nums:
            if i == 0:
                zero += 1
        idx = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[idx] = nums[i]
                idx += 1
        for i in range(len(nums)-zero, len(nums)):
            nums[i] = 0

    def moveZeroes2(self, nums: List[int]) -> None:
        # https://leetcode.cn/problems/move-zeroes/solutions/489622/yi-dong-ling-by-leetcode-solution/
        n = len(nums)
        left = right = 0
        while right < n:
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            right += 1
