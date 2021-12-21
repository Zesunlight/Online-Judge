# -*- coding: UTF-8 -*-
"""=================================================
Problem: 1154. 一年中的第几天
Website: https://leetcode-cn.com/problems/day-of-the-year/
Difficulty: 简单
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 72 ms
Memory Usage: 15 MB
=================================================="""

"""
给你一个字符串 date ，按 YYYY-MM-DD 格式表示一个 现行公元纪年法 日期。
请你计算并返回该日期是当年的第几天。
通常情况下，我们认为 1 月 1 日是每年的第 1 天，1 月 2 日是每年的第 2 天，依此类推。
每个月的天数与现行公元纪年法（格里高利历）一致。
"""

class Solution:
    def dayOfYear(self, date: str) -> int:
        year, month, day = map(int, date.split('-'))
        m = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
            m[1] += 1
        d = 0
        d += sum(m[:month-1])
        d += day
        return d


if __name__ == '__main__':
    solution = Solution()
    print(solution.dayOfYear('2004-03-1'))
