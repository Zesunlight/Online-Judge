# -*- coding: UTF-8 -*-
"""=================================================
Problem: 303. 区域和检索 - 数组不可变
Website: https://leetcode.cn/problems/range-sum-query-immutable/description/?envType=daily-question&envId=2024-03-19
Difficulty: 简单
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 51 ms
Memory Usage: 20.4 MB
=================================================="""
from typing import List
from itertools import accumulate


class NumArray:

    def __init__(self, nums: List[int]):
        # s = list(accumulate(nums, initial=0))
        # 在前面多加一个0，就不用判断边界条件（dummy node）
        self.sn = [nums[0]]
        for i in range(1, len(nums)):
            self.sn.append(self.sn[-1] + nums[i])

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.sn[right]
        else:
            return self.sn[right] - self.sn[left-1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)

