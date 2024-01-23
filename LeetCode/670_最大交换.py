# -*- coding: UTF-8 -*-
"""=================================================
Problem: 670. 最大交换
Website: https://leetcode.cn/problems/maximum-swap/description/
Difficulty: 中等
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 50 ms
Memory Usage: 16.31 MB
=================================================="""
from typing import List, Dict, Set, Optional
from collections import defaultdict, deque, Counter
from itertools import product
from pprint import pprint
import copy

"""
给定一个非负整数，你至多可以交换一次数字中的任意两位。返回你能得到的最大值。
"""


class ListNode:
    def __init__(self, val: int = 0, next=None):
        self.val = val
        self.next = next


class Solution:
    def maximumSwap(self, num: int) -> int:
        split = list(str(num))
        order = sorted(enumerate(split), key=lambda x: (-int(x[1]), x[0]))
        left, right = 0, 0
        for i in range(len(split) - 1):
            if split[i] != order[i][1]:
                left = i
                break
        right = left
        while right < len(split)-1 and order[right][1] == order[right+1][1]:
            right += 1
        split[left], split[order[right][0]] = split[order[right][0]], split[left]
        return int(''.join(split))

    def maximumSwap2(self, num: int) -> int:
        # https://leetcode.cn/problems/maximum-swap/solutions/1818457/zui-da-jiao-huan-by-leetcode-solution-lnd5/
        # https://leetcode.cn/problems/maximum-swap/solutions/1/yi-ci-bian-li-jian-ji-xie-fa-pythonjavac-c9b1
        s = list(str(num))
        n = len(s)
        maxIdx = n - 1
        idx1 = idx2 = -1
        for i in range(n - 1, -1, -1):
            if s[i] > s[maxIdx]:
                maxIdx = i
            elif s[i] < s[maxIdx]:
                idx1, idx2 = i, maxIdx
        if idx1 < 0:
            return num
        s[idx1], s[idx2] = s[idx2], s[idx1]
        return int(''.join(s))
    
    def maximumSwap3(self, num: int) -> int:
        # https://leetcode.cn/problems/maximum-swap/solutions/1818457/zui-da-jiao-huan-by-leetcode-solution-lnd5/
        ans = num
        s = list(str(num))
        for i in range(len(s)):
            for j in range(i):
                s[i], s[j] = s[j], s[i]
                ans = max(ans, int(''.join(s)))
                s[i], s[j] = s[j], s[i]
        return ans


if __name__ == '__main__':
    solution = Solution()
    # 98368 27367 99901
    result = solution.maximumSwap(98368)
    print(result)
