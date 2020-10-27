# http://lx.lanqiao.cn/problem.page?gpid=T7


# n = int(input())
n, m = list(map(int, input().split()))
for i in range(n):
    p = [chr(j) for j in range(ord('A') + i, max(ord('A') + i - m, ord('A') - 1), -1)]
    p.extend([chr(j) for j in range(ord('B'), ord('A') + m - i)])
    print(''.join(p))
