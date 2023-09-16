# -*- coding: UTF-8 -*-
"""=================================================
Problem: 36. 有效的数独
Website: https://leetcode.cn/problems/valid-sudoku/description/
Difficulty: 中等
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 68 ms
Memory Usage: 15.9 MB
=================================================="""
from typing import List, Dict, Set
from collections import defaultdict, deque, Counter
from itertools import product

"""
请你判断一个 9 x 9 的数独是否有效。只需要 根据以下规则 ，验证已经填入的数字是否有效即可。
数字 1-9 在每一行只能出现一次。
数字 1-9 在每一列只能出现一次。
数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。

注意：
一个有效的数独（部分已被填充）不一定是可解的。
只需要根据以上规则，验证已经填入的数字是否有效即可。
空白格用 '.' 表示。
"""


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def valid(digits: Counter):
            del digits['.']
            for d in digits:
                if digits[d] > 1:
                    return False
            return True

        for i in range(9):
            if not valid(Counter(board[i])):
                return False
            if not valid(Counter([line[i] for line in board])):
                return False

        for i in range(3):
            for j in range(3):
                block = [l[j * 3:j * 3 + 3] for l in board[i * 3:i * 3 + 3]]
                if not valid(Counter([k for line in block for k in line])):
                    return False

        return True


if __name__ == '__main__':
    solution = Solution()
    print(solution.isValidSudoku(
        [[".", ".", "4", ".", ".", ".", "6", "3", "."],
         [".", ".", ".", ".", ".", ".", ".", ".", "."],
         ["5", ".", ".", ".", ".", ".", ".", "9", "."],
         [".", ".", ".", "5", "6", ".", ".", ".", "."],
         ["4", ".", "3", ".", ".", ".", ".", ".", "1"],
         [".", ".", ".", "7", ".", ".", ".", ".", "."],
         [".", ".", ".", "5", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", ".", "."]]))
