# -*- coding: UTF-8 -*-
"""=================================================
Problem: 1329. 将矩阵按对角线排序
Website: https://leetcode.cn/problems/sort-the-matrix-diagonally/description/?envType=daily-question&envId=2024-04-28
Difficulty: 简单
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 47 ms
Memory Usage: 16.89 MB
=================================================="""
from typing import List


class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])

        for i in range(m):
            temp = []
            x, y = i, 0
            while (0 <= x < m) and (0 <= y < n):
                temp.append(mat[x][y])
                x += 1
                y = x - i
            temp.sort(reverse=True)
            x, y = i, 0
            while (0 <= x < m) and (0 <= y < n):
                mat[x][y] = temp.pop()
                x += 1
                y = x - i

        for i in range(1, n):
            temp = []
            x, y = 0, i
            while (0 <= x < m) and (0 <= y < n):
                temp.append(mat[x][y])
                x += 1
                y = x + i
            temp.sort(reverse=True)
            x, y = 0, i
            while (0 <= x < m) and (0 <= y < n):
                mat[x][y] = temp.pop()
                x += 1
                y = x + i

        return mat

    def diagonalSort2(self, mat: List[List[int]]) -> List[List[int]]:
        # https://leetcode.cn/problems/sort-the-matrix-diagonally/solutions/2754949/jiang-ju-zhen-an-dui-jiao-xian-pai-xu-by-fsf0/
        n = len(mat)
        m = len(mat[0])
        diag = [[] for _ in range(m + n)]
        for i in range(n):
            for j in range(m):
                # mat[i][j] 属于第 i - j + m 条对角线
                diag[i - j + m].append(mat[i][j])
        for d in diag:
            d.sort(reverse=True)
        for i in range(n):
            for j in range(m):
                mat[i][j] = diag[i - j + m].pop()
        return mat


if __name__ == '__main__':
    s = Solution()
    print(s.diagonalSort2([[3,3,1,1],[2,2,1,2],[1,1,1,2]]))

