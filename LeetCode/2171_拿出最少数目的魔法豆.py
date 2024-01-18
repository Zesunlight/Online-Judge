# -*- coding: UTF-8 -*-
"""=================================================
Problem: 2171. 拿出最少数目的魔法豆
Website: https://leetcode.cn/problems/removing-minimum-number-of-magic-beans/description
Difficulty: 中等
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 419 ms
Memory Usage: 34.86 MB
=================================================="""
from typing import List, Dict, Set, Optional
from collections import defaultdict, deque, Counter
from itertools import product
from pprint import pprint
import copy

"""
给定一个 正整数 数组 beans ，其中每个整数表示一个袋子里装的魔法豆的数目。

请你从每个袋子中 拿出 一些豆子（也可以 不拿出），使得剩下的 非空 袋子中（即 至少还有一颗 魔法豆的袋子）魔法豆的数目 相等。一旦把魔法豆从袋子中取出，你不能再将它放到任何袋子中。

请返回你需要拿出魔法豆的 最少数目。
"""


class ListNode:
    def __init__(self, val: int = 0, next=None):
        self.val = val
        self.next = next


class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        n = len(beans)
        if n == 1:
            return 0

        beans.sort()
        back_presum = list(beans)
        for i in range(n-2, -1, -1):
            back_presum[i] = back_presum[i] + back_presum[i+1]
        presum = list(beans)
        for i in range(1, n):
            presum[i] = presum[i] + presum[i-1]
        
        res = back_presum[0] - beans[0] * n
        for i in range(1, n):
            res = min(res, presum[i-1] + back_presum[i] - beans[i] * (n - i))
        return res
    
    def minimumRemoval2(self, beans: List[int]) -> int:
        # https://leetcode.cn/problems/removing-minimum-number-of-magic-beans/solutions/1270306/na-chu-zui-shao-shu-mu-de-mo-fa-dou-by-l-dhsl/
        n = len(beans)
        beans.sort()
        total = sum(beans) # 豆子总数
        res = total # 最少需要移除的豆子数
        for i in range(n):
            res = min(res, total - beans[i] * (n - i))
        return res


if __name__ == '__main__':
    solution = Solution()
    result = solution.minimumRemoval([4,1,6,5])
    print(result)
