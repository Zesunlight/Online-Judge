# -*- coding: UTF-8 -*-
"""
=================================================
Problem: 643. 子数组最大平均数 I
Website: https://leetcode-cn.com/problems/maximum-average-subarray-i/
Difficulty: 简单
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 1160 ms
Memory Usage: 18.3 MB
=================================================="""


class Solution:
    """
    给定 n 个整数，找出平均数最大且长度为 k 的连续子数组，并输出该最大平均数。
    """
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        mm = temp = sum(nums[:k]) / k
        for i in range(k, len(nums)):
            temp = (temp * k + nums[i] - nums[i - k]) / k
            mm = max(mm, temp)
        return mm

    def findMaxAverage2(self, nums: List[int], k: int) -> float:
        maxTotal = total = sum(nums[:k])
        n = len(nums)

        for i in range(k, n):
            total = total - nums[i - k] + nums[i]
            maxTotal = max(maxTotal, total)
        
        return maxTotal / k

        # 作者：LeetCode-Solution
        # 链接：https://leetcode-cn.com/problems/maximum-average-subarray-i/solution/zi-shu-zu-zui-da-ping-jun-shu-i-by-leetc-us1k/
        # 来源：力扣（LeetCode）
        # 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
