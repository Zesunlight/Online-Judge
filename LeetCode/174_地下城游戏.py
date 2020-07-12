# -*- coding: UTF-8 -*-
"""
=================================================
Problem: 174. 地下城游戏
Website: https://leetcode-cn.com/problems/dungeon-game/
Difficulty: 困难
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 56 ms, 在所有 Python3 提交中击败了69.43%的用户
Memory Usage: 14.2 MB, 在所有 Python3 提交中击败了100.00%的用户
=================================================="""


class Solution:
    """
    一些恶魔抓住了公主（P）并将她关在了地下城的右下角。地下城是由 M x N 个房间组成的二维网格。
    我们英勇的骑士（K）最初被安置在左上角的房间里，他必须穿过地下城并通过对抗恶魔来拯救公主。
    骑士的初始健康点数为一个正整数。如果他的健康点数在某一时刻降至 0 或以下，他会立即死亡。
    有些房间由恶魔守卫，因此骑士在进入这些房间时会失去健康点数（若房间里的值为负整数，则表示骑士将损失健康点数）；
    其他房间要么是空的（房间里的值为 0），
    要么包含增加骑士健康点数的魔法球（若房间里的值为正整数，则表示骑士将增加健康点数）。
    为了尽快到达公主，骑士决定每次只向右或向下移动一步。
    """

    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        hp = [0 for _ in range(len(dungeon[0]))]
        hp[-1] = 1 if dungeon[-1][-1] >= 0 else (1 - dungeon[-1][-1])
        for i in range(len(hp) - 2, -1, -1):
            hp[i] = max(1, hp[i + 1] - dungeon[-1][i])
        
        for i in range(len(dungeon) - 2, -1, -1):
            for j in range(len(hp) - 1, -1, -1):
                if j == len(hp) - 1:
                    hp[j] = max(1, hp[j] - dungeon[i][j])
                else:
                    hp[j] = max(1, min(hp[j+1], hp[j]) - dungeon[i][j])
        return hp[0]

# https://leetcode-cn.com/problems/dungeon-game/solution/di-xia-cheng-you-xi-by-leetcode-solution/