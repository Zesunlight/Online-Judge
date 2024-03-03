# -*- coding: UTF-8 -*-
"""=================================================
Problem: 2369. 检查数组是否存在有效划分
Website: https://leetcode.cn/problems/check-if-there-is-a-valid-partition-for-the-array/description/
Difficulty: 中等
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 137 ms
Memory Usage: 60.06 MB
=================================================="""
from typing import List

'''
给你一个下标从 0 开始的整数数组 nums ，你必须将数组划分为一个或多个 连续 子数组。

如果获得的这些子数组中每个都能满足下述条件 之一 ，则可以称其为数组的一种 有效 划分：
子数组 恰 由 2 个相等元素组成，例如，子数组 [2,2] 。
子数组 恰 由 3 个相等元素组成，例如，子数组 [4,4,4] 。
子数组 恰 由 3 个连续递增元素组成，并且相邻元素之间的差值为 1 。例如，子数组 [3,4,5] ，但是子数组 [1,3,5] 不符合要求。
如果数组 至少 存在一种有效划分，返回 true ，否则，返回 false 。
'''


class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        answer = set()
        n = len(nums)

        def dfs(start: int):
            if start in answer:
                return False
            rest = n - start
            if rest <= 1:
                return False
            if rest == 2:
                return nums[start] == nums[start + 1]
            if rest == 3:
                if nums[start] == nums[start + 1] and nums[start + 1] == nums[start + 2]:
                    return True
                if nums[start] + 1 == nums[start + 1] and nums[start + 1] + 1 == nums[start + 2]:
                    return True
                return False

            if nums[start] == nums[start + 1]:
                if dfs(start + 2):
                    return True
                else:
                    answer.add(start + 2)
            if (nums[start] == nums[start + 1] and nums[start + 1] == nums[start + 2]) or \
                    (nums[start] + 1 == nums[start + 1] and nums[start + 1] + 1 == nums[start + 2]):
                if dfs(start + 3):
                    return True
                else:
                    answer.add(start + 3)

            return False

        return dfs(0)

    def validPartition2(self, nums: List[int]) -> bool:
        # https://leetcode.cn/problems/check-if-there-is-a-valid-partition-for-the-array/solutions/2654315/jian-cha-shu-zu-shi-fou-cun-zai-you-xiao-8597
        n = len(nums)
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(1, n + 1):
            if i >= 2:
                dp[i] = dp[i - 2] and self.validTwo(nums[i - 2], nums[i - 1])
            if i >= 3:
                dp[i] = dp[i] or (dp[i - 3] and self.validThree(nums[i - 3], nums[i - 2], nums[i - 1]))
        return dp[-1]

    def validTwo(self, num1: int, num2: int) -> bool:
        return num1 == num2

    def validThree(self, num1: int, num2: int, num3: int) -> bool:
        return (num1 == num2 == num3) or (num1 + 2 == num2 + 1 == num3)


if __name__ == '__main__':
    solution = Solution()
    result = solution.validPartition([4, 4, 4, 5, 6])
    print(result)
