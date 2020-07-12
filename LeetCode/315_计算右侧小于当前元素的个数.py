# -*- coding: UTF-8 -*-
"""
=================================================
Problem: 315. 计算右侧小于当前元素的个数
Website: https://leetcode-cn.com/problems/count-of-smaller-numbers-after-self/
Difficulty: 困难
Author: 
Language: Python3
Result: Accepted
Runtime: 
Memory Usage: 
=================================================="""


class Solution:
    '''
    给定一个整数数组 nums，按要求返回一个新数组 counts。
    数组 counts 有该性质： counts[i] 的值是  nums[i] 右侧小于 nums[i] 的元素的数量。
    '''

    def countSmaller(self, nums: List[int]) -> List[int]:
        sortns = []
        res = []
        for n in reversed(nums):
            idx = bisect.bisect_left(sortns, n)
            res.append(idx)
            sortns.insert(idx,n)
        return res[::-1]
    
    # https://leetcode-cn.com/problems/count-of-smaller-numbers-after-self/solution/bu-dao-10xing-dai-ma-zui-jian-dan-fang-fa-mei-you-/
