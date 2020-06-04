# -*- coding: UTF-8 -*-
"""
=================================================
Problem: 面试题10- II. 青蛙跳台阶问题
Website: https://leetcode-cn.com/problems/qing-wa-tiao-tai-jie-wen-ti-lcof/
Difficulty: 简单
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 36 ms, 在所有 Python3 提交中击败了83.90%的用户
Memory Usage: 13.7 MB, 在所有 Python3 提交中击败了100.00%的用户
=================================================="""


class Solution:
    """
    一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。求该青蛙跳上一个 n 级的台阶总共有多少种跳法。

    答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。
    """
    def numWays(self, n: int) -> int:
        a, b = 1, 1
        for _ in range(n):
            a, b = b, a + b
        return a % int(1e9+7)


"""
和斐波那契数列一个意思

1. 1000000007是一个质数（素数），对质数取余能最大程度避免冲突～

2. int32位的最大值为2147483647，所以对于int32位来说1000000007足够大

3. int64位的最大值为2^63-1，对于1000000007来说它的平方不会在int64中溢出
所以在大数相乘的时候，因为(a∗b)%c=((a%c)∗(b%c))%c，所以相乘时两边都对1000000007取模，再保存在int64里面不会溢出

https://www.liuchuo.net/archives/645
"""
