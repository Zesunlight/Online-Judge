# -*- coding: UTF-8 -*-
"""
=================================================
Problem: 面试题14- II. 剪绳子 II
Website: https://leetcode-cn.com/problems/jian-sheng-zi-ii-lcof/
Difficulty: 中等
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 44 ms, 在所有 Python3 提交中击败了64.32%的用户
Memory Usage: 13.7 MB, 在所有 Python3 提交中击败了100.00%的用户
=================================================="""


class Solution:
    """
    给你一根长度为 n 的绳子，请把绳子剪成整数长度的 m 段（m、n都是整数，n>1并且m>1），
    每段绳子的长度记为 k[0],k[1]...k[m - 1] 。请问 k[0]*k[1]*...*k[m - 1] 可能的最大乘积是多少？
    例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。

    答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。
    """

    def cuttingRope(self, n: int) -> int:
        if n == 2:
            return 1
        elif n == 3:
            return 2

        three, rest = divmod(n, 3)
        if rest == 0:
            return 3 ** three % 1000000007
        elif rest == 1:
            return 3 ** (three - 1) * 4 % 1000000007
        else:
            return 3 ** three * 2 % 1000000007
