# -*- coding: UTF-8 -*-
"""
=================================================
Problem: 数位之积（vivo2020届春季校园招聘在线编程考试）
Website: https://www.nowcoder.com/question/next?pid=22390442&qid=925105&tid=33888152
Author: ZYZ
Language: Python3
Result: 通过了所有的测试用例
=================================================="""

#
# 输入一个整形数值，返回一个整形值
# @param n int整型 n>9
# @return int整型
#
class Solution:
    def solution(self , n ):
        # write code here
        self.n = n
        two = self.how_many(2)
        three = self.how_many(3)
        five = self.how_many(5)
        seven = self.how_many(7)

        if self.n == 1:
            eight = two // 3
            two = two % 3
            nine = three // 2
            three = three % 2
            six = min(two, three)
            two = two - min(two, three)
            three = three - min(two, three)
            four = two // 2
            two = two % 2
            res = ''
            if two > 0:
                res += two * '2'
            if three > 0:
                res += three * '3'
            if four > 0:
                res += four * '4'
            if five > 0:
                res += five * '5'
            if six > 0:
                res += six * '6'
            if seven > 0:
                res += seven * '7'
            if eight > 0:
                res += eight * '8'
            if nine > 0:
                res += nine * '9'
            return int(res)
        else:
            return -1
        
    def how_many(self, i):
        r = 0
        while self.n % i == 0:
            r += 1
            self.n = self.n / i
        return r
