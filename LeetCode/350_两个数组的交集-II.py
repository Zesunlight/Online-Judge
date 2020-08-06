# -*- coding: UTF-8 -*-
"""
=================================================
Problem: 350. 两个数组的交集 II
Website: https://leetcode-cn.com/problems/intersection-of-two-arrays-ii/
Difficulty: 简单
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 64 ms, 在所有 Python3 提交中击败了64.99%的用户
Memory Usage: 13.7 MB, 在所有 Python3 提交中击败了12.50%的用户
=================================================="""


class Solution:
    '''
    给定两个数组，编写一个函数来计算它们的交集。
    '''

    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums1 or not nums2:
            return []
        
        nums1.sort()
        nums2.sort()
        res = []
        one, two = 0, 0

        while one < len(nums1) and two < len(nums2):
            if nums1[one] < nums2[two]:
                one += 1
            elif nums1[one] > nums2[two]:
                two += 1
            else:
                res.append(nums1[one])
                one += 1
                two += 1
        
        return res


    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        '''
    由于同一个数字在两个数组中都可能出现多次，因此需要用哈希表存储每个数字出现的次数。
    对于一个数字，其在交集中出现的次数等于该数字在两个数组中出现次数的最小值。

    首先遍历第一个数组，并在哈希表中记录第一个数组中的每个数字以及对应出现的次数，
    然后遍历第二个数组，对于第二个数组中的每个数字，如果在哈希表中存在这个数字，则将该数字添加到答案，并减少哈希表中该数字出现的次数。

    为了降低空间复杂度，首先遍历较短的数组并在哈希表中记录每个数字以及对应出现的次数，然后遍历较长的数组得到交集。

    作者：LeetCode-Solution
    链接：https://leetcode-cn.com/problems/intersection-of-two-arrays-ii/solution/liang-ge-shu-zu-de-jiao-ji-ii-by-leetcode-solution/
    来源：力扣（LeetCode）
    著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
        '''
        if len(nums1) > len(nums2):
            return self.intersect(nums2, nums1)
        
        m = collections.Counter()
        for num in nums1:
            m[num] += 1
        
        intersection = list()
        for num in nums2:
            if (count := m.get(num, 0)) > 0:
                intersection.append(num)
                m[num] -= 1
                if m[num] == 0:
                    m.pop(num)
        
        return intersection

