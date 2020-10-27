# http://lx.lanqiao.cn/problem.page?gpid=T48


n = int(input())
# nums = list(map(int, input().split()))
for i in range(1, 10):
    for j in range(10):
        for k in range(10):
            if i + j + k + j + i == n:
                print(i * 10000 + j * 1000 + k * 100 + j * 10 + i)
for i in range(1, 10):
    for j in range(10):
        for k in range(10):
            if i + j + k + k + j + i == n:
                print(i * 100000 + j * 10000 + k * 1000 + k * 100 + j * 10 + i)
