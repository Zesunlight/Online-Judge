# -*- coding: UTF-8 -*-
"""
=================================================
Problem: 面试题53 - II. 0～n-1中缺失的数字
Website: https://leetcode-cn.com/problems/que-shi-de-shu-zi-lcof/
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 60 ms, 在所有 Python3 提交中击败了19.75%的用户
Memory Usage: 14.6 MB, 在所有 Python3 提交中击败了100.00%的用户
=================================================="""


class Solution:
    """
    一个长度为n-1的递增排序数组中的所有数字都是唯一的，并且每个数字都在范围0～n-1之内。
    在范围0～n-1内的n个数字中有且只有一个数字不在该数组中，请找出这个数字。
    """
    def missingNumber(self, nums: List[int]) -> int:
        if nums[-1] == len(nums) - 1:
            return len(nums)
        left, right = 0, len(nums)
        while left < right:
            middle = (left + right) // 2
            if nums[middle] == middle:
                left = middle + 1
            else:
                right = middle
        return nums[left] - 1



class Solution_2:
    def missingNumber(self, nums: List[int]) -> int:
        i, j = 0, len(nums) - 1
        while i <= j:
            m = (i + j) // 2
            if nums[m] == m: i = m + 1
            else: j = m - 1
        return i
"""
作者：jyd
链接：https://leetcode-cn.com/problems/que-shi-de-shu-zi-lcof/solution/mian-shi-ti-53-ii-0n-1zhong-que-shi-de-shu-zi-er-f/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""
