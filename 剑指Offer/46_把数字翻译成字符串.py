# -*- coding: UTF-8 -*-
"""
=================================================
Problem: 面试题46. 把数字翻译成字符串
Website: https://leetcode-cn.com/problems/ba-shu-zi-fan-yi-cheng-zi-fu-chuan-lcof/
Difficulty: 中等
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 48 ms, 在所有 Python3 提交中击败了21.66%的用户
Memory Usage: 13.7 MB, 在所有 Python3 提交中击败了100.00%的用户
=================================================="""


class Solution:
    """
    给定一个数字，我们按照如下规则把它翻译为字符串：
    0 翻译成 “a” ，1 翻译成 “b”，……，11 翻译成 “l”，……，25 翻译成 “z”。
    一个数字可能有多个翻译。
    请编程实现一个函数，用来计算一个数字有多少种不同的翻译方法。
    """
    @functools.lru_cache()
    def translateNum(self, num: int) -> int:
        s = str(num)
        if len(s) <= 1:
            return 1
        if int(s[:2]) <= 25:
            if len(s) == 2:
                return 2
            return self.translateNum(int(s[1:])) + self.translateNum(int(s[2:]))
        else:
            return self.translateNum(int(s[1:]))

"""

"""
