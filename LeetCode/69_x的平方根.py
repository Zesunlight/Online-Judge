# -*- coding: UTF-8 -*-
"""=================================================
Problem: 69. x 的平方根
Website: https://leetcode-cn.com/problems/sqrtx/
Difficulty: 简单
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 64 ms
Memory Usage: 14.9 MB
=================================================="""
from math import log, e

"""
实现int sqrt(int x)函数。
计算并返回x的平方根，其中 x 是非负整数。
由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。
"""


class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        c = int(pow(e, log(x) / 2))
        return c if (c + 1) ** 2 > x else c + 1

    def mySqrt2(self, x: int) -> int:
        # https://leetcode-cn.com/problems/sqrtx/solution/x-de-ping-fang-gen-by-leetcode-solution/
        l, r, ans = 0, x, -1
        while l <= r:
            mid = (l + r) // 2
            if mid * mid <= x:
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        return ans

    def mySqrt3(self, x: int) -> int:
        # https://leetcode-cn.com/problems/sqrtx/solution/x-de-ping-fang-gen-by-leetcode-solution/
        # 牛顿迭代法
        if x == 0:
            return 0

        C, x0 = float(x), float(x)
        while True:
            xi = 0.5 * (x0 + C / x0)
            if abs(x0 - xi) < 1e-7:
                break
            x0 = xi

        return int(x0)


if __name__ == '__main__':
    solution = Solution()
    print(solution.mySqrt(4))
