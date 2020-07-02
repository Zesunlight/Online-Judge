# -*- coding: UTF-8 -*-
"""
=================================================
Problem: 278. 第一个错误的版本
Website: https://leetcode-cn.com/problems/first-bad-version/
Difficulty: 简单
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 44 ms, 在所有 Python3 提交中击败了38.21%的用户
Memory Usage: 13.5 MB, 在所有 Python3 提交中击败了100.00%的用户
=================================================="""


class Solution:
    '''
    假设你有 n 个版本 [1, 2, ..., n]，你想找出导致之后所有版本出错的第一个错误的版本。

    你可以通过调用 bool isBadVersion(version) 接口来判断版本号 version 是否在单元测试中出错。
    实现一个函数来查找第一个错误的版本。你应该尽量减少对调用 API 的次数。
    '''
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 1, n
        while left <= right:
            middle = (left + right) // 2
            if isBadVersion(middle):
                right = middle - 1
            else:
                left = middle + 1
        return left
