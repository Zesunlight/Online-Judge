# -*- coding: UTF-8 -*-
"""=================================================
Problem:    寻宝
Website: https://ac.nowcoder.com/acm/contest/13215/A
Author: ZYZ
Language: Python3
Result: 通过了所有的测试用例
=================================================="""


from math import ceil

k, a, b = map(int, input().split())

if k == 0:
    print(0)
elif k > 0:
    if a >= k:
        print(1)
    elif b >= a:
        print(-1)
    else:
        print(ceil((k - a) / (a - b)) + 1)
else:
    if a >= b:
        print(-1)
    else:
        print(ceil((-k) / (b - a)))
