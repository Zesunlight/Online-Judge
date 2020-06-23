# -*- coding: UTF-8 -*-
"""
=================================================
Problem: 136. 只出现一次的数字
Website: https://leetcode-cn.com/problems/single-number/
Difficulty: 简单
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 52 ms, 在所有 Python3 提交中击败了42.35%的用户
Memory Usage: 15.4 MB, 在所有 Python3 提交中击败了5.26%的用户
=================================================="""


class Solution:
    """
    给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
    """
    def singleNumber(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] = nums[i-1] ^ nums[i]
        return nums[-1]

    def singleNumber_2(self, nums: List[int]) -> int:
        return reduce(lambda x, y: x ^ y, nums)

"""
异或运算有以下三个性质。

任何数和 0 做异或运算，结果仍然是原来的数，即 a⊕0=a。
任何数和其自身做异或运算，结果是 0，即 a⊕a=0。
异或运算满足交换律和结合律，即 a⊕b⊕a=b⊕a⊕a=b⊕(a⊕a)=b⊕0=b。


作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/single-number/solution/zhi-chu-xian-yi-ci-de-shu-zi-by-leetcode-solution/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""
