# -*- coding: UTF-8 -*-
"""=================================================
Problem: 1583. 统计不开心的朋友
Website: https://leetcode-cn.com/problems/count-unhappy-friends/
Difficulty: 中等
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 580 ms
Memory Usage: 26.1 MB
=================================================="""
from typing import List
from pprint import pprint

"""
给你一份 n 位朋友的亲近程度列表，其中 n 总是 偶数 。
对每位朋友 i，preferences[i] 包含一份 按亲近程度从高到低排列 的朋友列表。
换句话说，排在列表前面的朋友与 i 的亲近程度比排在列表后面的朋友更高。每个列表中的朋友均以 0 到 n-1 之间的整数表示。
所有的朋友被分成几对，配对情况以列表 pairs 给出，其中 pairs[i] = [xi, yi] 表示 xi 与 yi 配对，且 yi 与 xi 配对。
但是，这样的配对情况可能会是其中部分朋友感到不开心。在 x 与 y 配对且 u 与 v 配对的情况下，如果同时满足下述两个条件，x 就会不开心：
    x 与 u 的亲近程度胜过 x 与 y，且u 与 x 的亲近程度胜过 u 与 v
返回 不开心的朋友的数目 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/count-unhappy-friends
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def unhappyFriends(self,
                       n: int,
                       preferences: List[List[int]],
                       pairs: List[List[int]]) -> int:
        love = [[-1 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                love[i][j] = preferences[i].index(j)

        # order = [[0] * n for _ in range(n)]
        # for i in range(n):
        #     for j in range(n - 1):
        #         order[i][preferences[i][j]] = j

        meet = [0 for _ in range(n)]
        for x, y in pairs:
            meet[x] = y
            meet[y] = x

        unhappy = 0
        for x in range(n):
            y = meet[x]
            stand = love[x][y]
            for i in range(stand):
                c = preferences[x][i]
                if love[c][x] < love[c][meet[c]]:
                    unhappy += 1
                    break

        return unhappy


if __name__ == '__main__':
    solution = Solution()
    print(solution.unhappyFriends(n=2, preferences=[[1], [0]], pairs=[[1, 0]]))
