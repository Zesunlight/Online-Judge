# -*- coding: UTF-8 -*-
"""
=================================================
Problem: 1431. 拥有最多糖果的孩子
Website: https://leetcode-cn.com/problems/kids-with-the-greatest-number-of-candies/
Difficulty: 简单
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 48 ms, 在所有 Python3 提交中击败了27.14%的用户
Memory Usage: 13.7 MB, 在所有 Python3 提交中击败了100.00%的用户
=================================================="""


class Solution:
    """
    给你一个数组 candies 和一个整数 extraCandies ，其中 candies[i] 代表第 i 个孩子拥有的糖果数目。

    对每一个孩子，检查是否存在一种方案，将额外的 extraCandies 个糖果分配给孩子们之后，此孩子有 最多的糖果。注意，允许有多个孩子同时拥有 最多的糖果数目。
    """
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        m = max(candies)
        return list(map(lambda x: x + extraCandies >= m, candies))
