# -*- coding: UTF-8 -*-
"""=================================================
Problem: 1646. 获取生成数组中的最大值
Website: https://leetcode-cn.com/problems/get-maximum-in-generated-array/
Difficulty: 简单
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 28 ms
Memory Usage: 14.9 MB
=================================================="""

"""
给你一个整数 n 。按下述规则生成一个长度为 n + 1 的数组 nums ：
nums[0] = 0
nums[1] = 1
当 2 <= 2 * i <= n 时，nums[2 * i] = nums[i]
当 2 <= 2 * i + 1 <= n 时，nums[2 * i + 1] = nums[i] + nums[i + 1]
返回生成数组 nums 中的 最大 值。
"""


class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n == 0:
            return 0
        nums = [0] * (n + 1)
        nums[1] = 1
        m = 1
        for i in range(2, n + 1):
            if i % 2 == 0:
                nums[i] = nums[i // 2]
            else:
                nums[i] = nums[i // 2] + nums[i // 2 + 1]
            m = max(m, nums[i])
        return m


if __name__ == '__main__':
    solution = Solution()
    print(solution.getMaximumGenerated(7))
