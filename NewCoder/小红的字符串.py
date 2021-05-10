# -*- coding: UTF-8 -*-
"""=================================================
Problem:    小红的字符串
Website: https://ac.nowcoder.com/acm/contest/13215/B
Author: ZYZ
Language: Python3
Result: 通过了所有的测试用例
=================================================="""


n = int(input())
s = input()
d = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

if len(s) > 62:
    print(-1)
else:
    pos = {}
    for i in range(len(d)):
        pos[d[i]] = i

    exist = set()
    change = 0
    for i in range(n):
        if s[i] not in exist:
            exist.add(s[i])
        else:
            temp = s[i]
            while temp in exist:
                change += 1
                temp = d[(pos[temp] + 1) % 62]
            else:
                exist.add(temp)
    print(change)
