# -*- coding: UTF-8 -*-
"""=================================================
Problem: 787. K 站中转内最便宜的航班
Website: https://leetcode-cn.com/problems/cheapest-flights-within-k-stops/
Difficulty: 中等
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 580 ms
Memory Usage: 15.6 MB
=================================================="""
from typing import List
from pprint import pprint

"""
有 n 个城市通过一些航班连接。给你一个数组flights ，
其中flights[i] = [fromi, toi, pricei] ，
表示该航班都从城市 fromi 开始，以价格 pricei 抵达 toi。
现在给定所有的城市和航班，以及出发城市 src 和目的地 dst，
你的任务是找到出一条最多经过 k站中转的路线，使得从 src 到 dst 的 价格最便宜 ，
并返回该价格。 如果不存在这样的路线，则输出 -1。
"""


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        fly = [[float('inf')] * n for _ in range(n)]
        for f, t, p in flights:
            fly[f][t] = p

        dp = [[float('inf')] * n for _ in range(k + 1)]
        for i in range(n):
            dp[0][i] = fly[src][i]
        for t in range(1, k + 1):
            for i in range(n):
                for j in range(n):
                    if dp[t - 1][j] > 0 and fly[j][i] > 0:
                        dp[t][i] = min(dp[t][i], dp[t - 1][j] + fly[j][i])

        m = min([dp[t][dst] for t in range(k + 1)])
        return m if m != float('inf') else -1

    def findCheapestPrice2(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # https://leetcode-cn.com/problems/cheapest-flights-within-k-stops/solution/k-zhan-zhong-zhuan-nei-zui-bian-yi-de-ha-abzi/
        f = [[float("inf")] * n for _ in range(k + 2)]
        f[0][src] = 0
        for t in range(1, k + 2):
            for j, i, cost in flights:
                f[t][i] = min(f[t][i], f[t - 1][j] + cost)

        ans = min(f[t][dst] for t in range(1, k + 2))
        return -1 if ans == float("inf") else ans


if __name__ == '__main__':
    solution = Solution()
    print(solution.findCheapestPrice(n=5, flights=[[1, 2, 10], [2, 0, 7], [1, 3, 8], [4, 0, 10], [3, 4, 2], [4, 2, 10], [0, 3, 3], [3, 1, 6], [2, 4, 5]], src=0, dst=4, k=1))
