# -*- coding: UTF-8 -*-
"""=================================================
Problem:    牛牛扔牌
Website: https://ac.nowcoder.com/acm/problem/207797
Author: ZYZ
Language: Python3
Result: 通过了所有的测试用例
=================================================="""

#
# @param x string字符串 字符串从前到后分别是从上到下排列的n张扑克牌
# @return string字符串
#
class Solution:
    def Orderofpoker(self , x ):
        # write code here
        res = ''
        for i in range(len(x) // 2, 0, -1):
            if i in (2, 3, 5, 7):
                res += x[:2]
                x = x[2:]
            else:
                res += x[-2:]
                x = x[:-2]
        return res