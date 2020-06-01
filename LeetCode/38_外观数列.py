# -*- coding: UTF-8 -*-
"""
=================================================
Problem: 38. 外观数列
Website: https://leetcode-cn.com/problems/count-and-say/
Difficulty: 简单
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 60 ms, 在所有 Python3 提交中击败了19.85%的用户
Memory Usage: 13.7 MB, 在所有 Python3 提交中击败了6.67%的用户
=================================================="""


class Solution:
    """
    「外观数列」是一个整数序列，从数字 1 开始，序列中的每一项都是对前一项的描述。
    给定一个正整数 n（1 ≤ n ≤ 30），输出外观数列的第 n 项。
    """
    def countAndSay(self, n: int) -> str:
        des = '1'
        for _ in range(n-1):
            count = 1
            index = 0
            res = ''
            for index in range(len(des) - 1):
                if des[index] != des[index+1]:
                    res = res + str(count) + des[index]
                    count = 1
                else:
                    count += 1
            if count == 1:
                res = res + '1' + des[-1]
            else:
                res = res + str(count) + des[-1]
            des = res
        return des

"""
先求解出来，答案列在数组里，总共就30个
"""