# -*- coding: UTF-8 -*-
"""=================================================
Problem: 576. 出界的路径数
Website: https://leetcode-cn.com/problems/out-of-boundary-paths/
Difficulty: 中等
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 112 ms
Memory Usage: 16.5 MB
=================================================="""
from typing import List
from pprint import pprint

"""
给你一个大小为 m x n 的网格和一个球。球的起始坐标为 [startRow, startColumn] 。
你可以将球移到在四个方向上相邻的单元格内（可以穿过网格边界到达网格之外）。
你 最多 可以移动 maxMove 次球。
给你五个整数 m、n、maxMove、startRow 以及 startColumn ，找出并返回可以将球移出边界的路径数量。
因为答案可能非常大，返回对 109 + 7 取余 后的结果。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/out-of-boundary-paths
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        way = [[[0] * n for _ in range(m)] for _ in range(maxMove + 1)]
        way[0][startRow][startColumn] = 1
        out = 0
        direct = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        MOD = int(1e9 + 7)

        for i in range(maxMove):
            for j in range(m):
                for k in range(n):
                    if way[i][j][k] > 0:
                        # for j1, k1 in [(j - 1, k), (j + 1, k), (j, k - 1), (j, k + 1)]:
                        for x, y in direct:
                            if (0 <= j + x < m) and (0 <= k + y < n):
                                way[i + 1][j + x][k + y] = (way[i][j][k] + way[i + 1][j + x][k + y]) % MOD
                            else:
                                out = (out + way[i][j][k]) % MOD

        return out


if __name__ == '__main__':
    solution = Solution()
    print(solution.findPaths(m=1, n=3, maxMove=3, startRow=0, startColumn=1))
