class Solution:
    # https://leetcode-cn.com/problems/Uh984O/
    
    def combination(self, n: int, k: int) -> int:
        if k > n:
            return 0

        res = 1
        for i in range(k):
            res = res * (n - i) // (i + 1)
        return res

    def keyboard(self, k: int, n: int) -> int:
        dp = [[0 for _ in range(n + 1)] for _ in range(27)]
        for i in range(27):
            dp[i][1] = i
            dp[i][0] = 1
        for i in range(n + 1):
            dp[1][i] = 1 if i <= k else 0

        for i in range(2, 27):
            for j in range(2, n + 1):
                for c in range(min(k, j) + 1):
                    dp[i][j] = (dp[i][j] + dp[i - 1][j - c] * self.combination(j, c)) % 1000000007

        return dp[26][n]