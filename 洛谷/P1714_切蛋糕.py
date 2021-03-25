"""
https://www.luogu.com.cn/problem/P1714
前缀和，单调栈
"""


n, m = map(int, input().split())
cake = list(map(int, input().split()))
delicious = max(0, cake[0])
monotone = [0 for _ in range(n+1)]
for i in range(1, n):
    cake[i] += cake[i-1]
    if i < m:
        delicious = max(delicious, cake[i])

head, tail = 0, 0
for i in range(n):
    while head < tail and (i - monotone[head]) > m:
        head += 1
    delicious = max(delicious, cake[i] - cake[monotone[head]])
    while cake[i] < cake[monotone[tail]] and tail >= head:
        tail -= 1
    tail += 1
    monotone[tail] = i

print(delicious)
