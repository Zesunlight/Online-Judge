# -*- coding: UTF-8 -*-
"""=================================================
Problem: 123. 买卖股票的最佳时机 III
Website: https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-iii/
Difficulty: 困难
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 1204 ms
Memory Usage: 58.54 MB
=================================================="""
from typing import List, Dict, Set

"""
给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。
设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易。

注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-iii/solutions/71209/tong-su-yi-dong-de-dong-tai-gui-hua-jie-fa-by-marc/
        # 第 i 天
        # 未买入0  买入1
        # 剩余交易次数
        dp = [[[0, 0, 0], [float('-inf'), -prices[0], -prices[0]]] for _ in range(len(prices))]
        for i in range(1, len(prices)):
            dp[i][0][0] = max(dp[i - 1][0][0], dp[i - 1][1][1] + prices[i])
            dp[i][0][1] = max(dp[i - 1][0][1], dp[i - 1][1][2] + prices[i])
            dp[i][0][2] = dp[i - 1][0][2]
            dp[i][1][0] = float('-inf')
            dp[i][1][1] = max(dp[i - 1][0][1] - prices[i], dp[i - 1][1][1])
            dp[i][1][2] = max(dp[i - 1][0][2] - prices[i], dp[i - 1][1][2])
        return dp[len(prices) - 1][0][0]

    def maxProfit2(self, prices: List[int]) -> int:
        # https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-iii/description/
        n = len(prices)
        buy1 = buy2 = -prices[0]
        sell1 = sell2 = 0
        for i in range(1, n):
            buy1 = max(buy1, -prices[i])
            sell1 = max(sell1, buy1 + prices[i])
            buy2 = max(buy2, sell1 - prices[i])
            sell2 = max(sell2, buy2 + prices[i])
        return sell2


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxProfit([3, 2]))
