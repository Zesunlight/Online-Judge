# -*- coding: UTF-8 -*-
"""=================================================
Problem:    切绳子
Website: https://ac.nowcoder.com/acm/contest/12949/B
Author: ZYZ
Language: Python3
Result: 通过了所有的测试用例
=================================================="""


t = int(input())
for _ in range(t):
    day = 1
    n = int(input())
    while n > 1:
        n = max(n>>1, (n+1)>>1)
        day += 1
    print(day)
