# -*- coding: UTF-8 -*-
"""
=================================================
Problem: 867. 转置矩阵
Website: https://leetcode-cn.com/problems/transpose-matrix/
Difficulty: 简单
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 44 ms
Memory Usage: 15.3 MB
=================================================="""


class Solution:
    """
    给你一个二维整数数组 matrix， 返回 matrix 的 转置矩阵 。
    矩阵的 转置 是指将矩阵的主对角线翻转，交换矩阵的行索引与列索引。
    """
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        return list(zip(*matrix))

    def transpose2(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        transposed = [[0] * m for _ in range(n)]
        for i in range(m):
            for j in range(n):
                transposed[j][i] = matrix[i][j]
        return transposed

        # 作者：LeetCode-Solution
        # 链接：https://leetcode-cn.com/problems/transpose-matrix/solution/zhuan-zhi-ju-zhen-by-leetcode-solution-85s2/
        # 来源：力扣（LeetCode）
        # 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
