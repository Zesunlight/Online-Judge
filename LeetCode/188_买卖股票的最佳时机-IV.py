# -*- coding: UTF-8 -*-
"""=================================================
Problem: 188. 买卖股票的最佳时机 IV
Website: https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-iv/
Difficulty: 困难
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 156 ms
Memory Usage: 18.52 MB
=================================================="""
from typing import List, Dict, Set

"""
给你一个整数数组 prices 和一个整数 k ，其中 prices[i] 是某支给定的股票在第 i 天的价格。
设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。也就是说，你最多可以买 k 次，卖 k 次。

注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
"""


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        dp = [[[0 for _ in range(k + 1)], [0 for _ in range(k + 1)]] for _ in range(n)]
        # 第i天  买入1/未买入0  第i次交易已完成
        dp[0][1][0] = -prices[0]
        for i in range(1, k + 1):
            dp[0][1][i] = float('-inf')
            dp[0][0][i] = float('-inf')

        for i in range(1, n):
            dp[i][0][0] = dp[i - 1][0][0]
            dp[i][1][0] = max(dp[i - 1][0][0] - prices[i], dp[i - 1][1][0])
            for j in range(1, k + 1):
                dp[i][0][j] = max(dp[i - 1][0][j], dp[i - 1][1][j - 1] + prices[i])
                dp[i][1][j] = max(dp[i - 1][1][j], dp[i - 1][0][j] - prices[i])
        return max(dp[n - 1][0])

    def maxProfit2(self, k: int, prices: List[int]) -> int:
        # https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-iv/solutions/537731/mai-mai-gu-piao-de-zui-jia-shi-ji-iv-by-8xtkp/
        if not prices:
            return 0

        n = len(prices)
        k = min(k, n // 2)
        buy = [[0] * (k + 1) for _ in range(n)]
        sell = [[0] * (k + 1) for _ in range(n)]

        buy[0][0], sell[0][0] = -prices[0], 0
        for i in range(1, k + 1):
            buy[0][i] = sell[0][i] = float("-inf")

        for i in range(1, n):
            buy[i][0] = max(buy[i - 1][0], sell[i - 1][0] - prices[i])
            for j in range(1, k + 1):
                buy[i][j] = max(buy[i - 1][j], sell[i - 1][j] - prices[i])
                sell[i][j] = max(sell[i - 1][j], buy[i - 1][j - 1] + prices[i])

        return max(sell[n - 1])

    def maxProfit3(self, k: int, prices: List[int]) -> int:
        # https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-iv/solutions/537731/mai-mai-gu-piao-de-zui-jia-shi-ji-iv-by-8xtkp/
        if not prices:
            return 0

        n = len(prices)
        k = min(k, n // 2)
        buy = [0] * (k + 1)
        sell = [0] * (k + 1)

        buy[0], sell[0] = -prices[0], 0
        for i in range(1, k + 1):
            buy[i] = sell[i] = float("-inf")

        for i in range(1, n):
            buy[0] = max(buy[0], sell[0] - prices[i])
            for j in range(1, k + 1):
                buy[j] = max(buy[j], sell[j] - prices[i])
                sell[j] = max(sell[j], buy[j - 1] + prices[i])

        return max(sell)


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxProfit(k=2, prices=[2, 4, 1]))
