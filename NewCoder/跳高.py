# -*- coding: UTF-8 -*-
"""=================================================
Problem:    跳高
Website: https://ac.nowcoder.com/acm/contest/12949/A
Author: ZYZ
Language: Python3
Result: 通过了所有的测试用例
=================================================="""


n, h, u = map(int, input().split())
a = list(map(int, input().split()))

if h >= u:
    print(0)
elif h == u + 1:
    print(1)
else:
    a.sort(reverse=True)
    ans = 0
    for i in a:
        h += i
        ans += 1
        if h >= u:
            print(ans)
            break
