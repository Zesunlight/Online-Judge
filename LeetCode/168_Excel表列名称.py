# -*- coding: utf-8 -*-
"""=================================================
Problem: 168. Excel表列名称
Website: https://leetcode-cn.com/problems/excel-sheet-column-title/
Difficulty: 简单
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 32 ms
Memory Usage: 15 MB
=================================================="""

"""
给你一个整数 columnNumber ，返回它在 Excel 表中相对应的列名称。
"""

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = ''
        while columnNumber > 0:
            columnNumber, remainder = divmod(columnNumber, 26)
            if remainder == 0:
                columnNumber -= 1
            result += self.convertToCharacter(remainder)
        return result[::-1]

    def convertToCharacter(self, characterNumber: int) -> str:
        if characterNumber < 0 or characterNumber >= 26:
            raise ValueError('parameter invalid')
        return chr(ord('A') + (characterNumber + 25) % 26)


class Solution2:
    # https://leetcode-cn.com/problems/excel-sheet-column-title/solution/excelbiao-lie-ming-cheng-by-leetcode-sol-hgj4/
    def convertToTitle(self, columnNumber: int) -> str:
        ans = list()
        while columnNumber > 0:
            columnNumber -= 1
            ans.append(chr(columnNumber % 26 + ord("A")))
            columnNumber //= 26
        return "".join(ans[::-1])


if __name__ == '__main__':
    solution = Solution()
    print(solution.convertToTitle(2147483647))
