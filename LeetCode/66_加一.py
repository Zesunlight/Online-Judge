# -*- coding: UTF-8 -*-
"""
=================================================
Problem: 66. 加一
Website: https://leetcode-cn.com/problems/plus-one/
Difficulty: 简单
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 32 ms, 在所有 Python3 提交中击败了95.34%的用户
Memory Usage: 13.8 MB, 在所有 Python3 提交中击败了6.82%的用户
=================================================="""


class Solution:
    """
    给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。

    最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。

    你可以假设除了整数 0 之外，这个整数不会以零开头。
    """
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] != 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
        else:
            res = [1]
            res.extend(digits)
            return res
