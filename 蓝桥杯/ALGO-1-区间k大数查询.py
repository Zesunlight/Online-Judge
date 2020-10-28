# http://lx.lanqiao.cn/problem.page?gpid=T11


n = int(input())
nums = list(map(int, input().split()))
# n = 5
# nums = [1, 2, 3, 4, 5]
# dp = [[[0] * (n + 1) for _ in range(n + 1)] for _ in range(n + 1)]
# for i in range(1, n + 1):
#     dp[i][i][1] = nums[i - 1]
#
# for l in range(1, n + 1):
#     for r in range(l + 1, n + 1):
#         for k in range(1, r - l + 2):
#             if dp[l][r][k] != 0:
#                 continue
#             if k == r - l + 1:
#                 dp[l][r][k] = min(nums[r - 1], dp[l][r-1][k-1])
#                 continue
#             if nums[r - 1] <= dp[l][r-1][k]:
#                 dp[l][r][k] = dp[l][r-1][k]
#             else:
#                 dp[l][r][k+1] = dp[l][r-1][k]
#                 if k == 1:
#                     dp[l][r][k] = nums[r - 1]
#                     continue
#                 if nums[r - 1] > dp[l][r-1][k-1]:
#                     dp[l][r][k] = dp[l][r-1][k-1]
#                 else:
#                     dp[l][r][k] = nums[r - 1]

m = int(input())
for _ in range(m):
    l, r, k = map(int, input().split())
    print(sorted(nums[l-1:r], reverse=True)[k-1])
    # print(dp[l][r][k])
