# -*- coding: UTF-8 -*-
"""
=================================================
Problem: 面试题10- I. 斐波那契数列
Website: https://leetcode-cn.com/problems/fei-bo-na-qi-shu-lie-lcof/
Difficulty: 简单
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 40 ms, 在所有 Python3 提交中击败了64.51%的用户
Memory Usage: 13.7 MB, 在所有 Python3 提交中击败了100.00%的用户
=================================================="""


class Solution:
    """
    写一个函数，输入 n ，求斐波那契（Fibonacci）数列的第 n 项。
    斐波那契数列由 0 和 1 开始，之后的斐波那契数就是由之前的两数相加而得出。

    答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。
    """
    def fib(self, n: int) -> int:
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a % int(1e9 + 7)


"""
1e9 + 7 的结果默认是 float 类型
int(a % (1e9 + 7)) 会因为精度出现问题
"""
