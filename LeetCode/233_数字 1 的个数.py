# -*- coding: UTF-8 -*-
"""
=================================================
Problem: 233. 数字 1 的个数
Website: https://leetcode-cn.com/problems/number-of-digit-one/
Difficulty: 困难
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 44 ms, 在所有 Python3 提交中击败了40.60%的用户
Memory Usage: 13.7 MB, 在所有 Python3 提交中击败了50.00%的用户
=================================================="""


class Solution:
    """
    给定一个整数 n，计算所有小于等于 n 的非负整数中数字 1 出现的个数。
    """
    def countDigitOne(self, n: int) -> int:
        if n <= 9:
            return 1 if n > 0 else 0
        res = 0
        sn = str(n)
        if sn[0] == '1':
            res += int(sn[1:]) + 1
        else:
            res += 10 ** (len(sn) - 1)

        for i in range(1, len(sn) - 1):
            if sn[i] == '0':
                res += int(sn[:i]) * 10 ** (len(sn) - i - 1)
            elif sn[i] == '1':
                res += int(sn[:i]) * 10 ** (len(sn) - i - 1) + int(sn[i+1:]) + 1
            else:
                res += (int(sn[:i]) + 1) * 10 ** (len(sn) - i - 1)

        res += int(sn[:-1]) + (0 if sn[-1] == '0' else 1)
        return res


"""
class Solution:
    def countDigitOne(self, n: int) -> int:
        digit, res = 1, 0
        high, cur, low = n // 10, n % 10, 0
        while high != 0 or cur != 0:
            if cur == 0: res += high * digit
            elif cur == 1: res += high * digit + low + 1
            else: res += (high + 1) * digit
            low += cur * digit
            cur = high % 10
            high //= 10
            digit *= 10
        return res

作者：jyd
链接：https://leetcode-cn.com/problems/1nzheng-shu-zhong-1chu-xian-de-ci-shu-lcof/solution/mian-shi-ti-43-1n-zheng-shu-zhong-1-chu-xian-de-2/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""
