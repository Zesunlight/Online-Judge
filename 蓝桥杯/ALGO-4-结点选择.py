# http://lx.lanqiao.cn/problem.page?gpid=T14

from collections import defaultdict
# import sys
# sys.setrecursionlimit(100000)

with open(r'C:\Users\DF\Desktop\测试数据\结点选择-input-8.txt') as f:
    n = int(f.readline())
    nums = list(map(int, f.readline().split()))
    edge = defaultdict(list)
    value = [-1] * n
    problem = []
    for i in range(n):
        problem.append([0, nums[i]])
    for _ in range(n - 1):
        a, b = map(int, f.readline().split())
        edge[a].append(b)
        edge[b].append(a)


# n = int(input())
# nums = list(map(int, input().split()))
# edge = defaultdict(list)
# value = [-1] * n
# problem = []
# for i in range(n):
#     problem.append([0, nums[i]])
# for _ in range(n-1):
#     a, b = map(int, input().split())
#     edge[a].append(b)
#     edge[b].append(a)


def max_value(current, previous):
    if value[current-1] != -1:
        return value[current-1]
    not_choose, choose = 0, nums[current-1]
    for follow in edge[current]:
        if follow != previous:
            not_choose += max_value(follow, current)
            for further in edge[follow]:
                if further != current:
                    choose += max_value(further, follow)
    value[current-1] = max(not_choose, choose)
    return value[current-1]


def max_value2(current, previous):
    for follow in edge[current]:
        if follow == previous:
            continue
        max_value2(follow, current)
        problem[current - 1][0] += max(problem[follow - 1])
        problem[current - 1][1] += problem[follow - 1][0]


print(max_value(1, 0))
max_value2(1, 0)
print(max(problem[0]))


# 因为python递归深度的原因，只能得到70分，其他语言可以通过