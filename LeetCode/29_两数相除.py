# -*- coding: UTF-8 -*-
"""=================================================
Problem: 29. 两数相除
Website: https://leetcode-cn.com/problems/divide-two-integers/
Difficulty: 中等
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 36 ms
Memory Usage: 15 MB
=================================================="""
from typing import List
from pprint import pprint

"""
给定两个整数，被除数dividend和除数divisor。
将两数相除，要求不使用乘法、除法和 mod 运算符。
返回被除数dividend除以除数divisor得到的商。
整数除法的结果应当截去（truncate）其小数部分，
例如：truncate(8.345) = 8 以及 truncate(-2.7335) = -2
"""


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2147483648:
            if divisor == -1:
                return 2147483647

        sign = 1
        if dividend < 0 and divisor < 0:
            dividend = -dividend
            divisor = -divisor
        elif dividend < 0:
            sign = -1
            dividend = -dividend
        elif divisor < 0:
            sign = -1
            divisor = -divisor

        if dividend < divisor:
            return 0

        base = 1
        d = divisor
        while d < dividend:
            d += d
            base += base

        return ((base >> 1) + self.divide(dividend - (d >> 1), divisor)) * sign


if __name__ == '__main__':
    solution = Solution()
    print(solution.divide(1, 1))
    print(3)
