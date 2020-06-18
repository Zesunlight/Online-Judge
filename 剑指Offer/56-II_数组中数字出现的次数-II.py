# -*- coding: UTF-8 -*-
"""
=================================================
Problem: 面试题56 - II. 数组中数字出现的次数 II
Website: https://leetcode-cn.com/problems/shu-zu-zhong-shu-zi-chu-xian-de-ci-shu-ii-lcof/
Difficulty: 简单
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 64 ms, 在所有 Python3 提交中击败了76.27%的用户
Memory Usage: 14.8 MB, 在所有 Python3 提交中击败了100.00%的用户
=================================================="""


class Solution:
    """
    在一个数组 nums 中除一个数字只出现一次之外，其他数字都出现了三次。请找出那个只出现一次的数字。
    """
    def singleNumber(self, nums: List[int]) -> int:
        return (sum(set(nums)) * 3 -  sum(nums)) // 2


class Solution_2:
    def singleNumber(self, nums: List[int]) -> int:
        ones, twos = 0, 0
        for num in nums:
            ones = ones ^ num & ~twos
            twos = twos ^ num & ~ones
        return ones
"""
作者：jyd
链接：https://leetcode-cn.com/problems/shu-zu-zhong-shu-zi-chu-xian-de-ci-shu-ii-lcof/solution/mian-shi-ti-56-ii-shu-zu-zhong-shu-zi-chu-xian-d-4/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""
