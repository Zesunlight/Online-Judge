# -*- coding: UTF-8 -*-
"""
=================================================
Problem: 5738. K 进制表示下的各位数字总和
Website: https://leetcode-cn.com/problems/sum-of-digits-in-base-k/
Difficulty: 简单
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 44 ms
Memory Usage: 16.1 MB
=================================================="""


class Solution:
    """
    给你一个整数 n（10 进制）和一个基数 k ，请你将 n 从 10 进制表示转换为 k 进制表示，计算并返回转换后各位数字的 总和 。
    转换后，各位数字应当视作是 10 进制数字，且它们的总和也应当按 10 进制表示返回。
    """

    def sumBase(self, n: int, k: int) -> int:
        return sum([int(i) for i in self.base(n, k)])

    def base(self, n, b):
        # 十进制转b进制
        if n == 0:
            return '0'

        trans = [str(i) for i in range(10)]
        trans.extend([chr(i) for i in range(ord('A'), ord('Z') + 1)])
        res = ''
        while n:
            n, r = divmod(n, b)
            res += trans[r]
        return res[::-1]

    def sumBase2(self, n: int, k: int) -> int:
        res = 0
        while n:
            res += n % k
            n //= k
        return res
    # 作者：LeetCode-Solution
    # 链接：https://leetcode-cn.com/problems/sum-of-digits-in-base-k/solution/k-jin-zhi-biao-shi-xia-de-ge-wei-shu-zi-4ltwc/
    # 来源：力扣（LeetCode）
    # 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
