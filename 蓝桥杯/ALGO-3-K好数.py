# http://lx.lanqiao.cn/problem.page?gpid=T13


# n = int(input())
# nums = list(map(int, input().split()))

k, l = map(int, input().split())
dp = [[0] * k for _ in range(l + 1)]
for i in range(k):
    dp[1][i] = 1

for i in range(2, l + 1):
    for j in range(k):
        dp[i][j] = sum(dp[i-1]) - \
                   (dp[i-1][j-1] if j-1 >= 0 else 0) - \
                   (dp[i-1][j+1] if j+1 < k else 0)
s = 0
for i in range(1, k):
    s = (s + dp[l][i]) % 1000000007

print(s)

# https://imwtx.com/archives/40/
# https://staight.github.io/2018/10/12/k%E5%A5%BD%E6%95%B0/