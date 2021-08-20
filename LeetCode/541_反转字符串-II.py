# -*- coding: UTF-8 -*-
"""=================================================
Problem: 541. 反转字符串 II
Website: https://leetcode-cn.com/problems/reverse-string-ii/
Difficulty: 简单
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 36 ms
Memory Usage: 15 MB
=================================================="""

"""
给定一个字符串 s 和一个整数 k，从字符串开头算起，每 2k 个字符反转前 k 个字符。
如果剩余字符少于 k 个，则将剩余字符全部反转。
如果剩余字符小于 2k 但大于或等于 k 个，则反转前 k 个字符，其余字符保持原样。
"""


class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        r = ''
        keep = False
        for i in range(0, len(s), k):
            if not keep:
                r += s[i:min(i + k, len(s))][::-1]
                keep = True
            else:
                r += s[i:min(i + k, len(s))]
                keep = False
        return r

    def reverseStr2(self, s: str, k: int) -> str:
        # https://leetcode-cn.com/problems/reverse-string-ii/solution/fan-zhuan-zi-fu-chuan-ii-by-leetcode-sol-ua7s/
        t = list(s)
        for i in range(0, len(t), 2 * k):
            t[i: i + k] = reversed(t[i: i + k])
        return "".join(t)


if __name__ == '__main__':
    solution = Solution()
    print(solution.reverseStr("abcd", 2))
