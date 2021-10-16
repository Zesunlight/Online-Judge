# -*- coding: UTF-8 -*-
"""=================================================
Problem: 171. Excel 表列序号
Website: https://leetcode-cn.com/problems/excel-sheet-column-number/
Difficulty: 简单
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 36 ms
Memory Usage: 14.8 MB
=================================================="""

"""
给你一个字符串 columnTitle ，表示 Excel 表格中的列名称。返回该列名称对应的列序号。
"""


class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        n = len(columnTitle)
        r = 0
        for i in range(n):
            r += 26 ** (n - i - 1) * (ord(columnTitle[i]) - ord('A') + 1)
        return r


if __name__ == '__main__':
    solution = Solution()
    print(solution.titleToNumber('FXSHRXW'))
