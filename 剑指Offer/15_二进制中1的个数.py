# -*- coding: UTF-8 -*-
"""
=================================================
Problem: 面试题15. 二进制中1的个数
Website: https://leetcode-cn.com/problems/er-jin-zhi-zhong-1de-ge-shu-lcof/
Difficulty: 简单
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 52 ms, 在所有 Python3 提交中击败了77.67%的用户
Memory Usage: 23.2 MB, 在所有 Python3 提交中击败了100.00%的用户
=================================================="""


class Solution:
    """
    请实现一个函数，输入一个整数，输出该数二进制表示中 1 的个数。
    例如，把 9 表示成二进制是 1001，有 2 位是 1。因此，如果输入 9，则该函数输出 2。
    """
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            if n & 1 == 1:
                res += 1
            n = n >> 1
        return res


"""
对于任意数字 n ，将 n 和 n−1 做与运算，会把最后一个 1 的位变成 0

class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            res += 1
            n &= n - 1
        return res

作者：jyd
链接：https://leetcode-cn.com/problems/er-jin-zhi-zhong-1de-ge-shu-lcof/solution/mian-shi-ti-15-er-jin-zhi-zhong-1de-ge-shu-wei-yun/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""
