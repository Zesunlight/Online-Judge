# -*- coding: UTF-8 -*-
"""=================================================
Problem: 1588. 所有奇数长度子数组的和
Website: https://leetcode-cn.com/problems/sum-of-all-odd-length-subarrays
Difficulty: 简单
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 52 ms
Memory Usage: 15 MB
=================================================="""
from typing import List

"""
给你一个正整数数组arr，请你计算所有可能的奇数长度子数组的和。
子数组 定义为原数组中的一个连续子序列。
请你返回 arr中 所有奇数长度子数组的和 。
"""


class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        s = 0
        n = len(arr)
        p = [0] + arr.copy()
        for i in range(1, n + 1):
            p[i] += p[i - 1]

        for i in range(1, n + 1, 2):
            for j in range(i, n + 1):
                s += (p[j] - p[j - i])

        return s


if __name__ == '__main__':
    solution = Solution()
    print(solution.sumOddLengthSubarrays([10, 11, 12]))
