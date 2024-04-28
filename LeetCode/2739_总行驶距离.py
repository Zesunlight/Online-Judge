# -*- coding: UTF-8 -*-
"""=================================================
Problem: 2739. 总行驶距离
Website: https://leetcode.cn/problems/total-distance-traveled/?envType=daily-question&envId=2024-04-28
Difficulty: 简单
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 63 ms
Memory Usage: 16.41 MB
=================================================="""


class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        distance = 0
        while mainTank >= 5 and additionalTank > 0:
            go = min(additionalTank, mainTank // 5)
            mainTank -= go * 4
            additionalTank -= go
            distance += go * 50
        distance += mainTank * 10
        return distance

    def distanceTraveled2(self, mainTank: int, additionalTank: int) -> int:
        # https://leetcode.cn/problems/total-distance-traveled/solutions/2751954/zong-xing-shi-ju-chi-by-leetcode-solutio-d63g/
        return 10 * (mainTank + min((mainTank - 1) // 4, additionalTank))
