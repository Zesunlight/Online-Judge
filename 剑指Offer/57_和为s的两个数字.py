# -*- coding: UTF-8 -*-
"""
=================================================
Problem: 面试题57. 和为s的两个数字
Website: https://leetcode-cn.com/problems/he-wei-sde-liang-ge-shu-zi-lcof/
Difficulty: 简单
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 144 ms, 在所有 Python3 提交中击败了83.19%的用户
Memory Usage: 27.2 MB, 在所有 Python3 提交中击败了100.00%的用户
=================================================="""


class Solution:
    """
    输入一个递增排序的数组和一个数字s，在数组中查找两个数，使得它们的和正好是s。
    如果有多对数字的和等于s，则输出任意一对即可。
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        partner = {}
        for i in nums:
            if i in partner:
                return [i, partner[i]]
            else:
                partner[target - i] = i
        return []


class Solution_2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i, j = 0, len(nums) - 1
        while i < j:
            s = nums[i] + nums[j]
            if s > target: j -= 1
            elif s < target: i += 1
            else: return nums[i], nums[j]
        return []
"""
作者：jyd
链接：https://leetcode-cn.com/problems/he-wei-sde-liang-ge-shu-zi-lcof/solution/mian-shi-ti-57-he-wei-s-de-liang-ge-shu-zi-shuang-/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""
