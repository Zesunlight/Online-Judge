# -*- coding: UTF-8 -*-
"""=================================================
Problem: 2765. 最长交替子数组
Website: https://leetcode.cn/problems/longest-alternating-subarray/description/?envType=daily-question&envId=2024-01-23
Difficulty: 简单
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 58 ms
Memory Usage: 16.41 MB
=================================================="""
from typing import List, Dict, Set, Optional

"""
给你一个下标从 0 开始的整数数组 nums 。如果 nums 中长度为 m 的子数组 s 满足以下条件，我们称它是一个 交替子数组 ：

m 大于 1 。
s1 = s0 + 1 。
下标从 0 开始的子数组 s 与数组 [s0, s1, s0, s1,...,s(m-1) % 2] 一样。也就是说，s1 - s0 = 1 ，s2 - s1 = -1 ，s3 - s2 = 1 ，s4 - s3 = -1 ，以此类推，直到 s[m - 1] - s[m - 2] = (-1)m 。
请你返回 nums 中所有 交替 子数组中，最长的长度，如果不存在交替子数组，请你返回 -1 。

子数组是一个数组中一段连续 非空 的元素序列。
"""


class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return -1
        
        distance = 1
        res = -1
        length = -1
        i = 1
        while i < n:
            if nums[i] - nums[i-1] == distance:
                distance = -distance
                if length == -1:
                    length = 2
                else:
                    length += 1
            else:
                res = max(res, length)
                if i > 1 and length > -1:
                    i -= 1
                length = -1
                distance = 1
            i += 1
        res = max(res, length)
        return res
    
    def alternatingSubarray2(self, nums: List[int]) -> int:
        # https://leetcode.cn/problems/longest-alternating-subarray/solutions/2610815/zui-chang-jiao-ti-zi-xu-lie-by-leetcode-2aevc/
        res = -1
        firstIndex = 0
        for i in range(1, len(nums)):
            length = i - firstIndex + 1
            if nums[i] - nums[firstIndex] == (length - 1) % 2:
                res = max(res, length)
            else:
                if nums[i] - nums[i - 1] == 1:
                    firstIndex = i - 1
                    res = max(res, 2)
                else:
                    firstIndex = i
        return res

    def alternatingSubarray3(self, nums: List[int]) -> int:
        # https://leetcode.cn/problems/longest-alternating-subarray/solutions/2615916/jiao-ni-yi-ci-xing-ba-dai-ma-xie-dui-on-r57bz/
        ans = -1
        i, n = 0, len(nums)
        while i < n - 1:
            if nums[i + 1] - nums[i] != 1:
                i += 1  # 直接跳过
                continue
            i0 = i  # 记录这一组的开始位置
            i += 2  # i 和 i+1 已经满足要求，从 i+2 开始判断
            while i < n and nums[i] == nums[i - 2]:
                i += 1
            # 从 i0 到 i-1 是满足题目要求的（并且无法再延长的）子数组
            ans = max(ans, i - i0)
            i -= 1
        return ans


if __name__ == '__main__':
    solution = Solution()
    result = solution.alternatingSubarray([2,3,4,3,4])
    print(result)
