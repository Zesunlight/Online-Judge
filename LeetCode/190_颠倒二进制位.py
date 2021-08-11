# -*- coding: UTF-8 -*-
"""=================================================
Problem: 190. 颠倒二进制位
Website: https://leetcode-cn.com/problems/reverse-bits/
Difficulty: 简单
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 32 ms
Memory Usage: 14.9 MB
=================================================="""


"""
    颠倒给定的 32 位无符号整数的二进制位。
"""


class Solution:
    def reverseBits(self, n: int) -> int:
        return int(str(bin(n))[2:].zfill(32)[::-1], 2)


if __name__ == '__main__':
    s = Solution()
    print(s.reverseBits(0b00000010100101000001111010011100))
