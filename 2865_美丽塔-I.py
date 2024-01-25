# -*- coding: UTF-8 -*-
"""=================================================
Problem: 2865. 美丽塔 I
Website: https://leetcode.cn/problems/beautiful-towers-i/description/?envType=daily-question&envId=2024-01-24
Difficulty: 中等
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 1368 ms
Memory Usage: 16.63 MB
=================================================="""
from typing import List

"""
给你一个长度为 n 下标从 0 开始的整数数组 maxHeights 。

你的任务是在坐标轴上建 n 座塔。第 i 座塔的下标为 i ，高度为 heights[i] 。

如果以下条件满足，我们称这些塔是 美丽 的：

1 <= heights[i] <= maxHeights[i]
heights 是一个 山脉 数组。
如果存在下标 i 满足以下条件，那么我们称数组 heights 是一个 山脉 数组：

对于所有 0 < j <= i ，都有 heights[j - 1] <= heights[j]
对于所有 i <= k < n - 1 ，都有 heights[k + 1] <= heights[k]
请你返回满足 美丽塔 要求的方案中，高度和的最大值 。

找到最大的山形（递增再递减）部分
"""


class Solution:
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        n = len(maxHeights)
        res = n
        for i in range(n):
            temp = maxHeights[i]

            standard = maxHeights[i]
            for j in range(i-1, -1, -1):
                standard = min(standard, maxHeights[j])
                temp += standard
            
            standard = maxHeights[i]
            for k in range(i+1, n):
                standard = min(standard, maxHeights[k])
                temp += standard
            res = max(res, temp)
        return res

    def maximumSumOfHeights2(self, maxHeights: List[int]) -> int:
        # https://leetcode.cn/problems/beautiful-towers-i/solutions/2614597/mei-li-ta-i-by-leetcode-solution-uqnf/
        n = len(maxHeights)
        res = 0
        prefix, suffix = [0] * n, [0] * n

        # 单调栈(存下标)
        stack1, stack2 = [], []

        for i in range(n):
            while stack1 and maxHeights[i] < maxHeights[stack1[-1]]:
                stack1.pop()
            if stack1:
                prefix[i] = prefix[stack1[-1]] + (i - stack1[-1]) * maxHeights[i]
            else:
                prefix[i] = (i + 1) * maxHeights[i]
            stack1.append(i)

        for i in range(n - 1, -1, -1):
            while stack2 and maxHeights[i] < maxHeights[stack2[-1]]:
                stack2.pop()
            if stack2:
                suffix[i] = suffix[stack2[-1]] + (stack2[-1] - i) * maxHeights[i]
            else:
                suffix[i] = (n - i) * maxHeights[i]
            stack2.append(i)
        
        for i in range(n):
            res = max(res, prefix[i] + suffix[i] - maxHeights[i])
            
        return res


if __name__ == '__main__':
    solution = Solution()
    result = solution.maximumSumOfHeights([6,5,3,9,2,7])
    print(result)
