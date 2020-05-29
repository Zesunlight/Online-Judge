# -*- coding: UTF-8 -*-
"""
=================================================
Problem: 198. 打家劫舍
Website: https://leetcode-cn.com/problems/house-robber/
Difficulty: 简单
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 36 ms, 在所有 Python3 提交中击败了84.98%的用户
Memory Usage: 13.6 MB, 在所有 Python3 提交中击败了9.09%的用户
=================================================="""


class Solution:
    """
    你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

    给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。
    """
    def rob(self, nums: List[int]) -> int:
        if nums is None or len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        dp = [0 for _ in range(len(nums))]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        # last_visit = [0 for _ in range(len(nums))]
        # last_visit[1] = 1 if nums[1] > nums[0] else 0
        
        for i in range(2, len(nums)):
            if dp[i-2] + nums[i] > dp[i-1]:
                dp[i] = dp[i-2] + nums[i]
                # last_visit[i] = i
            else:
                dp[i] = dp[i-1]
        
        return dp[-1]


    def rob_2(self, nums: List[int]) -> int:
        if nums is None or len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        dp_0 = nums[0]
        dp_1 = max(nums[0], nums[1])
        
        for i in range(2, len(nums)):
            if dp_0 + nums[i] > dp_1:
                dp_0, dp_1 = dp_1, dp_0 + nums[i]
            else:
                dp_0 = dp_1
        
        return dp_1


"""
https://leetcode-cn.com/problems/house-robber/solution/da-jia-jie-she-by-leetcode-solution/
"""