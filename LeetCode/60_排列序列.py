# -*- coding: UTF-8 -*-
"""=================================================
Problem: 60. 排列序列
Website: https://leetcode-cn.com/problems/permutation-sequence/
Difficulty: 困难
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 32 ms
Memory Usage: 15 MB
=================================================="""
from math import floor, ceil

"""
给出集合[1,2,3,...,n]，其所有元素共有n! 种排列。
按大小顺序列出所有排列情况，并一一标记，当n = 3 时, 所有排列如下：
"123"
"132"
"213"
"231"
"312"
"321"
给定n 和k，返回第k个排列。
"""


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        factorial = [1] * n
        for i in range(2, n):
            factorial[i] = factorial[i - 1] * i

        candidate = [1] * n
        ans = []
        for i in range(n - 1, -1, -1):
            left = ceil(k / factorial[i])
            k -= (left - 1) * factorial[i]
            find = 0
            start = 0
            while find < left:
                if candidate[start] == 1:
                    find += 1
                start += 1
            candidate[start - 1] = 0
            ans.append(str(start))

        return ''.join(ans)

    def getPermutation2(self, n: int, k: int) -> str:
        from itertools import permutations
        index = 1
        for p in permutations(list(range(1, n + 1))):
            if index == k:
                return ''.join([str(x) for x in p])
            index += 1


if __name__ == '__main__':
    solution = Solution()
    print(solution.getPermutation(4, 9))
