# -*- coding: UTF-8 -*-
"""=================================================
Problem: 1155. 掷骰子等于目标和的方法数
Website: https://leetcode.cn/problems/number-of-dice-rolls-with-target-sum/
Difficulty: 中等
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 592 ms
Memory Usage: 16.27 MB
=================================================="""
import numpy as np

"""
这里有 n 个一样的骰子，每个骰子上都有 k 个面，分别标号为 1 到 k 。
给定三个整数 n ,  k 和 target ，返回可能的方式(从总共 kn 种方式中)滚动骰子的数量，使正面朝上的数字之和等于 target 。
答案可能很大，你需要对 109 + 7 取模 。

示例 1：
输入：n = 1, k = 6, target = 3
输出：1
解释：你扔一个有 6 个面的骰子。
得到 3 的和只有一种方法。

示例 2：
输入：n = 2, k = 6, target = 7
输出：6
解释：你扔两个骰子，每个骰子有 6 个面。
得到 7 的和有 6 种方法：1+6 2+5 3+4 4+3 5+2 6+1。

示例 3：
输入：n = 30, k = 30, target = 500
输出：222616187
解释：返回的结果必须是对 109 + 7 取模。
"""


class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        dp = [[0 for _ in range(n)] for _ in range(target + 1)]
        for i in range(1, min(k, target) + 1):
            dp[i][0] = 1
        for i in range(1, target + 1):
            for j in range(1, n):
                for h in range(1, min(k, i) + 1):
                    dp[i][j] += dp[i - h][j - 1]
        return dp[target][n-1] % (10 ** 9 + 7)

    def numRollsToTarget2(self, n: int, k: int, target: int) -> int:
        # https://leetcode.cn/problems/number-of-dice-rolls-with-target-sum/solutions/2490436/zhi-tou-zi-deng-yu-mu-biao-he-de-fang-fa-eewv/
        mod = 10 ** 9 + 7
        f = [1] + [0] * target
        for i in range(1, n + 1):
            for j in range(target, -1, -1):
                f[j] = 0
                for x in range(1, k + 1):
                    if j - x >= 0:
                        f[j] = (f[j] + f[j - x]) % mod
        return f[target]

    def numRollsToTarget3(self, n: int, k: int, t: int) -> int:
        # https://leetcode.cn/problems/number-of-dice-rolls-with-target-sum/solutions/2490436/zhi-tou-zi-deng-yu-mu-biao-he-de-fang-fa-eewv/comments/2157168
        MOD = 10 ** 9 + 7
        cur = base = np.array([0] + [1 for _ in range(min(t, k))] + [0 for _ in range(t - k)])
        for _ in range(n - 1):
            cur = (np.convolve(cur, base) % MOD)[:(t + 1)]
        return int(cur[t])

    def numRollsToTarget4(self, n: int, k: int, target: int) -> int:
        # https://leetcode.cn/problems/number-of-dice-rolls-with-target-sum/solutions/2495836/ji-bai-100cong-ji-yi-hua-sou-suo-dao-di-421ab/
        if not (n <= target <= n * k):
            return 0  # 无法组成 target
        MOD = 10 ** 9 + 7

        @cache
        def dfs(i: int, j: int) -> int:
            if i == 0:
                return int(j == 0)
            res = 0
            for x in range(min(k, j + 1)):  # 掷出了 x
                res += dfs(i - 1, j - x)
            return res % MOD

        return dfs(n, target - n)


if __name__ == '__main__':
    solution = Solution()
    result = solution.numRollsToTarget(n=1, k=6, target=3)
    print(result)
