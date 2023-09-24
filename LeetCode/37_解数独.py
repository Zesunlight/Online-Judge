# -*- coding: UTF-8 -*-
"""=================================================
Problem: 37. 解数独
Website: https://leetcode.cn/problems/sudoku-solver/description/
Difficulty: 困难
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 304 ms
Memory Usage: 16.1 MB
=================================================="""
from typing import List, Dict, Set
from collections import defaultdict, deque, Counter
from itertools import product
from pprint import pprint
import copy

"""
编写一个程序，通过填充空格来解决数独问题。

数独的解法需 遵循如下规则：

数字 1-9 在每一行只能出现一次。
数字 1-9 在每一列只能出现一次。
数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。
数独部分空格内已填入了数字，空白格用 '.' 表示。
"""


class Solution:
    solve = False

    def solveSudoku(self, board: List[List[str]]) -> None:
        self.dfs(board)

    def dfs(self, board: List[List[str]]):
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    if i == 8 and j == 8:
                        self.solve = True
                    continue
                suitable = self.candidate(board, i, j)
                for suit in suitable:
                    board[i][j] = suit
                    self.dfs(board)
                    if self.solve:
                        return
                    board[i][j] = '.'
                return

    def candidate(self, board: List[List[str]], i: int, j: int) -> List[str]:
        row = set(board[i])
        column = set([x[j] for x in board])
        block = set()
        for x in range(i // 3 * 3, i // 3 * 3 + 3):
            for y in range(j // 3 * 3, j // 3 * 3 + 3):
                block.add(board[x][y])
        fill = (row | column | block)
        return list(set([str(z) for z in range(1, 10)]) - fill)


if __name__ == '__main__':
    solution = Solution()
    answer = [["5", "3", "4", "6", "7", "8", "9", "1", "2"],
              ["6", "7", "2", "1", "9", "5", "3", "4", "8"],
              ["1", "9", "8", "3", "4", "2", "5", "6", "7"],
              ["8", "5", "9", "7", "6", "1", "4", "2", "3"],
              ["4", "2", "6", "8", "5", "3", "7", "9", "1"],
              ["7", "1", "3", "9", "2", "4", "8", "5", "6"],
              ["9", "6", "1", "5", "3", "7", "2", "8", "4"],
              ["2", "8", "7", "4", "1", "9", "6", "3", "5"],
              ["3", "4", "5", "2", "8", "6", "1", "7", "9"]]
    question = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
                ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                [".", "9", "8", ".", ".", ".", ".", "6", "."],
                ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                [".", "6", ".", ".", ".", ".", "2", "8", "."],
                [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    print(solution.solveSudoku(question))
    pprint(question)
