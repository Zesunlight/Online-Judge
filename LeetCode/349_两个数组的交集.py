# -*- coding: UTF-8 -*-
"""
=================================================
Problem: 349. 两个数组的交集
Website: https://leetcode-cn.com/problems/intersection-of-two-arrays/
Difficulty: 简单
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 60 ms, 在所有 Python3 提交中击败了71.50%的用户
Memory Usage: 13.7 MB, 在所有 Python3 提交中击败了5.88%的用户
=================================================="""


class Solution:
    '''
    给定两个数组，编写一个函数来计算它们的交集。
    '''

    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))

    def intersection2(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        length1, length2 = len(nums1), len(nums2)
        intersection = list()
        index1 = index2 = 0
        while index1 < length1 and index2 < length2:
            num1 = nums1[index1]
            num2 = nums2[index2]
            if num1 == num2:
                # 保证加入元素的唯一性
                if not intersection or num1 != intersection[-1]:
                    intersection.append(num1)
                index1 += 1
                index2 += 1
            elif num1 < num2:
                index1 += 1
            else:
                index2 += 1
        return intersection

# 作者：LeetCode-Solution
# 链接：https://leetcode-cn.com/problems/intersection-of-two-arrays/solution/liang-ge-shu-zu-de-jiao-ji-by-leetcode-solution/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。