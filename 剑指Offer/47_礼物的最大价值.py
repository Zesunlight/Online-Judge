# -*- coding: UTF-8 -*-
"""
=================================================
Problem: 面试题47. 礼物的最大价值
Website: https://leetcode-cn.com/problems/li-wu-de-zui-da-jie-zhi-lcof/
Difficulty: 中等
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 64 ms, 在所有 Python3 提交中击败了44.98%的用户
Memory Usage: 15.5 MB, 在所有 Python3 提交中击败了100.00%的用户
=================================================="""


class Solution:
    """
    在一个 m*n 的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值（价值大于 0）。
    你可以从棋盘的左上角开始拿格子里的礼物，并每次向右或者向下移动一格、直到到达棋盘的右下角。
    给定一个棋盘及其上面的礼物的价值，请计算你最多能拿到多少价值的礼物？
    """
    def maxValue(self, grid: List[List[int]]) -> int:
        dp = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        temp = 0
        for i in range(len(grid)):
            temp += grid[i][0]
            dp[i][0] = temp
        temp = grid[0][0]
        for i in range(1, len(grid[0])):
            temp += grid[0][i]
            dp[0][i] = temp
        
        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                dp[i][j] = grid[i][j] + max(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]


class Solution_2:
    def maxValue(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        for j in range(1, n): # 初始化第一行
            grid[0][j] += grid[0][j - 1]
        for i in range(1, m): # 初始化第一列
            grid[i][0] += grid[i - 1][0]
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += max(grid[i][j - 1], grid[i - 1][j])
        return grid[-1][-1]
"""
可以将原矩阵 grid 用作 dp 矩阵，即直接在 grid 上修改即可。

作者：jyd
链接：https://leetcode-cn.com/problems/li-wu-de-zui-da-jie-zhi-lcof/solution/mian-shi-ti-47-li-wu-de-zui-da-jie-zhi-dong-tai-gu/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""
