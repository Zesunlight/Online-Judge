# -*- coding: UTF-8 -*-
"""
=================================================
Problem: 837. 新21点
Website: https://leetcode-cn.com/problems/new-21-game/
Difficulty: 困难
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 92 ms, 在所有 Python3 提交中击败了71.32%的用户
Memory Usage: 14.1 MB, 在所有 Python3 提交中击败了100.00%的用户
=================================================="""


class Solution:
    """
    爱丽丝参与一个大致基于纸牌游戏 “21点” 规则的游戏，描述如下：

    爱丽丝以 0 分开始，并在她的得分少于 K 分时抽取数字。 抽取时，她从 [1, W] 的范围中随机获得一个整数作为分数进行累计，其中 W 是整数。 每次抽取都是独立的，其结果具有相同的概率。

    当爱丽丝获得不少于 K 分时，她就停止抽取数字。 爱丽丝的分数不超过 N 的概率是多少？
    """
    def new21Game(self, N: int, K: int, W: int) -> float:
        if N == 0 or K == 0:
            return 1.0
        dp = [0 for _ in range(N)]
        if W >= N:
            temp = 0
            for i in range(K):
                # dp[i] = (sum(dp[:i]) + 1) / W
                dp[i] = (temp + 1) / W
                temp += dp[i]
            temp = (sum(dp[:K - 1]) + 1) / W
            for i in range(K, N):
                dp[i] = temp
        elif W < K:
            temp = 0
            for i in range(W):
                # dp[i] = (sum(dp[:i]) + 1) / W
                dp[i] = (temp + 1) / W
                temp += dp[i]
            temp = sum(dp[:W])
            for i in range(W, K):
                # dp[i] = sum(dp[i - W:i]) / W
                dp[i] = temp / W
                temp += dp[i] - dp[i - W]
            temp = sum(dp[K - W:K - 1])
            for i in range(K, min(K + W, N)):
                # dp[i] = sum(dp[i - W:K - 1]) / W
                dp[i] = temp / W
                temp -= dp[i - W]
        else:
            temp = 0
            for i in range(K):
                # dp[i] = (sum(dp[:i]) + 1) / W
                dp[i] = (temp + 1) / W
                temp += dp[i]
            temp = (sum(dp[:K - 1]) + 1)
            for i in range(K, W):
                # dp[i] = (sum(dp[:K-1]) + 1) / W
                dp[i] = temp / W
            temp = sum(dp[:K - 1])
            for i in range(W, min(K + W, N)):
                # dp[i] = sum(dp[i - W:K - 1]) / W
                dp[i] = temp / W
                temp -= dp[i - W]
        return sum(dp[K - 1:])


s = Solution()
print(s.new21Game(98, 33, 68))
# 9811, 8890, 7719    0.99898
"""
爱丽丝获胜的概率只和下一轮开始前的得分有关，因此根据得分计算概率。

令 dp[x] 表示从得分为 x 的情况开始游戏并且获胜的概率，目标是求 dp[0] 的值。

根据规则，当分数达到或超过 K 时游戏结束，游戏结束时，如果分数不超过 N 则获胜，如果分数超过 N 则失败。
因此当 K≤x≤min(N,K+W−1) 时有 dp[x]=1，当 x>min(N,K+W−1) 时有 dp[x]=0。

只有在分数不超过 NN 时才算获胜；其次，可以达到的最大分数为 K+W−1，即在最后一次抽取数字之前的分数为 K−1，并且抽到了 W。

当 0≤x<K 时，如何计算 dp[x] 的值？注意到每次在范围[1,W] 内随机抽取一个整数，且每个整数被抽取到的概率相等，因此可以得到如下状态转移方程：

dp[x] = (dp[x+1] + dp[x+2] + ⋯ + dp[x+W]) / W
​	

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/new-21-game/solution/xin-21dian-by-leetcode-solution/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""
