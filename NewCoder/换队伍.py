# -*- coding: UTF-8 -*-
"""=================================================
Problem:    换队伍
Website: https://ac.nowcoder.com/acm/contest/12949/D
Author: ZYZ
Language: Python3
Result: 通过了所有的测试用例
=================================================="""


n1, n2, q = map(int, input().split())
one, two = [0 for _ in range(n1 + n2 + q + 2)], [0 for _ in range(n1 + n2 + q + 2)]
id_to_pos = {}
for i in range(n1):
    one[i] = i + 1
    id_to_pos[i + 1] = (1, i)
for i in range(n2):
    two[i] = i + n1 + 1
    id_to_pos[i + n1 + 1] = (2, i)

can = list(map(int, input().split()))
for c in can:
    pos = id_to_pos[c]
    if pos[0] == 1:
        one[pos[1]] = 0
        two[n2] = c
        id_to_pos[c] = (2, n2)
        n2 += 1
    else:
        two[pos[1]] = 0
        one[n1] = c
        id_to_pos[c] = (1, n1)
        n1 += 1

print(' '.join([str(i) for i in one if i != 0]))
print(' '.join([str(i) for i in two if i != 0]))
