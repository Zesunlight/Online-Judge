# -*- coding: UTF-8 -*-
"""
=================================================
Problem: 73. 矩阵置零
Website: https://leetcode-cn.com/problems/set-matrix-zeroes/
Difficulty: 中等
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 52 ms, 在所有 Python3 提交中击败了66.50%的用户
Memory Usage: 14.2 MB, 在所有 Python3 提交中击败了7.69%的用户
=================================================="""


class Solution:
    """
    给定一个 m x n 的矩阵，如果一个元素为 0，则将其所在行和列的所有元素都设为 0。请使用原地算法。
    """
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r, c = [], []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    r.append(i)
                    c.append(j)
        for i in r:
            for j in range(len(matrix[0])):
                matrix[i][j] = 0
        for i in c:
            for j in range(len(matrix)):
                matrix[j][i] = 0

"""
我们可以用每行和每列的第一个元素作为标记，这个标记用来表示这一行或者这一列是否需要赋零。
这些标签用于之后对矩阵的更新，如果某行的第一个元素为零就将整行置零，如果某列的第一个元素为零就将整列置零。
"""