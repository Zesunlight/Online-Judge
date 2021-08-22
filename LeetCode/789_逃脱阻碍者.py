# -*- coding: UTF-8 -*-
"""=================================================
Problem: 789. 逃脱阻碍者
Website: https://leetcode-cn.com/problems/escape-the-ghosts/
Difficulty: 中等
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 36 ms
Memory Usage: 15.1 MB
=================================================="""
from typing import List

"""
你在进行一个简化版的吃豆人游戏。你从 [0, 0] 点开始出发，你的目的地是target = [xtarget, ytarget] 。
地图上有一些阻碍者，以数组 ghosts 给出，第 i 个阻碍者从ghosts[i] = [xi, yi]出发。所有输入均为 整数坐标 。
每一回合，你和阻碍者们可以同时向东，西，南，北四个方向移动，每次可以移动到距离原位置 1 个单位 的新位置。
当然，也可以选择 不动 。所有动作 同时 发生。
如果你可以在任何阻碍者抓住你 之前 到达目的地（阻碍者可以采取任意行动方式），则被视为逃脱成功。
如果你和阻碍者同时到达了一个位置（包括目的地）都不算是逃脱成功。
只有在你有可能成功逃脱时，输出 true ；否则，输出 false 。
"""


class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        dis_tar = self.distance(target, [0, 0])
        dis_army = dis_tar + 1
        for g in ghosts:
            dis_army = min(dis_army, self.distance(target, g))
        return dis_tar < dis_army

    def distance(self, a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])


if __name__ == '__main__':
    solution = Solution()
    print(solution.escapeGhosts(ghosts=[[5, 0], [-10, -2], [0, -5], [-2, -2], [-7, 1]], target=[7, 7]))
