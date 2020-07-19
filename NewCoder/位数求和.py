# -*- coding: UTF-8 -*-
"""=================================================
Problem:    位数求和
Website: https://ac.nowcoder.com/acm/problem/208125
Author: ZYZ
Language: Python3
Result: 通过了所有的测试用例
=================================================="""

#
# 返回这样的数之和
# @param n int整型 数的长度
# @param m int整型 各个为之和
# @return long长整型
#
class Solution:
    def sum(self , n , m ):
        # write code here
        r = 0
        for i in range(10 ** (n - 1), 10 ** n):
            res = 0
            temp = i
            while temp:
                reminder = temp % 10
                res += reminder
                temp //= 10
            if res == m:
                r += i
        return r