# -*- coding: UTF-8 -*-
"""=================================================
Problem: 2582. 递枕头
Website: https://leetcode.cn/problems/pass-the-pillow/description
Difficulty: 简单
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 44 ms
Memory Usage: 15.61 MB
=================================================="""
from typing import List, Dict, Set
from collections import defaultdict, deque, Counter
from itertools import product
from pprint import pprint
import copy

"""
n 个人站成一排，按从 1 到 n 编号。

最初，排在队首的第一个人拿着一个枕头。每秒钟，拿着枕头的人会将枕头传递给队伍中的下一个人。
一旦枕头到达队首或队尾，传递方向就会改变，队伍会继续沿相反方向传递枕头。

例如，当枕头到达第 n 个人时，TA 会将枕头传递给第 n - 1 个人，然后传递给第 n - 2 个人，依此类推。
给你两个正整数 n 和 time ，返回 time 秒后拿着枕头的人的编号。
"""


class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        if n == 1:
            return 1

        cycle = 2 * n - 2
        remain = (time + 1) % cycle
        if remain == 0:
            return 2

        if remain <= n:
            return remain
        return 2 * n - remain

    def passThePillow2(self, n: int, time: int) -> int:
        # https://leetcode.cn/problems/pass-the-pillow/solutions/2451117/di-zhen-tou-by-leetcode-solution-kl5e/
        time %= (n - 1) * 2
        return time + 1 if time < n else n * 2 - time - 1

    def passThePillow3(self, n: int, time: int) -> int:
        # https://leetcode.cn/problems/pass-the-pillow/solutions/2459198/python3javacgorust-yi-ti-shuang-jie-mo-n-kclg/
        k, mod = divmod(time, n - 1)
        return n - mod if k & 1 else mod + 1


if __name__ == '__main__':
    solution = Solution()
    print(solution.passThePillow(4, 5))
