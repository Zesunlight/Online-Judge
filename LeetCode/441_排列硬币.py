# -*- coding: UTF-8 -*-
"""=================================================
Problem: 441. 排列硬币
Website: https://leetcode-cn.com/problems/arranging-coins/
Difficulty: 简单
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 40 ms
Memory Usage: 15 MB
=================================================="""


class Solution:
    """
    你总共有 n 枚硬币，并计划将它们按阶梯状排列。
    对于一个由 k 行组成的阶梯，其第 i 行必须正好有 i 枚硬币。
    阶梯的最后一行 可能 是不完整的。
    给你一个数字 n ，计算并返回可形成 完整阶梯行 的总行数。
    """
    def arrangeCoins(self, n: int) -> int:
        return floor(sqrt(2 * n + 0.25) - 0.5)
