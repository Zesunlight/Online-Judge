# -*- coding: UTF-8 -*-
"""
=================================================
Problem: 263. 丑数
Website: https://leetcode-cn.com/problems/ugly-number/
Difficulty: 简单
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 28 ms
Memory Usage: 14.7 MB
=================================================="""


class Solution:
    """
    给你一个整数 n ，请你判断 n 是否为 丑数 。如果是，返回 true ；否则，返回 false 。
    丑数 就是只包含质因数 2、3 和/或 5 的正整数。
    """
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        while n % 2 == 0:
            n = n // 2
        while n % 3 == 0:
            n = n // 3
        while n % 5 == 0:
            n = n // 5
        return n == 1
