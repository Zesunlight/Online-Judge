# -*- coding: UTF-8 -*-
"""=================================================
Problem: 2789. 合并后数组中的最大元素
Website: https://leetcode.cn/problems/largest-element-in-an-array-after-merge-operations/description/?envType=daily-question&envId=2024-03-14
Difficulty: 中等
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 255 ms
Memory Usage: 28.09 MB
=================================================="""
from typing import List


'''
给你一个下标从 0 开始、由正整数组成的数组 nums 。

你可以在数组上执行下述操作 任意 次：

选中一个同时满足 0 <= i < nums.length - 1 和 nums[i] <= nums[i + 1] 的整数 i 。将元素 nums[i + 1] 替换为 nums[i] + nums[i + 1] ，并从数组中删除元素 nums[i] 。
返回你可以从最终数组中获得的 最大 元素的值。
'''


class Solution:
    def maxArrayValue(self, nums: List[int]) -> int:
        # 不断缩短非递减序列
        change = True
        result = max(nums)
        while change:
            change = False
            k = len(nums) - 1
            while k > 0:
                if nums[k] != -1:
                    h = k - 1
                    while h >= 0 and nums[h] == -1:
                        h -= 1
                    if h >= 0 and nums[k] >= nums[h]:
                        nums[h] += nums[k]
                        result = max(result, nums[h])
                        nums[k] = -1
                        change = True
                k -= 1
        return result

    def maxArrayValue2(self, nums: List[int]) -> int:
        # https://leetcode.cn/problems/largest-element-in-an-array-after-merge-operations/solutions/2679835/he-bing-hou-shu-zu-zhong-de-zui-da-yuan-s2b5o/
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] <= nums[i + 1]:
                nums[i] += nums[i + 1]
        return nums[0]


if __name__ == '__main__':
    s = Solution()
    print(s.maxArrayValue([5,3,3]))
