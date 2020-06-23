# -*- coding: UTF-8 -*-
"""
=================================================
Problem: 面试题44. 数字序列中某一位的数字
Website: https://leetcode-cn.com/problems/shu-zi-xu-lie-zhong-mou-yi-wei-de-shu-zi-lcof/
Difficulty: 中等
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 44 ms, 在所有 Python3 提交中击败了40.70%的用户
Memory Usage: 13.7 MB, 在所有 Python3 提交中击败了100.00%的用户
=================================================="""


class Solution:
    """
    数字以0123456789101112131415…的格式序列化到一个字符序列中。
    在这个序列中，第5位（从下标0开始计数）是5，第13位是1，第19位是4，等等。
    请写一个函数，求任意第n位对应的数字。
    """
    def findNthDigit(self, n: int) -> int:
        long = 0
        if n <= 9:
            return n
        while n > 0:
            long += 1
            n -= long * (10 ** (long - 1) * 9)
        if n == 0:
            return 9
        n += long * (10 ** (long - 1) * 9)
        q, r = divmod(n, long)
        if r == 0:
            return (q - 1) % 10
        return int(str(10 ** (long - 1) + q)[r - 1])

"""
[0, 9]这个区间，长度为9，每个数字只有1位，共有9*1个数字
[10, 99]这个区间，长度为90，每个数字只有2位，共有90*2个数字
[100, 999]这个区间，长度为900，每个数字只有3位，共有900*3个数字

作者：woxiaosade
链接：https://leetcode-cn.com/problems/nth-digit/solution/zhao-gui-lu-jian-ji-de-jie-jue-ci-wen-ti-by-woxiao/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""
