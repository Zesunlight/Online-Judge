# -*- coding: UTF-8 -*-
"""
=================================================
Problem: 231. 2 的幂
Website: https://leetcode-cn.com/problems/power-of-two/
Difficulty: 简单
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 52 ms
Memory Usage: 15 MB
=================================================="""


class Solution:
    """
    给你一个整数 n，请你判断该整数是否是 2 的幂次方。如果是，返回 true ；否则，返回 false 。
    如果存在一个整数 x 使得n == 2x ，则认为 n 是 2 的幂次方。
    """

    def isPowerOfTwo(self, n: int) -> bool:
        b = bin(n)[2:]
        if b[0] != '1':
            return False
        if '1' in b[1:]:
            return False
        return True

    def isPowerOfTwo2(self, n: int) -> bool:
        return n > 0 and (n & (n - 1)) == 0

    def isPowerOfTwo3(self, n: int) -> bool:
        return n > 0 and (n & -n) == n

    BIG = 2**30
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and Solution.BIG % n == 0


    """
    作者：LeetCode-Solution
    链接：https://leetcode-cn.com/problems/power-of-two/solution/2de-mi-by-leetcode-solution-rny3/
    来源：力扣（LeetCode）
    著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    """