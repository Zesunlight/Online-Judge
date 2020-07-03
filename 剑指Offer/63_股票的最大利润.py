# -*- coding: UTF-8 -*-
"""
=================================================
Problem: 剑指 Offer 63. 股票的最大利润
Website: https://leetcode-cn.com/problems/gu-piao-de-zui-da-li-run-lcof/
Difficulty: 中等
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 56 ms, 在所有 Python3 提交中击败了39.02%的用户
Memory Usage: 14.4 MB, 在所有 Python3 提交中击败了100.00%的用户
=================================================="""


class Solution:
    """
    假设把某股票的价格按照时间先后顺序存储在数组中，请问买卖该股票一次可能获得的最大利润是多少？
    """
    def maxProfit(self, prices: List[int]) -> int:
        stack = []
        res = 0
        for i in range(len(prices)):
            if stack:
                if prices[i] > stack[-1]:
                    res = max(res, prices[i] - stack[0])
                else:
                    while stack and (prices[i] <= stack[-1]):
                        stack.pop()
            stack.append(prices[i])
        return res

    def maxProfit_2(self, prices: List[int]) -> int:
        cost, profit = float("+inf"), 0
        for price in prices:
            cost = min(cost, price)
            profit = max(profit, price - cost)
        return profit
'''
作者：jyd
链接：https://leetcode-cn.com/problems/gu-piao-de-zui-da-li-run-lcof/solution/mian-shi-ti-63-gu-piao-de-zui-da-li-run-dong-tai-2/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
