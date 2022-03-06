# -*- coding: UTF-8 -*-
"""=================================================
Problem: 2100. 适合打劫银行的日子
Website: https://leetcode-cn.com/problems/find-good-days-to-rob-the-bank/
Difficulty: 中等
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 252 ms
Memory Usage: 32.5 MB
=================================================="""
from typing import List

"""
你和一群强盗准备打劫银行。给你一个下标从 0开始的整数数组security，其中security[i]是第 i天执勤警卫的数量。
日子从 0开始编号。同时给你一个整数time。

如果第 i天满足以下所有条件，我们称它为一个适合打劫银行的日子：
第 i天前和后都分别至少有 time天。
第 i天前连续 time天警卫数目都是非递增的。
第 i天后连续 time天警卫数目都是非递减的。
更正式的，第 i 天是一个合适打劫银行的日子当且仅当：
security[i - time] >= security[i - time + 1] >= ... >= security[i] <= ... <= security[i + time - 1] <= security[i + time].

请你返回一个数组，包含 所有 适合打劫银行的日子（下标从 0开始）。返回的日子可以 任意顺序排列。
"""


class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        n = len(security)
        up = [0 for _ in range(n)]
        down = [0 for _ in range(n)]

        for i in range(1, n):
            if security[i] <= security[i - 1]:
                down[i] = down[i - 1] + 1

        for i in range(n - 2, -1, -1):
            if security[i] <= security[i + 1]:
                up[i] = up[i + 1] + 1

        res = []
        for i in range(n):
            if up[i] >= time and down[i] >= time:
                res.append(i)

        return res
