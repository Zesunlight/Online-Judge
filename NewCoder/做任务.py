# -*- coding: UTF-8 -*-
"""=================================================
Problem:    切绳子
Website: https://ac.nowcoder.com/acm/contest/12949/C
Author: ZYZ
Language: Python3
Result: 通过了所有的测试用例
=================================================="""


n = int(input())
h = list(map(int, input().split()))
task = [[] for _ in range(5)]

for i in range(n):
    task[h[i] - 1].append(i)

    l = 1
    for j in task:
        l *= len(j)
    if l > 0:
        print(' '.join([str(t.pop() + 1) for t in task]))
    else:
        print(-1)
