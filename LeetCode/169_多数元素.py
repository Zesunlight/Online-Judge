# -*- coding: UTF-8 -*-
"""
=================================================
Problem: 169. 多数元素
Website: https://leetcode-cn.com/problems/majority-element/
Difficulty: 简单
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 52 ms, 在所有 Python3 提交中击败了65.53%的用户
Memory Usage: 14.9 MB, 在所有 Python3 提交中击败了6.90%的用户
=================================================="""


class Solution:
    """
    给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。

    你可以假设数组是非空的，并且给定的数组总是存在多数元素。
    """
    def majorityElement(self, nums: List[int]) -> int:
        return collections.Counter(nums).most_common(1)[0][0]

class Solution_2:
    def majorityElement(self, nums):
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)

'''
如果将数组 nums 中的所有元素按照单调递增或单调递减的顺序排序，
那么下标为 ⌊2/n⌋ 的元素（下标从 0 开始）一定是众数。
'''

'''
因为超过 ⌊2/n⌋ 的数组下标被众数占据了，这样我们随机挑选一个下标对应的元素并验证，有很大的概率能找到众数。
'''
