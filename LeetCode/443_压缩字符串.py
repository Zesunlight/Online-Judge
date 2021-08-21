# -*- coding: UTF-8 -*-
"""=================================================
Problem: 443. 压缩字符串
Website: https://leetcode-cn.com/problems/string-compression/
Difficulty: 中等
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 32 ms
Memory Usage: 15.2 MB
=================================================="""
from typing import List
from pprint import pprint

"""
给你一个字符数组 chars ，请使用下述算法压缩：
从一个空字符串 s 开始。对于 chars 中的每组 连续重复字符 ：
如果这一组长度为 1 ，则将字符追加到 s 中。
否则，需要向 s 追加字符，后跟这一组的长度。
压缩后得到的字符串 s 不应该直接返回 ，需要转储到字符数组 chars 中。
需要注意的是，如果组长度为 10 或 10 以上，则在 chars 数组中会被拆分为多个字符。
请在 修改完输入数组后 ，返回该数组的新长度。
你必须设计并实现一个只使用常量额外空间的算法来解决此问题。
"""


class Solution:
    def compress(self, chars: List[str]) -> int:
        i, j = 0, 1
        c = chars[0]
        n = 1
        while j < len(chars):
            if chars[j] == c:
                n += 1
            else:
                chars[i] = c
                i += 1
                if n > 1:
                    for s in str(n):
                        chars[i] = s
                        i += 1
                c = chars[j]
                n = 1
            j += 1
        else:
            chars[i] = c
            i += 1
            if n > 1:
                for s in str(n):
                    chars[i] = s
                    i += 1
        return i


if __name__ == '__main__':
    solution = Solution()
    print(solution.compress(["a","a","b","b","c","c","c"]))
