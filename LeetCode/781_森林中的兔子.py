# -*- coding: UTF-8 -*-
"""
=================================================
Problem: 781. 森林中的兔子
Website: https://leetcode-cn.com/problems/rabbits-in-forest/
Difficulty: 中等
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 44 ms
Memory Usage: 15 MB
=================================================="""


class Solution:
    """
    森林中，每个兔子都有颜色。其中一些兔子（可能是全部）告诉你还有多少其他的兔子和自己有相同的颜色。
    我们将这些回答放在 answers 数组里。
    返回森林中兔子的最少数量。
    """
    def numRabbits(self, answers: List[int]) -> int:
        num = defaultdict(int)
        for a in answers:
            num[a] += 1
        res = 0
        for a in num:
            if a == 0:
                res += num[a]
            else:
                res += ceil(num[a] / (a + 1)) * (a + 1)
        return res

    # https://leetcode-cn.com/problems/rabbits-in-forest/solution/ju-ji-ge-li-zi-xiang-xiang-jiu-ming-bai-4db5w/