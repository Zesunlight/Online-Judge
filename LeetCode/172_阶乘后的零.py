# -*- coding: UTF-8 -*-
"""=================================================
Problem: 172. 阶乘后的零
Website: https://leetcode-cn.com/problems/factorial-trailing-zeroes/submissions/
Difficulty: 中等
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 32 ms
Memory Usage: 14.9 MB
=================================================="""

"""
给定一个非负整数 n ，返回 n! 结果中尾随零的数量。
"""


class Solution:
    def trailingZeroes(self, n: int) -> int:
        zero = 0
        while n > 0:
            n = n // 5
            zero += n
        return zero


if __name__ == '__main__':
    solution = Solution()
    print(solution.trailingZeroes(10))
