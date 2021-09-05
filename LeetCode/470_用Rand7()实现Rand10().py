# -*- coding: UTF-8 -*-
"""=================================================
Problem: 470. 用 Rand7() 实现 Rand10()
Website: https://leetcode-cn.com/problems/implement-rand10-using-rand7/
Difficulty: 中等
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 768 ms
Memory Usage: 17.5 MB
=================================================="""
from typing import List

"""
已有方法 rand7 可生成 1 到 7 范围内的均匀随机整数，试写一个方法 rand10 生成 1 到 10 范围内的均匀随机整数。
不要使用系统的 Math.random() 方法。
"""


# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        while 1:
            a = rand7()
            b = rand7()
            if a == b:
                return a
            elif a == 1 and b == 2:
                return 8
            elif a == 2 and b == 3:
                return 9
            elif a == 3 and b == 4:
                return 10
    
    def rand10_2(self) -> int:
        # https://leetcode-cn.com/problems/implement-rand10-using-rand7/solution/yong-rand7-shi-xian-rand10-by-leetcode-s-qbmd/
        while True:
            row = rand7()
            col = rand7()
            idx = (row - 1) * 7 + col
            if idx <= 40:
                return 1 + (idx - 1) % 10
