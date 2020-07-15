# -*- coding: UTF-8 -*-
"""
=================================================
Problem: 面试题14- I. 剪绳子
Website: https://leetcode-cn.com/problems/jian-sheng-zi-lcof/
Difficulty: 中等
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 44 ms, 在所有 Python3 提交中击败了61.00%的用户
Memory Usage: 13.6 MB, 在所有 Python3 提交中击败了100.00%的用户
=================================================="""


class Solution:
    """
    给你一根长度为 n 的绳子，请把绳子剪成整数长度的 m 段（m、n都是整数，n>1并且m>1），
    每段绳子的长度记为 k[0],k[1]...k[m-1] 。
    请问 k[0]*k[1]*...*k[m-1] 可能的最大乘积是多少？
    """
    def cuttingRope(self, n: int) -> int:
        res = 0
        for i in range(2, n + 1):
            res = max(res, self.cut_to_m(n, i))
        return res


    def cut_to_m(self, n, m):
        k = n // m
        if n % m == 0:
            return k ** m
        else:
            return (k + 1) ** (n - k * m) * k ** (m - n + k * m)


"""
class Solution:
    def cuttingRope(self, n: int) -> int:
        if n <= 3: return n - 1
        a, b = n // 3, n % 3
        if b == 0: return int(math.pow(3, a))
        if b == 1: return int(math.pow(3, a - 1) * 4)
        return int(math.pow(3, a) * 2)

作者：jyd
链接：https://leetcode-cn.com/problems/jian-sheng-zi-lcof/solution/mian-shi-ti-14-i-jian-sheng-zi-tan-xin-si-xiang-by/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""